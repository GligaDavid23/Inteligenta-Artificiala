import pandas as pd
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent.parent / "data.csv"

df = pd.read_csv(DATA_PATH)
df["SprintSpeed"] = pd.to_numeric(df["SprintSpeed"], errors="coerce")
df["Acceleration"] = pd.to_numeric(df["Acceleration"], errors="coerce")

rezultat = (
    df.groupby("Nationality")[["SprintSpeed", "Acceleration"]]
    .mean()
    .sort_values("SprintSpeed", ascending=False)
)

print(rezultat.to_string())
