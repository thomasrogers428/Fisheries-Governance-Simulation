from mesa import Agent

import random

class Fish(Agent):
    def __init__(self, unique_id, pos, model):
        super().__init__(unique_id, model)
        self.x = pos[0]
        self.y = pos[1]

        self.age = self.init_age()
        self.size = self.calculate_size()
        self.fertility = self.calculate_fertility()

        self.caught = False

    def step(self):
        # Code to move the fish to a new location
        pass

    def get_caught(self):
        # Code to handle the fish getting caught by a fisherman
        self.caught = True

    def calculate_size(self):
        # Randomize the size of the fish based on its age with a gaussian distribution
        return random.gauss(self.age, 1)
    
    def calculate_fertility(self):
        # Code to calculate the fertility of the fish based on its age
        fertile = random.randint(0, 1) and self.age >= 18

        if fertile:
            return random.randint(1, 5)
        else: 
            return 0
        
    def init_age(self):
        # Code to initialize the age of the fish
        return random.randint(0, 7*12)
        