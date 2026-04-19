import pandas as pd
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent.parent / "data.csv"

df = pd.read_csv(DATA_PATH)
top5 = df["Nationality"].value_counts().head(5)

print("Cea mai frecventa nationalitate:")
print(top5.index[0])
print("\nTop 5 nationalitati:")
print(top5.to_string())
