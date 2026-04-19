import pandas as pd
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent.parent / "data.csv"

df = pd.read_csv(DATA_PATH)
df["Skill Moves"] = pd.to_numeric(df["Skill Moves"], errors="coerce")
rezultat = df.sort_values("Skill Moves", ascending=False)
print(rezultat[["Name", "Skill Moves", "Overall", "Age"]].to_string(index=False))
