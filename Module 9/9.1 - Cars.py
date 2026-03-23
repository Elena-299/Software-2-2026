class Car:
    def __init__(self, registration, max_speed, current_speed = 0, distance = 0):
        self.registration = registration
        self.max_speed = max_speed
        self.current_speed = current_speed
        self.distance = distance

new_car = Car("ABC-123", 142)
print(f"The registration of the car is {new_car.registration}")
print(f"The maximum speed it can reach is {new_car.max_speed}km/h")
print(f"Its current speed is {new_car.current_speed}")
print(f"The distance it has traveled is {new_car.distance}km")

