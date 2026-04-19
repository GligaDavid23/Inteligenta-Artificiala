import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

DATA_PATH = Path(__file__).resolve().parent.parent / "data.csv"

df = pd.read_csv(DATA_PATH)
top5 = df["Nationality"].value_counts().head(5)

plt.figure(figsize=(8, 8))
plt.pie(top5.values, labels=top5.index, autopct="%1.1f%%", startangle=90)
plt.title("Proportia jucatorilor pe nationalitati (Top 5)")
plt.tight_layout()
plt.show()
