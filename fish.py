from mesa import Agent

import random

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
        self.update_reproduction()

        self.move()

    def get_caught(self):
        self.caught = True

    def calculate_size(self):
        # Randomize the size of the fish based on its age with a gaussian distribution
        return random.gauss(self.age, 1)
    
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
        horizontal = random.randint(0,1)
        vertical = random.randint(-1,1)

        self.x += horizontal
        self.y += vertical
    
        