class car:
    def __init__(self, rides, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rides = rides
        self.fast = 128
class house:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.costs = "7"
class Houseonwheels(house, car):
    def print_info(self):
        print(self.rides)
        print(self.fast)
        print(self.costs)
house = Houseonwheels(rides ="Last")






