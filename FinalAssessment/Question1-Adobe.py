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

# ---------- 1. Load ----------

df = pd.read_csv(
    "FinalAssessment/Adobe(ADBE)Stock/Adobe (ADBE) From 1986 To Dec-2024.csv",
    index_col="Date"
)
df.index = pd.to_datetime(df.index, utc=True)
df = df.sort_index()

# ---------- 2. Descriptive statistics ----------

print("=== Descriptive Statistics ===")
print(df.shape)
print(df.dtypes)
print(df.head())
print(df.isnull().sum())
print(df[["Open", "High", "Low", "Close", "Volume"]].describe())

# ---------- 3. Feature engineering ----------

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

# ---------- 4. Seaborn EDA ----------

os.makedirs("FinalAssessment/output_plots", exist_ok=True)

sns.histplot(df["Return"], kde=True)
plt.title("Adobe - Return Distribution")
plt.savefig("FinalAssessment/output_plots/Adobe_returns.png")
plt.close()

cols = ["Return", "Volume_Ratio", "Vol20", "Mom10"]
sns.heatmap(df[cols].corr(), annot=True, cmap="coolwarm")
plt.title("Adobe - Correlation Heatmap")
plt.savefig("FinalAssessment/output_plots/Adobe_corr.png")
plt.close()

plt.figure(figsize=(10, 5))
plt.plot(df.index, df["Close"], label="Close")
plt.plot(df.index, df["MA50"], label="MA50")
plt.plot(df.index, df["MA200"], label="MA200")
plt.legend()
plt.title("Adobe - Price Trend")
plt.savefig("FinalAssessment/output_plots/Adobe_trend.png")
plt.close()

print("Plots saved")

# ---------- 5. Scikit-Learn models ----------

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

# ---------- 6. Clustering (KMeans + PCA) ----------

X_scaled = StandardScaler().fit_transform(X)
X_pca = PCA(n_components=2).fit_transform(X_scaled)
df["Regime"] = KMeans(n_clusters=3, random_state=42, n_init=10).fit_predict(X_pca)

plt.figure(figsize=(8, 5))
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=df["Regime"], cmap="viridis", s=8)
plt.title("Adobe - Market Regimes (KMeans + PCA)")
plt.savefig("FinalAssessment/output_plots/Adobe_regimes.png")
plt.close()

print(df["Regime"].value_counts())

# ---------- 7. Backtesting metrics ----------

returns = df["Return"]
sharpe = (returns.mean() / returns.std()) * np.sqrt(252)
cum_return = (1 + returns).cumprod()
drawdown = (cum_return - cum_return.cummax()) / cum_return.cummax()
years = (df.index[-1] - df.index[0]).days / 365.25
cagr = cum_return.iloc[-1] ** (1 / years) - 1

print("\nSharpe Ratio:", sharpe)
print("Max Drawdown:", drawdown.min())
print("CAGR:", cagr)
