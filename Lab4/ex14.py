import pandas as pd
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent.parent / "data.csv"

df = pd.read_csv(DATA_PATH)
for col in ["Overall", "Potential", "SprintSpeed", "Passing"]:
    df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)

df["Scor"] = (
    0.3 * df["Overall"]
    + 0.3 * df["Potential"]
    + 0.2 * df["SprintSpeed"]
    + 0.2 * df["Passing"]
)

print(df[["Name", "Overall", "Potential", "SprintSpeed", "Passing", "Scor"]]
      .sort_values("Scor", ascending=False)
      .head(20)
      .to_string(index=False))
