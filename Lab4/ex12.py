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

numar = int((df["Value_num"] > df["Wage_num"]).sum())
print(f"Jucatori cu Value > Wage: {numar}")
