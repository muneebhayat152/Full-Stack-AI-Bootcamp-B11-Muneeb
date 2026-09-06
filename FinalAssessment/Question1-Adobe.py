import pandas as pd

df = pd.read_csv(
    "FinalAssessment/Adobe(ADBE)Stock/Adobe (ADBE) From 1986 To Dec-2024.csv",
    parse_dates=["Date"], index_col="Date"
).sort_index()

print(df.shape)
print(df.dtypes)
print(df.head())
print(df.isnull().sum())
print(df[["Open", "High", "Low", "Close", "Volume"]].describe())