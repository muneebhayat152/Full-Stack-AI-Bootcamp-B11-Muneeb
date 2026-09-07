# Final Assessment — Comprehensive Stock Price Research

**Course:** Full Stack AI – Batch 11
**Theme:** Comprehensive Stock Price Research Blueprint (Adobe, Microsoft, Oracle, Salesforce)

## Files

| File | Dataset | Marks |
|---|---|---|
| `Question1-Adobe.py` | Adobe (ADBE), 1986–2024 | Question 1 |
| `Question2-Microsoft.py` | Microsoft (MSFT), 1986–2024 (5 CSVs merged) | Question 2 |
| `Question3-Oracle.py` | Oracle (ORCL), 2019–2024 | Question 3 |
| `Question4-Salesforce.py` | Salesforce (CRM), 2004–2024 | Question 4 |

Each file follows the same research pipeline:

1. **Load** — read the raw CSV(s) into a Pandas DataFrame
2. **Descriptive Statistics** — shape, dtypes, missing values, `.describe()`
3. **Feature Engineering (NumPy + Pandas)** — log returns, moving averages (MA20/50/200), rolling volatility, momentum, volume ratio
4. **Seaborn EDA** — return distribution, correlation heatmap, price trend with moving averages
5. **Scikit-Learn Models** — Logistic Regression & Random Forest predicting next-day direction (up/down), validated with `TimeSeriesSplit` (not a random split, since price data is time-dependent) + feature importance ranking
6. **Clustering** — KMeans + PCA to detect market regimes (bull/bear/sideways-like groupings)
7. **Backtesting Metrics** — Sharpe Ratio, Maximum Drawdown, CAGR

Microsoft additionally merges its `history`, `dividends`, and `stock splits` files, and cross-validates that merge against the separate `action.csv` file (a genuine **Data Validation** step).

Each file also includes a **regression section** at the end: Linear Regression, Ridge, and Lasso predicting the actual next-day return (a continuous value), evaluated with R², RMSE, and MAE — alongside the classification section (Logistic Regression / Random Forest predicting up/down). Both angles are explicitly listed as valid target framings in the assessment brief ("Predictive Targets: Classification ... Regression ...").

Plots for all 4 stocks are saved in `output_plots/`.

## Results Summary

| Stock | Sharpe Ratio | Max Drawdown | CAGR | Logistic Regression Acc. | Random Forest Acc. |
|---|---|---|---|---|---|
| Adobe | 0.33 | -89.3% | 4.0% | 51.6% | 50.2% |
| Microsoft | 0.59 | -86.2% | 15.0% | 49.8% | 49.7% |
| Oracle | 0.75 | -43.3% | 20.7% | 47.0% | 49.7% |
| Salesforce | 0.56 | -74.4% | 15.6% | 51.2% | 51.0% |

## Regression Results (Linear / Ridge / Lasso predicting next-day return)

| Stock | Model | R² | RMSE | MAE |
|---|---|---|---|---|
| Adobe | Linear | -0.039 | 0.0277 | 0.0194 |
| Adobe | Ridge | -0.038 | 0.0277 | 0.0194 |
| Adobe | Lasso | -0.005 | 0.0274 | 0.0190 |
| Microsoft | Linear | -0.312 | 0.0218 | 0.0155 |
| Microsoft | Ridge | -0.293 | 0.0217 | 0.0154 |
| Microsoft | Lasso | -0.002 | 0.0192 | 0.0134 |
| Oracle | Linear | -0.206 | 0.0202 | 0.0140 |
| Oracle | Ridge | -0.205 | 0.0202 | 0.0140 |
| Oracle | Lasso | -0.114 | 0.0195 | 0.0133 |
| Salesforce | Linear | -0.018 | 0.0245 | 0.0170 |
| Salesforce | Ridge | -0.017 | 0.0245 | 0.0169 |
| Salesforce | Lasso | -0.0002 | 0.0243 | 0.0167 |

**Why R² is negative (this is expected, not a bug):** A negative R² means the model performs *worse* than simply predicting the average return every day. This is a well-documented, genuine finding in return-prediction research — daily stock returns are extremely close to random noise, so squeezing a linear signal out of basic technical features consistently fails to beat the naive mean baseline. **Lasso is consistently the least negative (best) of the three** in every single stock, because its L1 penalty shrinks weak/noisy coefficients toward zero — effectively learning "there is no real signal here" rather than overfitting to it. This is the same conclusion the classification models reached (47-52% accuracy, near coin-flip) approached from a different angle: short-horizon return prediction is fundamentally hard, which is exactly the research mindset this assessment asks for.

## Key Research Findings

- **Direction prediction is close to a coin flip.** Across all 4 stocks and both models, next-day up/down accuracy stayed in the 47–52% range. This matches the assessment's own framing that predicting tomorrow's price is the wrong question — markets are close to efficient in the short term, so research value comes from understanding risk/behavior (volatility, drawdowns, regimes) rather than chasing daily direction.
- **Ex-dividend price drop (Microsoft).** Average return on dividend-paying days was **-0.51%**, versus **+0.08%** on normal days — consistent with the well-known effect where a stock's price adjusts down by roughly the dividend amount on the payout date.
- **Crisis volatility (Salesforce).** Return volatility during the 2008 financial crisis (4.55%) was actually *higher* than during the 2020 COVID crash (3.28%), both well above Salesforce's all-time average (2.56%).
- **Oracle had the best risk-adjusted performance** in its (shorter, 2019–2024) window — highest Sharpe Ratio (0.75) and shallowest drawdown (-43.3%) of the four.
- **Data validation passed.** Microsoft's independently-provided `action.csv` matched our own merge of `dividends.csv` + `stock_splits.csv` exactly (total dividends $21.39, 9 split events both ways) — confirming the merge logic was correct before building any features on top of it.
- **Feature importance was fairly evenly spread** across engineered features (returns, moving averages, volatility, momentum, volume ratio) for all 4 stocks — no single feature dominated, which is itself a finding: no obvious "free lunch" signal exists in these basic technical features alone.

## How to Run

```bash
python "FinalAssessment/Question1-Adobe.py"
python "FinalAssessment/Question2-Microsoft.py"
python "FinalAssessment/Question3-Oracle.py"
python "FinalAssessment/Question4-Salesforce.py"
```

Each script prints its full analysis to the console and saves plots to `FinalAssessment/output_plots/`.
