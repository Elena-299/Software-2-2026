class Car:
    def __init__(self, registration, max_speed, current_speed = 0, distance = 0):
        self.registration = registration
        self.max_speed = max_speed
        self.current_speed = current_speed
        self.distance = distance

    def accelerate(self, change_of_speed):
        cur_speed = self.current_speed
        new_speed = cur_speed
        if (cur_speed + change_of_speed) < 0:
            new_speed = 0
            print("You have stopped completely \nYour current speed is 0km/h\n")
        elif (cur_speed + change_of_speed) < self.max_speed:
            new_speed = cur_speed + change_of_speed
            print(f"You have accelerated {change_of_speed}km/h\nYour current speed is {new_speed}km/h\n")
        elif (cur_speed + change_of_speed) > self.max_speed:
            new_speed = self.max_speed
            print(f"You reached your maximum speed\nYou are going 142km/h\n")
        self.current_speed = new_speed
        return

    def drive(self, hours):
        cur_distance = self.distance
        print(f"Your current distance traveled is {cur_distance}")
        new_distance = cur_distance + (self.current_speed * hours)
        self.distance = new_distance
        print(f"Your updated distance traveled is {new_distance}")
        return

import random
racers = []
for i in range(10):
    registration = f"ABC-{i+1}"
    max_speed = random.randint(100,200)
    new_car = Car(registration, max_speed)

race_finished = False
while not race_finished:
    for car in racers:
        change_of_speed = random.randint(-10, 15)
        car.accelerate(change_of_speed)
        car.drive(1)
        if car.distance >= 1:
            race_finished = True
            break

print("\n--- Race Results ---")
print(f"{'Registration':<10} {'Max Speed':<10} {'Speed':<10} {'Distance':<15}")

for car in racers:
    print(f"{car.registration:<10} {car.max_speed:<10} {car.current_speed:<10} {car.distance:<15.2f}")

