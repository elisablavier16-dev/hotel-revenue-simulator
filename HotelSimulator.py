
# Hotel settings
hotel_name = "Lizzy Hotel Amsterdam"
nb_of_rooms = 110
initial_room_rate= 170.0
room_rate = initial_room_rate

# Menu

choice = input (" Choose simulation mode (reporting / simulation)").lower()
if choice == "reporting":
    while True:
       try:
        rooms_sold = int(input( "How many rooms were sold tonight ?"))

        if rooms_sold > nb_of_rooms or rooms_sold < 0:
            print("Invalid number, enter a value between 0 and 110.")
        else:
            break

       except ValueError:
            print ("Please enter a number")
        
elif choice == "simulation":
    while True:
         demand_level = input(" Choose demand level (Low / Medium / High): ").lower()
         if demand_level == "low":
             rooms_sold = 40
             room_rate = 140
             break
         elif demand_level == "medium":
             rooms_sold = 50
             room_rate = 170
             break
         elif demand_level == "high":
             rooms_sold = 100
             room_rate = 200
             break
         else:
             print ("Invalid demand level")
else:
    print("Invalid mode. Please choose reporting or simulation.")
    raise SystemExit


# Calculation
actual_nightly_revenue = rooms_sold * room_rate
occupancy_rate = rooms_sold / nb_of_rooms*100
if occupancy_rate < 50:
    print ("The occupancy rate is low")
elif 50 <= occupancy_rate <= 80:
    print ("The occupancy rate is moderate")
elif occupancy_rate > 80:
    print ("The occupancy rate is high")

if occupancy_rate < 50:
   recommendation = "Examine promotions"
elif 50 <= occupancy_rate <= 80:
    recommendation = "Distribution channels"
else:
    recommendation = "consider increasing rate"

maximum_nightly_revenue = nb_of_rooms * room_rate
adr = actual_nightly_revenue / rooms_sold
RevPar = actual_nightly_revenue / nb_of_rooms
rooms_available = nb_of_rooms - rooms_sold
potential_extra_revenue = rooms_available * room_rate
revenue_gap = maximum_nightly_revenue - actual_nightly_revenue

# Results
print (f"{hotel_name} has {nb_of_rooms} rooms. The initial room rate is {room_rate:.2f}€")
print (f"The maximum nightly revenue is {maximum_nightly_revenue:.2f}€")
print (f"The occupancy rate is {occupancy_rate:.2f}%")
print (f"The actual nightly revenue is {actual_nightly_revenue:.2f}€")
print (f"The ADR is {adr:.2f}€")
print (f"The RevPar is {RevPar:.2f}€")
print (f"The rooms available is {rooms_available}")
print (f"The potential extra revenue is {potential_extra_revenue:.2f}€")
print (f"The revenue gap is {revenue_gap:.2f}€")
print(recommendation)

