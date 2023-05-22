from mesa import Model
from mesa.space import MultiGrid
from mesa.time import RandomActivation
from mesa.datacollection import DataCollector

from fish import Fish
from fishery import Fishery

import random

class Model(Model):
    def __init__(self, width, height, num_fish, num_fisheries, num_ports):
        super().__init__()

        self.num_fish= num_fish
        self.num_fisheries = num_fisheries
        self.num_ports = num_ports

        self.fish_born = 0

        self.grid = MultiGrid(width, height, torus=True)
        self.schedule = RandomActivation(self)
        self.fish = []
        self.fisheries = []
        self.ports = []

        self.datacollector = DataCollector(
            model_reporters={"TotalFish": self.compute_total_fish,
                             "TotalFisheries": self.compute_total_fisheries}
        )

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
        for i in range(self.num_fisheries):
            
            port_pos = random.choice(self.ports)

            fishery = Fishery(i + num_fish, port_pos, self)

            self.schedule.add(fishery)
            self.grid.place_agent(fishery, (port_pos[0], port_pos[1]))
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

                self.fish_born += 1

                baby_fish = Fish(self.num_fish + self.num_fisheries + self.fish_born, (x,y), self)

                self.schedule.add(baby_fish)
                self.grid.place_agent(baby_fish, (x,y))
                self.fish.append(baby_fish)

    def handle_deaths(self):
        for fish in self.fish:
            if fish.age >= 12*7:
                self.schedule.remove(fish)
                self.grid.remove_agent(fish)
                self.fish.remove(fish)

    def compute_total_fish(model):
        return len(model.fish)

    def compute_total_fisheries(model):
        return len(model.fisheries)




                