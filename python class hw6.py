import csv
import urllib.request
from statistics import mean
import matplotlib.pyplot as plt
import pandas as pd

# load data
url = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/jhu/new_cases.csv"
urllib.request.urlretrieve(url, "covid_cases.csv")

df = pd.read_csv("covid_cases.csv")
df_1 = df[["date", "World"]]
# convert column date from object to datetime
df_1["date"] = pd.to_datetime(df_1["date"])
# set date as index
df_1 = df_1.set_index("date")
df_1["7day_avg"] = df_1["World"].rolling(window="7D",closed="right").mean()
df_1_shift3 = df_1.copy()
df_1_shift3["7day_avg_shift3d"]= df_1_shift3["7day_avg"].shift(-3)
df_1_shift3 = df_1_shift3.reset_index(names = "date")
df_final = df_1_shift3.iloc[3:-3].reset_index(drop = True)
df_final["flag_spike"] = (df_final["World"]>=2*df_final["7day_avg_shift3d"]).astype(int)
df_final["spike_ratio"] = df_final["World"]/df_final["7day_avg_shift3d"]
df_filtered = df_final[df_final["flag_spike"]==1]
df_filtered.plot.scatter(x="date", y='spike_ratio')

# Add labels and title for clarity
plt.xlabel("Date")
plt.ylabel("Spike Ratio")
plt.xticks(rotation=90)
plt.title("Scatter Plot of Spike Ratio vs. Index (flag_spike = 1)")
plt.grid(True) # Optional: Add a grid
plt.show()