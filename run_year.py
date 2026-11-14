from calendar import weekday

from datetime import date, timedelta
import pandas as pd
from hotel_model import simulate_night, get_dynamic_rate, split_by_channel
import random
random.seed(42)


NB_OF_ROOMS = 110
ROOM_RATE = 170
start_date = date(2026, 1, 1)

nights = []
channel_rows = []
for day_number in range(365):
    current_date = start_date + timedelta(days=day_number)
    dynamic_rate = get_dynamic_rate(current_date)
    night = simulate_night(current_date, dynamic_rate, NB_OF_ROOMS)
    nights.append(night)
    channel_rows.extend(split_by_channel(night))
df = pd.DataFrame(nights)
print("Total revenue:", df["revenue"].sum())
print("Average RevPAR:", df["revpar"].mean())
print(df.head())
df.to_csv("hotel_data.csv", index=False)

df_channels = pd.DataFrame(channel_rows)
df_channels.to_csv("hotel_channels.csv", index=False)
print(len(df_channels))
print(df_channels.groupby("channel")["net_revenue"].sum())

print(df.groupby(df["date"].astype(str).str[:7])["occupancy"].mean())
import os
print(os.path.abspath("hotel_data.csv"))
print(df[df["date"].astype(str).str.startswith("2026-06")].head())