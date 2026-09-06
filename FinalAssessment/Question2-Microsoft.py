import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
import os
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import TimeSeriesSplit
from sklearn.metrics import accuracy_score
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

MS_FOLDER = "FinalAssessment/MicrosoftStock"

# ---------- 1. Company profile (info.csv) ----------

info_df = pd.read_csv(f"{MS_FOLDER}/Microsoft_stock_info.csv", header=None, names=["Field", "Value"])
print("=== Company Info ===")
print(info_df.to_string(index=False))

# ---------- 2. Load the 3 files we will merge ----------

history_df = pd.read_csv(f"{MS_FOLDER}/Microsoft_stock_history.csv", index_col="Date")
history_df.index = pd.to_datetime(history_df.index, utc=True)
history_df = history_df.sort_index()

dividends_df = pd.read_csv(f"{MS_FOLDER}/Microsoft_stock_dividends.csv", index_col="Date")
dividends_df.index = pd.to_datetime(dividends_df.index, utc=True)

splits_df = pd.read_csv(f"{MS_FOLDER}/Microsoft_stock_spilts.csv", index_col="Date")
splits_df.index = pd.to_datetime(splits_df.index, utc=True)

# ---------- 3. Merge history + dividends + splits ----------

df = history_df.merge(dividends_df, how="left", left_index=True, right_index=True)
df = df.merge(splits_df, how="left", left_index=True, right_index=True)
df["Dividends"] = df["Dividends"].fillna(0)
df["Stock Splits"] = df["Stock Splits"].fillna(0)

# ---------- 4. Data validation using the 5th file (action.csv) ----------

action_df = pd.read_csv(f"{MS_FOLDER}/Microsoft_stock_action.csv", index_col="Date")
action_df.index = pd.to_datetime(action_df.index, utc=True)

print("\n=== Data Validation: action.csv vs merged dividends/splits ===")
print("Action file total dividends:", action_df["Dividends"].sum())
print("Merged data total dividends:", df["Dividends"].sum())
print("Action file split events:", (action_df["Stock Splits"] > 0).sum())
print("Merged data split events:", (df["Stock Splits"] > 0).sum())

# ---------- 5. Descriptive statistics ----------

print("\n=== Descriptive Statistics ===")
print(df.shape)
print(df.dtypes)
print(df.head())
print("Dividend-paying days:\n", df[df["Dividends"] > 0].head())
print("Stock split days:\n", df[df["Stock Splits"] > 0])
print(df[["Open", "High", "Low", "Close", "Volume"]].describe())

# ---------- 6. Feature engineering ----------

price = df["Close"]
df["Return"] = np.log(price / price.shift(1))
df["MA20"] = price.rolling(20).mean()
df["MA50"] = price.rolling(50).mean()
df["MA200"] = price.rolling(200).mean()
df["Vol20"] = df["Return"].rolling(20).std()
df["Mom10"] = price / price.shift(10)
df["Volume_Ratio"] = df["Volume"] / df["Volume"].rolling(20).mean()
df = df.dropna()
print("\nShape after feature engineering:", df.shape)

# ---------- 7. Seaborn EDA ----------

os.makedirs("FinalAssessment/output_plots", exist_ok=True)

sns.histplot(df["Return"], kde=True)
plt.title("Microsoft - Return Distribution")
plt.savefig("FinalAssessment/output_plots/Microsoft_returns.png")
plt.close()

cols = ["Return", "Volume_Ratio", "Vol20", "Mom10"]
sns.heatmap(df[cols].corr(), annot=True, cmap="coolwarm")
plt.title("Microsoft - Correlation Heatmap")
plt.savefig("FinalAssessment/output_plots/Microsoft_corr.png")
plt.close()

plt.figure(figsize=(10, 5))
plt.plot(df.index, df["Close"], label="Close")
plt.plot(df.index, df["MA50"], label="MA50")
plt.plot(df.index, df["MA200"], label="MA200")
plt.legend()
plt.title("Microsoft - Price Trend")
plt.savefig("FinalAssessment/output_plots/Microsoft_trend.png")
plt.close()

print("Plots saved")

# ---------- 8. Scikit-Learn models ----------

df["Target"] = (df["Close"].shift(-1) > df["Close"]).astype(int)
df = df.dropna()

features = ["Return", "MA20", "MA50", "Vol20", "Mom10", "Volume_Ratio"]
X = df[features]
y = df["Target"]

tscv = TimeSeriesSplit(n_splits=5)
acc_lr, acc_rf = [], []

for train_idx, test_idx in tscv.split(X):
    X_train, X_test = X.iloc[train_idx], X.iloc[test_idx]
    y_train, y_test = y.iloc[train_idx], y.iloc[test_idx]

    scaler = StandardScaler()
    X_train_s = scaler.fit_transform(X_train)
    X_test_s = scaler.transform(X_test)

    lr = LogisticRegression(max_iter=1000)
    lr.fit(X_train_s, y_train)
    acc_lr.append(accuracy_score(y_test, lr.predict(X_test_s)))

    rf = RandomForestClassifier(n_estimators=200, random_state=42)
    rf.fit(X_train, y_train)
    acc_rf.append(accuracy_score(y_test, rf.predict(X_test)))

print("\nLogistic Regression avg accuracy:", np.mean(acc_lr))
print("Random Forest avg accuracy:", np.mean(acc_rf))

final_rf = RandomForestClassifier(n_estimators=200, random_state=42).fit(X, y)
importances = pd.Series(final_rf.feature_importances_, index=features).sort_values(ascending=False)
print("Feature importances:\n", importances)

# ---------- 9. Clustering (KMeans + PCA) ----------

X_scaled = StandardScaler().fit_transform(X)
X_pca = PCA(n_components=2).fit_transform(X_scaled)
df["Regime"] = KMeans(n_clusters=3, random_state=42, n_init=10).fit_predict(X_pca)

plt.figure(figsize=(8, 5))
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=df["Regime"], cmap="viridis", s=8)
plt.title("Microsoft - Market Regimes (KMeans + PCA)")
plt.savefig("FinalAssessment/output_plots/Microsoft_regimes.png")
plt.close()

print(df["Regime"].value_counts())

# ---------- 10. Backtesting metrics ----------

returns = df["Return"]
sharpe = (returns.mean() / returns.std()) * np.sqrt(252)
cum_return = (1 + returns).cumprod()
drawdown = (cum_return - cum_return.cummax()) / cum_return.cummax()
years = (df.index[-1] - df.index[0]).days / 365.25
cagr = cum_return.iloc[-1] ** (1 / years) - 1

print("\nSharpe Ratio:", sharpe)
print("Max Drawdown:", drawdown.min())
print("CAGR:", cagr)

# ---------- 11. Bonus insight: dividend-day effect ----------

print("Avg return on dividend days:", df[df["Dividends"] > 0]["Return"].mean())
print("Avg return on normal days:", df[df["Dividends"] == 0]["Return"].mean())
