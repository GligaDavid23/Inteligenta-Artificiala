import pandas as pd
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent.parent / "data.csv"

df = pd.read_csv(DATA_PATH)
df["Overall"] = pd.to_numeric(df["Overall"], errors="coerce")

medii = df.groupby("Club")["Overall"].mean().sort_values(ascending=False)
print("Clubul cu cea mai mare medie de Overall:")
print(medii.head(1).to_string())
