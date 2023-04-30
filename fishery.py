from mesa import Agent

class Fishery(Agent):
    def __init__(self, unique_id, port_pos, model):
        super().__init__(unique_id, model)
        self.x = port_pos[0]
        self.y = port_pos[1]
        self.caught_fish = 0
        self.capacity = 1000
        self.can_fish = True

    def step(self):
        # Code to move the fisherman to a new location
        pass

    def catch_fish(self, fish):
        if (fish.x - self.x)**2 + (fish.y - self.y)**2 < 25:
            self.caught_fish += 1
            fish.get_caught()
        