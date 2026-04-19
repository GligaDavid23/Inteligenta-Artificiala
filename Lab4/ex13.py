import numpy as np
from pathlib import Path
import pandas as pd

DATA_PATH = Path(__file__).resolve().parent.parent / "data.csv"


def money_to_number(x):
    if pd.isna(x):
        return np.nan
    s = str(x).replace("€", "").replace(",", "").strip()
    if s.endswith("M"):
        return float(s[:-1]) * 1_000_000
    if s.endswith("K"):
        return float(s[:-1]) * 1_000
    try:
        return float(s)
    except ValueError:
        return np.nan


df = pd.read_csv(DATA_PATH)
df["Value_num"] = df["Value"].apply(money_to_number)
df["Wage_num"] = df["Wage"].apply(money_to_number)

df["is_underpaid"] = df["Wage_num"] < (df["Value_num"] / 100)

print(df[["Name", "Wage", "Value", "is_underpaid"]].head(20).to_string(index=False))
print(f"\nTotal underpaid: {int(df['is_underpaid'].sum())}")
