import pandas as pd
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent.parent / "data.csv"

df = pd.read_csv(DATA_PATH)
lipsa_inainte = df["Position"].isna().sum()

df["Position"] = df["Position"].fillna("Unknown")

lipsa_dupa = df["Position"].isna().sum()
print(f"Valori lipsa inainte: {lipsa_inainte}")
print(f"Valori lipsa dupa: {lipsa_dupa}")
print("\nExemplu pozitii completate:")
print(df[df["Position"] == "Unknown"][["Name", "Position"]].head(10).to_string(index=False))
