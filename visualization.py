from mesa.visualization.modules import ContinuousModule
from mesa.visualization.ModularVisualization import ModularServer

from model import Model

def fish_portrayal(agent):
    # Define how to portray your agents in the visualization
    pass

grid = ContinuousModule(fish_portrayal, 10, 10, 500, 500)
server = ModularServer(Model, [grid], "Model")