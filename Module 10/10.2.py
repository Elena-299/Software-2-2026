class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current = bottom
        return

    def go_to_floor(self, num):
        if (num >= self.bottom) and (num <= self.top):
            if num > self.current:
                self.floor_up(num)
            elif num < self.current:
                self.floor_down(num)
        else:
            print("No floor found")
        return

    def floor_up(self, num):
        floors = num - self.current
        for i in range(floors):
            if self.current + 1 >= self.top:
                self.current = self.top
                print(f"You are at floor {self.top}, aka the top floor")
                break
            else:
                self.current = self.current + 1
                print(f"You have moved up to the {self.current} floor")
        return

    def floor_down(self, num):
        floors = self.current - num
        for i in range(floors):
            if self.current - 1 <= 0:
                self.current = self.bottom
                print(f"You are at floor {self.bottom}, aka the bottom floor")
                break
            else:
                self.current = self.current - 1
                print(f"You have moved down to the {self.current} floor")
        return

class Building






