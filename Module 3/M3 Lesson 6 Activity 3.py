def hotel_cost(nights):
    return 150 * nights

def plane_ride_cost(city):
    if "London" == city:
        return 120
    elif "Manchester" == city:
        return 180
    elif "Liverpool" == city:
        return 165
    elif "Birmingham" == city:
        return 150
    else:
        return 0

def rental_car_cost(days):
    if days >= 7:
        return 50 * days - 40
    elif days >= 3:
        return 50 * days - 15
    else:
        return 50 * days
        
def trip_cost(city, days, spending_money):
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money
	
print("Cost of car rental (5 days):", rental_car_cost(5))

print("Cost of plane ride (London):", plane_ride_cost("London"))

print("Cost of hotel room (4 nights):", hotel_cost(4))

print("Total cost to London (4 days, 300 spending):", trip_cost("London", 4, 300))

print("Total cost to Manchester (7 days, 1000 spending):", trip_cost("Manchester", 7, 1000))