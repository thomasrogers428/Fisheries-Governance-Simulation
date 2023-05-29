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

        self.capacity = 100
        self.profit = 0
        self.fish_caught = 0
        self.fish_bag = []
        
        self.can_fish = True

        self.illegal_dict = {}


    def step(self):
        for fish in self.model.fish:
            self.catch_fish(fish)

        self.calculate_profit()

        self.move()

    def catch_fish(self, fish):
        if (fish.x == self.x and fish.y == self.y) and not self.model.is_protected(self.x, self.y):
            catch_prob = random.random()

            # 50% chance of catching a fish
            if catch_prob > 0.1 and fish.size >= self.model.size_limit:
                self.fish_caught += 1
                self.fish_bag.append(fish)
                fish.caught = True
        
    def move(self):
        potential_locations = self.locate_fishing_spot()

        if potential_locations is not None:
            new_pos = self.choose_location(potential_locations)

            if new_pos is not None:
                self.x, self.y = new_pos
                self.model.grid.move_agent(self, (self.x, self.y))


    def locate_fishing_spot(self):
        fish_counts = {}

        for cell in self.model.grid.coord_iter():
            if not self.model.is_protected(cell[1], cell[2]):
                x, y = cell[1], cell[2]
                cell_content = cell[0]

                fish_in_cell = [obj for obj in cell_content if isinstance(obj, Fish) and not obj.caught and obj.size >= self.model.size_limit]

                if fish_in_cell:
                    fish_counts[(x, y)] = len(fish_in_cell)

        
        if not fish_counts:
            return None

        sorted_locations = sorted(fish_counts.items(), key=lambda item: item[1], reverse=True)

        top_locations = sorted_locations[:10]

        return top_locations
    
    def choose_location(self, locations):
        dest_x, dest_y = None, None
        curr_profit = -math.inf

        random.shuffle(locations)

        # for location in locations: 
        #     x, y = location[0][0], location[0][1]
        #     fish_count = location[1]

        #     profit = self.estimate_profit(x, y, fish_count)

        #     if profit >= curr_profit:
        #         dest_x, dest_y = x, y
        #         curr_profit = profit
        
        dest_x, dest_y = locations[0][0][0], locations[0][0][1]

        if dest_x is None or dest_y is None:
            return None

        return dest_x, dest_y


    def estimate_profit(self, x, y, fish_count):
        
        distance = (x - self.x)**2 + (y - self.y)**2

        profit = fish_count*10 - distance*30

        return profit
    
    def calculate_profit(self):

        for fish in self.fish_bag:
            self.profit += fish.size * 7.5

        self.fish_bag = []

    def init_illegal(self):
        illegal_activities = ["marine_protected", "size_limit", "fishing_gear"]

        for activity in illegal_activities:
            self.illegal_dict[activity] = random.random()

    def portrayal(self):
        return {"Shape": "rect", "w": .5, "h": .5,  "Filled": "false", "Color": "red", "Layer": 1}