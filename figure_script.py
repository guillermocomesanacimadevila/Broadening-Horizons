import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.io as pio

def read_file(location):
    with open(os.path.expanduser(location), "r") as file:
        return pd.read_csv(file, sep=",", header=None, names=["Search Query", "Year", "Count"], skiprows=1)

df = read_file("~/Desktop/PubMed_Timeline_Results_by_Year.csv")
print(df.head(), np.shape(df))
print(df.columns)

pubmed_df_cleaned = df.iloc[1:].copy()
pubmed_df_cleaned.columns = ["Year", "Count", "NaN"]
pubmed_df_cleaned = pubmed_df_cleaned[["Year", "Count"]]

pubmed_df_cleaned["Year"] = pd.to_numeric(pubmed_df_cleaned["Year"], errors="coerce")
pubmed_df_cleaned["Count"] = pd.to_numeric(pubmed_df_cleaned["Count"], errors="coerce")
print(type(df["Year"]), type(df["Count"]))

pubmed_df_cleaned = pubmed_df_cleaned.dropna()

plt.figure(figsize=(8, 6))
plt.bar(pubmed_df_cleaned["Year"], pubmed_df_cleaned["Count"], color="skyblue", edgecolor="black")

plt.title("PubMed Timeline Results by Year", fontsize=14, fontweight="bold", loc="center")
plt.xlabel("Year", fontsize=12)
plt.ylabel("Publication Count", fontsize=12)
plt.tight_layout()

plt.savefig("probiotic_freq.png", dpi=300)
plt.show()

# ====== Energy and water savings ====== #
df_2 = read_file("~/Desktop/Longest Common Subsequence/water_electriciy_purebiotic.csv")
# print(df_2.head())
# print(df_2.columns)

types = ["Without BioFresh", "With BioFresh"]
electricity = [96.71, 43.96]
water = [40.326, 18.33]
total = [137.036, 62.29]

bar_width = 0.1
x = np.array([0, 0.4])
print(x)

plt.figure(figsize=(8, 6))
plt.bar(x - bar_width, electricity, width=bar_width, label="Electricity", color="#A2D5AB", edgecolor="black")
plt.bar(x, water, width=bar_width, label="Water", color="#76C7C0", edgecolor="black")
plt.bar(x + bar_width, total, width=bar_width, label="Total", color="#52A675", edgecolor="black")

plt.title("Yearly Energy Savings", fontsize=14, fontweight="bold")
plt.xlabel("Type", fontsize=12)
plt.ylabel("Values (Pounds per Year)", fontsize=12)
plt.xticks(x, types, fontsize=10)
plt.legend(title="Category")
plt.tight_layout()

plt.savefig("energy_savings.png", dpi=300, transparent=True)
plt.show()

# ==== Plotly pie chart ==== #
labels = [
    "Shower",
    "Other (cold taps)",
    "Washing machine",
    "Bath",
    "Toilet",
    "Bathroom hot tap",
    "Other (Garden, Car, Dishwasher)",
    "Hand wash dishes"
]
values = [25, 22, 9, 8, 22, 7, 3, 4]

colors = ["#A3D6A9", "#8DB7A5", "#49A489", "#2C8A77", "#1F5C5E", "#2C8A77", "#49A489", "#8DB7A5"]

fig = go.Figure(
    data=[go.Pie(labels=labels, values=values, hole=0.3, marker=dict(colors=colors))]
)

pio.write_html(fig, "pie_chart.html")
fig.show()