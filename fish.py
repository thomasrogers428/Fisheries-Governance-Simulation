from mesa import Agent

import random
import math

class Fish(Agent):
    def __init__(self, unique_id, pos, model, born=True):
        super().__init__(unique_id, model)
        self.x = pos[0]
        self.y = pos[1]

        if born:
            self.age = 0
            self.size = 1
        else:
            self.age = self.init_age()
            self.size = self.calculate_size()
        
        self.reproduction = self.calculate_reproduction()

        self.caught = False

    def step(self):
        if self.caught:
            self.model.grid.remove_agent(self)
            self.model.schedule.remove(self)
            self.model.fish.remove(self)
        else:
            self.age += 1
            self.update_reproduction()
            self.move()

    def calculate_size(self):
        # Randomize the size of the fish based on its age with a gaussian distribution
        return random.lognormvariate(self.age, 1)
    
    def calculate_reproduction(self):
        reproducing = random.randint(0, 1)

        if not reproducing:
            return None
        elif self.age <= 1.5*12: 
            return 0
        else:
            return random.randint(1,7)
        
    def update_reproduction(self):
        if self.reproduction == 0:
            if self.age >= 1.5*12:
                self.reproduction = random.randint(1,7)
        
    def init_age(self):
        return random.randint(0, 7*12)
    
    def move(self):
        horizontal = random.randint(-1,1)
        vertical = random.randint(-1,1)

        self.x = max(0, min(self.x + horizontal, self.model.grid.width - 1))
        self.y = max(0, min(self.y + vertical, self.model.grid.height - 1))
    
    def portrayal(agent):
        portrayal = {"Shape": "circle",
                    "Filled": "true"}

        # Count the number of fish in the cell
        num_fish_in_cell = len([other_agent for other_agent in agent.model.grid.get_cell_list_contents([agent.pos]) if type(other_agent) is Fish])

        # Scale the size of the portrayal based on the number of fish
        portrayal["r"] = min(1, 0.1 * math.log(num_fish_in_cell + 1))

        portrayal["Color"] = "blue"
        portrayal["Layer"] = 2

        return portrayal
        