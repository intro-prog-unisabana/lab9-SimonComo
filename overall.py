# TODO: Import modules
from car_utils import create_car_from_input, display_cars
from car import Car

cars = {}

while True:
    print("Choose an option:")
    print("1. Add a new car")
    print("2. View all cars")
    print("3. Drive a car")
    print("4. Paint a car")
    print("5. Quit")

    option = input()

    if option == "1":
        car = create_car_from_input()
        cars[car.car_id] = car
        print(car)
        print("Car added.")

    elif option == "2":
        display_cars(cars)

    elif option == "3":
        car_id = input()
        miles = float(input())

        if car_id in cars:
            cars[car_id].drive(miles)
            print("Mileage updated.")
            print(cars[car_id])

    elif option == "4":
        car_id = input()
        new_color = input()

        if car_id in cars:
            cars[car_id].change_color(new_color)
            print("Color updated.")
            print(cars[car_id])

    elif option == "5":
        print("Goodbye!")
        break