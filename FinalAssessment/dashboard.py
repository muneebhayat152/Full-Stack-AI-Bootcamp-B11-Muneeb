import json
from pathlib import Path

import pandas as pd
import streamlit as st

BASE_DIR = Path(__file__).parent
PLOTS_DIR = BASE_DIR / "output_plots"

st.set_page_config(page_title="Stock Research Dashboard", layout="wide")

with open(BASE_DIR / "dashboard_data.json") as f:
    data = json.load(f)

st.title("Stock Price Research Dashboard")
st.caption("NumPy · Pandas · Seaborn · Scikit-Learn quantitative research — Adobe, Microsoft, Oracle, Salesforce")

stock = st.sidebar.selectbox("Select Stock", list(data.keys()))
d = data[stock]

st.sidebar.markdown("---")
st.sidebar.write(f"**Data range:** {d['date_start']} to {d['date_end']}")
st.sidebar.write(f"**Rows analyzed:** {d['rows']:,}")
st.sidebar.markdown("---")
st.sidebar.caption(
    "Methodology: log returns, rolling moving averages, volatility, momentum, "
    "volume ratio, RSI, MACD and Bollinger Band position — all engineered with "
    "NumPy/Pandas, validated with TimeSeriesSplit (not a random split, since "
    "price data is time-dependent)."
)

col1, col2, col3 = st.columns(3)
col1.metric("Sharpe Ratio", f"{d['sharpe']:.2f}")
col2.metric("Max Drawdown", f"{d['max_drawdown']:.1%}")
col3.metric("CAGR", f"{d['cagr']:.1%}")

st.subheader("Price Trend")
st.image(str(PLOTS_DIR / f"{stock}_trend.png"))

col4, col5 = st.columns(2)
with col4:
    st.subheader("Return Distribution")
    st.image(str(PLOTS_DIR / f"{stock}_returns.png"))
with col5:
    st.subheader("Correlation Heatmap")
    st.image(str(PLOTS_DIR / f"{stock}_corr.png"))

st.subheader("Market Regimes (KMeans + PCA)")
st.image(str(PLOTS_DIR / f"{stock}_regimes.png"))
st.caption(f"Cluster sizes: {d['regime_counts']}")

st.subheader("Classification — Predicting Next-Day Direction")
acc_df = pd.DataFrame(list(d["accuracy"].items()), columns=["Model", "Accuracy"]).set_index("Model")
st.bar_chart(acc_df)
st.info(
    "Accuracy sits close to 50% across all models. This is expected: daily stock "
    "direction is close to a coin flip because markets are near-efficient. The "
    "research value here is in the risk metrics and feature analysis above, not "
    "in beating this baseline."
)

st.subheader("Feature Importance (Random Forest)")
fi_df = pd.DataFrame(
    list(d["feature_importance"].items()), columns=["Feature", "Importance"]
).sort_values("Importance", ascending=False).set_index("Feature")
st.bar_chart(fi_df)

st.subheader("Regression — Predicting Next-Day Return")
reg_df = pd.DataFrame(d["regression"]).T
reg_df.columns = ["R²", "RMSE", "MAE"]
st.dataframe(reg_df.style.format("{:.4f}"))
st.caption(
    "Negative R² means the model underperforms a naive mean-return baseline — "
    "also expected, and consistent with the classification result above."
)
