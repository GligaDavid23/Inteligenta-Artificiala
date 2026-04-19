import numpy as np
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

DATA_PATH = Path(__file__).resolve().parent.parent / "data.csv"


def money_to_number(x):
    if pd.isna(x):
        return np.nan
    s = str(x).replace("€", "").replace(",", "").strip()
    if s.endswith("M"):
        return float(s[:-1]) * 1_000_000
    if s.endswith("K"):
        return float(s[:-1]) * 1_000
    try:
        return float(s)
    except ValueError:
        return np.nan


df = pd.read_csv(DATA_PATH)
df["Value_num"] = df["Value"].apply(money_to_number)
df["Wage_num"] = df["Wage"].apply(money_to_number)
df["Overall"] = pd.to_numeric(df["Overall"], errors="coerce")

plot_df = df[["Name", "Wage_num", "Value_num", "Overall"]].dropna().reset_index(drop=True)

x = (plot_df["Wage_num"] / 1_000_000).to_numpy()
y = (plot_df["Value_num"] / 1_000_000).to_numpy()
names = plot_df["Name"].to_numpy()
overalls = plot_df["Overall"].to_numpy()

fig, ax = plt.subplots(figsize=(10, 6))
sc = ax.scatter(x, y, c=overalls, cmap="viridis", alpha=0.7, s=25, picker=True)
plt.colorbar(sc, label="Overall")
ax.set_xlabel("Wage (milioane EUR)")
ax.set_ylabel("Value (milioane EUR)")
ax.set_title("Hover pe punct pentru a vedea jucatorul")

annot = ax.annotate(
    "",
    xy=(0, 0),
    xytext=(12, 12),
    textcoords="offset points",
    bbox=dict(boxstyle="round", fc="white", alpha=0.9),
    arrowprops=dict(arrowstyle="->"),
)
annot.set_visible(False)


def update_annot(ind):
    i = ind["ind"][0]
    annot.xy = (x[i], y[i])
    annot.set_text(
        f"{names[i]}\nWage: {x[i]:.2f}M\nValue: {y[i]:.2f}M\nOverall: {overalls[i]:.0f}"
    )


def hover(event):
    visible = annot.get_visible()
    if event.inaxes == ax:
        contains, ind = sc.contains(event)
        if contains:
            update_annot(ind)
            annot.set_visible(True)
            fig.canvas.draw_idle()
        elif visible:
            annot.set_visible(False)
            fig.canvas.draw_idle()


fig.canvas.mpl_connect("motion_notify_event", hover)
plt.tight_layout()
plt.show()
