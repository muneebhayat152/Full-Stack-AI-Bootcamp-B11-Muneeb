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

Plots for all 4 stocks are saved in `output_plots/`.

## Results Summary

| Stock | Sharpe Ratio | Max Drawdown | CAGR | Logistic Regression Acc. | Random Forest Acc. |
|---|---|---|---|---|---|
| Adobe | 0.33 | -89.3% | 4.0% | 51.6% | 50.2% |
| Microsoft | 0.59 | -86.2% | 15.0% | 49.8% | 49.7% |
| Oracle | 0.75 | -43.3% | 20.7% | 47.0% | 49.7% |
| Salesforce | 0.56 | -74.4% | 15.6% | 51.2% | 51.0% |

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
