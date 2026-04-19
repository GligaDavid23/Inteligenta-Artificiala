import pandas as pd
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent.parent / "data.csv"

df = pd.read_csv(DATA_PATH)
ani_contract = pd.to_numeric(
    df["Contract Valid Until"].astype(str).str.extract(r"(\d{4})")[0],
    errors="coerce",
)
rezultat = df[ani_contract <= 2021]
print(rezultat[["Name", "Contract Valid Until", "Club"]].to_string(index=False))
