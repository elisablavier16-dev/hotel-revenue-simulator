import random

from pandas.tseries.holiday import weekend_to_monday

REFERENCE_RATE = 170
ELASTICITY = 0.5

CHANNELS = {
    "Direct": {"share": 0.40, "commission": 0.00},
    "Booking.com": {"share": 0.35, "commission": 0.18},
    "Expedia": {"share": 0.25, "commission": 0.15},
}

SEASON_DEMAND = {
    1: (30, 45), 2: (30, 45), 3: (30, 45),   # calme
    4: (55, 75),                              # reprise
    5: (70, 95), 6: (75,97), 7: (90,100), 8: (95,100) , 9: (80, 92),# haute saison
    10: (78,88), 11: (40, 55), 12: (45, 65)                         ## fin de saison, calme fin d'annee
}

def calculate_kpis(rooms_sold, room_rate, nb_of_rooms):
    revenue = rooms_sold * room_rate
    occupancy = rooms_sold / nb_of_rooms* 100
    adr = revenue / rooms_sold if rooms_sold > 0 else 0
    revpar = revenue / nb_of_rooms
    return {"revenue": revenue, "occupancy": occupancy, "adr": adr, "revpar": revpar}

def simulate_night (date, room_rate, nb_of_rooms):
    base_demand = expected_demand(date)
    price_factor = (REFERENCE_RATE / room_rate) ** ELASTICITY
    base_demand = base_demand * price_factor
    noise = random.randint(-10, 10)
    rooms_sold = round (base_demand + noise)
    rooms_sold = max(0, min(rooms_sold, nb_of_rooms))
    kpis = calculate_kpis(rooms_sold, room_rate, nb_of_rooms)
    kpis["date"] = date
    kpis["rooms_sold"] = rooms_sold
    kpis["room_rate"] = room_rate
    return kpis

def get_dynamic_rate(date):
    expected_occupancy = expected_demand(date) / 110 * 100
    if expected_occupancy >= 85:
        return 230
    elif expected_occupancy >= 60:
        return 190
    elif expected_occupancy >= 40:
        return 160
    else:
        return 130

def split_by_channel(night):
    rows = []
    for channel_name, info in CHANNELS.items():
        rooms = round(night["rooms_sold"] * info["share"])
        revenue = rooms * night["room_rate"]        # rooms multiplié par le tarif de la nuit
        commission = commission = revenue * info["commission"]     # revenue multiplié par info["commission"]
        rows.append({
            "date": night["date"],
            "channel": channel_name,
            "rooms_sold": rooms,
            "room_rate": night["room_rate"],
            "revenue": revenue,
            "commission": commission,
            "net_revenue": revenue - commission,    # revenue moins commission
        })
    return rows

def expected_demand(date):
    weekday_demand, weekend_demand = SEASON_DEMAND[date.month]
    if date.weekday() >= 4:
        demand = weekend_demand
    else:
        demand = weekday_demand
    if date.month == 12 and date.day in (24, 25, 26):
        demand = 15       # Noël : presque vide
    if (date.month == 12 and date.day >= 29) or (date.month == 1 and date.day == 1):
        demand = 110        # Nouvel an : complet
    return demand

from datetime import date
print(get_dynamic_rate(date(2026, 1, 1)))    # Nouvel an
print(get_dynamic_rate(date(2026, 7, 18)))   # samedi d'été
print(get_dynamic_rate(date(2026, 1, 14)))   # mercredi d'hiver
print(get_dynamic_rate(date(2026, 12, 25)))  # Noël