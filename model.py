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

        for i in range(self.num_ports):
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)

            port = (x,y)

            self.ports.append(port)
        
        # Create fish agents
        for i in range(self.num_fish):
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)

            fish = Fish(i, (x,y), self)

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
        
        # Update state of fish agents
        for fish in self.fish:
            fish.step()
            
        # Update state of fishery agents
        for fishery in self.fisheries:
            fishery.step()