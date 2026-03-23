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

test_car = Car("ABC-123", 142)
test_car.accelerate(30)
test_car.accelerate(70)
test_car.accelerate(50)
test_car.accelerate(-200)



