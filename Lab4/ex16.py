import numpy as np
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

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
df["Overall"] = pd.to_numeric(df["Overall"], errors="coerce")

plot_df = df[["Wage_num", "Value_num", "Overall"]].dropna()

x = plot_df["Wage_num"] / 1_000_000
y = plot_df["Value_num"] / 1_000_000

plt.figure(figsize=(10, 6))
sc = plt.scatter(x, y, c=plot_df["Overall"], cmap="viridis", alpha=0.7, s=25)
plt.colorbar(sc, label="Overall")
plt.xlabel("Wage (milioane EUR)")
plt.ylabel("Value (milioane EUR)")
plt.title("Relatia dintre Wage si Value")
plt.tight_layout()
plt.show()
