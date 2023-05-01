from mesa import Model
from mesa.space import MultiGrid
from mesa.time import RandomActivation

from fish import Fish
from fishery import Fishery

import random

class Model(Model):
    def __init__(self, width, height, num_fish, num_fisheries, num_ports):
        # Initialize your model here
        super().__init__()

        self.num_fish= num_fish
        self.num_fisheries = num_fisheries
        self.num_ports = num_ports
        self.grid = MultiGrid(width, height, torus=True)
        self.schedule = RandomActivation(self)
        self.fish = []
        self.fisheries = []
        self.ports = []

        self.step_count = 0

        for i in range(self.num_ports):
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)

            port = (x,y)

            self.ports.append(port)
        
        # Create fish agents
        for i in range(self.num_fish):
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)

            fish = Fish(i, (x,y), self, born=False)

            self.schedule.add(fish)
            self.grid.place_agent(fish, (x,y))
            self.fish.append(fish)
        
        # Create fisherman agents
        for i in range(self.num_agents):
            port_pos = random.choice(self.ports)

            fishery = Fishery(i, port_pos, self)

            self.schedule.add(fishery)
            self.grid.place_agent(fishery, (x,y))
            self.fisheries.append(fishery)
    
    def step(self):
        self.schedule.step()

        self.handle_deaths()
        if self.step_count % 12 == 0:
            self.handle_births()
        
        # Update state of fish agents
        for fish in self.fish:
            fish.step()
            
        # Update state of fishery agents
        for fishery in self.fisheries:
            fishery.step()

    def handle_births(self):
        for fish in self.fish:
            if fish.reproduction:
                x = fish.x
                y = fish.y

                baby_fish = Fish(self.num_fish, (x,y), self)

                self.schedule.add(baby_fish)
                self.grid.place_agent(baby_fish, (x,y))
                self.fish.append(baby_fish)

                self.num_fish += 1

    def handle_deaths(self):
        for fish in self.fish:
            if fish.age >= 12*7:
                self.schedule.remove(fish)
                self.grid.remove_agent(fish)
                self.fish.remove(fish)




                