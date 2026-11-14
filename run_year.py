from calendar import weekday

from datetime import date, timedelta
import pandas as pd
from hotel_model import simulate_night, get_dynamic_rate
import random
random.seed(42)

NB_OF_ROOMS = 110
ROOM_RATE = 170
start_date = date(2026, 1, 1)

nights = []
for day_number in range(365):
    current_date = start_date + timedelta(days=day_number)
    dynamic_rate = get_dynamic_rate(current_date)
    night = simulate_night(current_date, ROOM_RATE, NB_OF_ROOMS)
    nights.append(night)

df = pd.DataFrame(nights)
print("Total revenue:", df["revenue"].sum())
print("Average RevPAR:", df["revpar"].mean())
print(df.head())
df.to_csv("hotel_data.csv", index=False)

