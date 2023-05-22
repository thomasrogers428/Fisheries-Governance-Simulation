from mesa import Agent
from fish import Fish

import random
import math

class Fishery(Agent):
    def __init__(self, unique_id, port_pos, model):
        super().__init__(unique_id, model)
        self.model = model
        self.x = port_pos[0]
        self.y = port_pos[1]

        self.capacity = 1000
        self.profit = 0

        self.fish_caught = 0
        self.fish_bag = []
        
        self.can_fish = True

    def step(self):
        for fish in self.model.fish:
            self.catch_fish(fish)

        self.calculate_profit()

        self.move()

    def catch_fish(self, fish):
        if (fish.x == self.x and fish.y == self.y):
            catch_prob = random.random()

            # 20% chance of catching a fish
            if catch_prob > 0.8:
                self.fish_caught += 1
                self.fish_bag.append(fish)
                fish.get_caught()
        
    def move(self):
        potential_locations = self.locate_fishing_spot()

        self.x, self.y = self.choose_location(potential_locations)

    def locate_fishing_spot(self):
        fish_counts = {}

        for cell in self.model.grid.coord_iter():
            x, y = cell[1], cell[2]
            cell_content = cell[0]

            fish_in_cell = [obj for obj in cell_content if isinstance(obj, Fish) and not obj.caught]

            if fish_in_cell:
                fish_counts[(x, y)] = len(fish_in_cell)

        
        if not fish_counts:
            return None

        sorted_locations = sorted(fish_counts.items(), key=lambda item: item[1], reverse=True)

        top_locations = sorted_locations[:3]

        return top_locations
    
    def choose_location(self, locations):
        dest_x, dest_y = None, None
        curr_profit = -math.inf

        for location in locations: 
            x, y = location[0][0], location[0][1]
            fish_count = location[1]

            profit = self.estimate_profit(x, y, fish_count)

            if profit >= curr_profit:
                dest_x, dest_y = x, y
                curr_profit = profit
        
        return dest_x, dest_y


    def estimate_profit(self, x, y, fish_count):
        
        distance = (x - self.x)**2 + (y - self.y)**2

        profit = fish_count*10 - distance%30

        return profit
    
    def calculate_profit(self):

        for fish in self.fish_bag:
            self.profit += fish.size

        self.fish_bag = []

    def portrayal(self):
        return {"Shape": "rect", "w": 1, "h": 1,  "Filled": "true", "Color": "red", "Layer": 1}