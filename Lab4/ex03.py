import pandas as pd
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent.parent / "data.csv"

df = pd.read_csv(DATA_PATH)
rezultat = df[(df["Overall"] >= 85) & (df["Age"] < 25)]
print(rezultat.to_string(index=False))
