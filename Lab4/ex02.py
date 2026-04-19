import pandas as pd
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent.parent / "data.csv"

df = pd.read_csv(DATA_PATH)
rezultat = df[df["Age"] > 40].head(10)
print(rezultat.to_string(index=False))
