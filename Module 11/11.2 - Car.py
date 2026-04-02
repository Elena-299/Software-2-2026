class Car:
    def __init__(self, registration, max_speed, current_speed=0, distance=0):
        self.registration = registration
        self.max_speed = max_speed
        self.current_speed = current_speed
        self.distance = distance

    def accelerate(self, change_of_speed):
        cur_speed = self.current_speed

        if (cur_speed + change_of_speed) < 0:
            self.current_speed = 0
            print("You have stopped completely \nYour current speed is 0km/h\n")

        elif (cur_speed + change_of_speed) < self.max_speed:
            self.current_speed = cur_speed + change_of_speed
            print(f"You have accelerated {change_of_speed}km/h\nYour current speed is {self.current_speed}km/h\n")

        else:
            self.current_speed = self.max_speed
            print(f"You reached your maximum speed\nYou are going {self.max_speed}km/h\n")

    def drive(self, hours):
        cur_distance = self.distance
        print(f"Your current distance traveled is {cur_distance}")
        new_distance = cur_distance + (self.current_speed * hours)
        self.distance = new_distance
        print(f"Your updated distance traveled is {new_distance}")


class ElectricCar(Car):
    def __init__(self, registration, max_speed, battery_capacity):
        super().__init__(registration, max_speed)
        self.battery_capacity = battery_capacity


class GasolineCar(Car):
    def __init__(self, registration, max_speed, tank_volume):
        super().__init__(registration, max_speed)
        self.tank_volume = tank_volume


electric_car = ElectricCar("ABC-15", 180, 52.5)
electric_car.accelerate(110)
electric_car.drive(3)
print(f"Electric car {electric_car.registration} has travelled {electric_car.distance} km.")

gasoline_car = GasolineCar("ACD-123", 165, 32.3)
gasoline_car.accelerate(100)
gasoline_car.drive(3)
print(f"Gasoline car {gasoline_car.registration} has travelled {gasoline_car.distance} km.")