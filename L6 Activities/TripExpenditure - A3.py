hotel_cost_per_day = int(input("Enter hotel cost per day: "))
days = int(input("Enter number of days: "))
plane_cost = int(input("Enter plane ticket cost: "))
vehicle_cost = int(input("Enter vehicle rental cost: "))

hotel_cost = hotel_cost_per_day * days

total_expense = hotel_cost + plane_cost + vehicle_cost

print("\nTrip Expenditure Report")
print("Hotel Cost =", hotel_cost)
print("Plane Cost =", plane_cost)
print("Vehicle Rental Cost =", vehicle_cost)
print("Total Trip Expenditure =", total_expense)