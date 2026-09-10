import json
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression, LinearRegression, Ridge, Lasso
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.model_selection import TimeSeriesSplit
from sklearn.metrics import accuracy_score, r2_score, mean_absolute_error, mean_squared_error
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

FEATURES = ["Return", "MA20", "MA50", "Vol20", "Mom10", "Volume_Ratio", "RSI", "MACD", "BB_Position"]


def load_and_engineer(path):
    df = pd.read_csv(path, index_col="Date")
    df.index = pd.to_datetime(df.index, utc=True)
    df = df.sort_index()

    price = df["Close"]
    df["Return"] = np.log(price / price.shift(1))
    df["MA20"] = price.rolling(20).mean()
    df["MA50"] = price.rolling(50).mean()
    df["MA200"] = price.rolling(200).mean()
    df["Vol20"] = df["Return"].rolling(20).std()
    df["Mom10"] = price / price.shift(10)
    df["Volume_Ratio"] = df["Volume"] / df["Volume"].rolling(20).mean()

    delta = price.diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    avg_gain = gain.rolling(14).mean()
    avg_loss = loss.rolling(14).mean().replace(0, 1e-10)
    df["RSI"] = 100 - (100 / (1 + avg_gain / avg_loss))

    ema12 = price.ewm(span=12, adjust=False).mean()
    ema26 = price.ewm(span=26, adjust=False).mean()
    df["MACD"] = ema12 - ema26

    bb_mid = price.rolling(20).mean()
    bb_std = price.rolling(20).std()
    df["BB_Position"] = (price - bb_mid) / (2 * bb_std)

    return df.dropna()


def analyze(df, name):
    df = df.copy()
    df["Target"] = (df["Close"].shift(-1) > df["Close"]).astype(int)
    df = df.dropna()

    X = df[FEATURES]
    y = df["Target"]
    tscv = TimeSeriesSplit(n_splits=5)

    acc = {"Logistic Regression": [], "Random Forest": [], "Gradient Boosting": []}
    for train_idx, test_idx in tscv.split(X):
        X_train, X_test = X.iloc[train_idx], X.iloc[test_idx]
        y_train, y_test = y.iloc[train_idx], y.iloc[test_idx]

        scaler = StandardScaler()
        X_train_s = scaler.fit_transform(X_train)
        X_test_s = scaler.transform(X_test)

        lr = LogisticRegression(max_iter=1000).fit(X_train_s, y_train)
        acc["Logistic Regression"].append(accuracy_score(y_test, lr.predict(X_test_s)))

        rf = RandomForestClassifier(n_estimators=200, random_state=42).fit(X_train, y_train)
        acc["Random Forest"].append(accuracy_score(y_test, rf.predict(X_test)))

        gb = GradientBoostingClassifier(n_estimators=200, random_state=42).fit(X_train, y_train)
        acc["Gradient Boosting"].append(accuracy_score(y_test, gb.predict(X_test)))

    final_rf = RandomForestClassifier(n_estimators=200, random_state=42).fit(X, y)
    importances = pd.Series(final_rf.feature_importances_, index=FEATURES).sort_values(ascending=False)

    X_scaled = StandardScaler().fit_transform(X)
    X_pca = PCA(n_components=2).fit_transform(X_scaled)
    regime = KMeans(n_clusters=3, random_state=42, n_init=10).fit_predict(X_pca)
    regime_counts = pd.Series(regime).value_counts().sort_index()

    returns = df["Return"]
    sharpe = (returns.mean() / returns.std()) * np.sqrt(252)
    cum_return = (1 + returns).cumprod()
    drawdown = (cum_return - cum_return.cummax()) / cum_return.cummax()
    years = (df.index[-1] - df.index[0]).days / 365.25
    cagr = cum_return.iloc[-1] ** (1 / years) - 1

    df["Target_Return"] = df["Return"].shift(-1)
    df_reg = df.dropna(subset=["Target_Return"])
    X_reg = df_reg[FEATURES]
    y_reg = df_reg["Target_Return"]

    reg_models = {
        "Linear Regression": LinearRegression(),
        "Ridge Regression": Ridge(alpha=1.0),
        "Lasso Regression": Lasso(alpha=0.001),
    }
    reg_results = {}
    for reg_name, model in reg_models.items():
        r2s, rmses, maes = [], [], []
        for train_idx, test_idx in tscv.split(X_reg):
            X_train, X_test = X_reg.iloc[train_idx], X_reg.iloc[test_idx]
            y_train, y_test = y_reg.iloc[train_idx], y_reg.iloc[test_idx]

            scaler = StandardScaler()
            X_train_s = scaler.fit_transform(X_train)
            X_test_s = scaler.transform(X_test)

            model.fit(X_train_s, y_train)
            preds = model.predict(X_test_s)

            r2s.append(r2_score(y_test, preds))
            rmses.append(mean_squared_error(y_test, preds) ** 0.5)
            maes.append(mean_absolute_error(y_test, preds))

        reg_results[reg_name] = {
            "r2": float(np.mean(r2s)),
            "rmse": float(np.mean(rmses)),
            "mae": float(np.mean(maes)),
        }

    return {
        "name": name,
        "rows": int(len(df)),
        "date_start": str(df.index[0].date()),
        "date_end": str(df.index[-1].date()),
        "accuracy": {k: float(np.mean(v)) for k, v in acc.items()},
        "feature_importance": {k: round(float(v), 4) for k, v in importances.items()},
        "regime_counts": {str(k): int(v) for k, v in regime_counts.items()},
        "sharpe": float(sharpe),
        "max_drawdown": float(drawdown.min()),
        "cagr": float(cagr),
        "regression": reg_results,
    }


BASE_DIR = Path(__file__).parent

STOCKS = {
    "Adobe": BASE_DIR / "Adobe(ADBE)Stock" / "Adobe (ADBE) From 1986 To Dec-2024.csv",
    "Microsoft": BASE_DIR / "MicrosoftStock" / "Microsoft_stock_history.csv",
    "Oracle": BASE_DIR / "OracleStock" / "oracle.csv",
    "Salesforce": BASE_DIR / "SalesforceStock" / "Salesforce (CRM) From 2004 To Dec-2024.csv",
}

results = {}
for name, path in STOCKS.items():
    print(f"Analyzing {name}...")
    df = load_and_engineer(path)
    results[name] = analyze(df, name)

with open(BASE_DIR / "dashboard_data.json", "w") as f:
    json.dump(results, f, indent=2)

print("Saved", BASE_DIR / "dashboard_data.json")
