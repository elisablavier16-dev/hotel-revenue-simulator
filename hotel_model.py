import random
def calculate_kpis(rooms_sold, room_rate, nb_of_rooms):
    revenue = rooms_sold * room_rate
    occupancy = rooms_sold / nb_of_rooms* 100
    adr = revenue / rooms_sold if rooms_sold > 0 else 0
    revpar = revenue / nb_of_rooms
    return {"revenue": revenue, "occupancy": occupancy, "adr": adr, "revpar": revpar}

def simulate_night (date, room_rate, nb_of_rooms):
    base_demand = 55             # chambres vendues en semaine
    if date.weekday() >= 4:        # vendredi, samedi, dimanche
        base_demand = 80          # plus élevé le week-end
    noise = random.randint(-10, 10)
    rooms_sold = base_demand + noise
    rooms_sold = max(0, min(rooms_sold, nb_of_rooms))
    kpis = calculate_kpis(rooms_sold, room_rate, nb_of_rooms)
    kpis["date"] = date
    kpis["rooms_sold"] = rooms_sold
    kpis["room_rate"] = room_rate
    return kpis