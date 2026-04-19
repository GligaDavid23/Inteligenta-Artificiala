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
afaceri = df[["Name", "Wage", "Value"]].copy()
afaceri["value_num"] = afaceri["Value"].apply(money_to_number)
afaceri["wage_num"] = afaceri["Wage"].apply(money_to_number)
afaceri["difference"] = afaceri["value_num"] - afaceri["wage_num"]

afaceri = afaceri.sort_values("difference", ascending=False)
print(afaceri[["Name", "Wage", "Value", "difference"]].to_string(index=False))
