import pandas as pd
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent.parent / "data.csv"

df = pd.read_csv(DATA_PATH)
randuri, coloane = df.shape
jucatori_unici = df["Name"].nunique()

print(f"Numar randuri: {randuri}")
print(f"Numar coloane: {coloane}")
print(f"Numar jucatori unici (dupa Name): {jucatori_unici}")
