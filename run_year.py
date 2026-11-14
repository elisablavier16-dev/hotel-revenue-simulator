from datetime import date, timedelta
import pandas as pd
from hotel_model import simulate_night

NB_OF_ROOMS = 110
ROOM_RATE = 170
start_date = date(2026, 1, 1)

nights = []
for day_number in range(365):
    current_date = start_date + timedelta(days=day_number)
    night = simulate_night(current_date, ROOM_RATE, NB_OF_ROOMS)
    nights.append(night)

df = pd.DataFrame(nights)
print(df.head())
df.to_csv("hotel_data.csv", index=False)