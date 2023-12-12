max_number_of_cars = int(input())
cars_dict = {}

for i in range(max_number_of_cars):
    car, mileage, fuel = input().split("|")
    cars_dict[car] = [int(mileage), int(fuel)]

while True:
    command = input().split(" : ")
    if command[0] == "Stop":
        break
    car = command[1]
    if command[0] == "Drive":
        distance, fuel = int(command[2]), int(command[3])
        if int(cars_dict[car][1]) >= fuel:
            cars_dict[car][0] += distance
            cars_dict[car][1] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            if cars_dict[car][0] >= 100000:
                del cars_dict[car]
                print(f"Time to sell the {car}!")
        else:
            print("Not enough fuel to make that ride")
    elif command[0] == "Refuel":
        fuel_given = int(command[2])
        cars_fuel = cars_dict[car][1]
        if (fuel_given + cars_fuel) > 75:
            cars_dict[car][1] = 75
            fuel_given = 75 - cars_fuel
        else:
            cars_dict[car][1] += fuel_given
        print(f"{car} refueled with {fuel_given} liters")
    elif command[0] == "Revert":
        kilometers = int(command[2])
        if (cars_dict[car][0] - kilometers) < 10000:
            cars_dict[car][0] = 10000
        else:
            cars_dict[car][0] -= kilometers
            print(f"{car} mileage decreased by {kilometers} kilometers")

for current_car in cars_dict.keys():
    mileage = cars_dict[current_car][0]
    fuel = cars_dict[current_car][1]
    print(f"{current_car} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt.")