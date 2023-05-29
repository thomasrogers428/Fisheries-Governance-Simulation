from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import ChartModule

from model import Model, Fish, Fishery

# This function links the portrayal method to the agents
def agent_portrayal(agent):
    return agent.portrayal()

# Set up the grid
grid = CanvasGrid(agent_portrayal, 10, 10, 500, 500)  # assuming 10x10 grid and each cell is 500x500 pixels

# Set up the chart
chart_total_fish = ChartModule([{"Label": "Total Fish", "Color": "blue"}])
chart_total_fisheries = ChartModule([{"Label": "Total Fisheries", "Color": "green"}])

# Create the server
server = ModularServer(Model,
                       [grid, chart_total_fish, chart_total_fisheries],
                       "Fisheries Model",
                       {"width": 10, "height": 10, "num_fish": 100, "num_fisheries": 10, "num_ports": 5, "p_protected": 0.3, "size_limit": 8})

server.port = 8521  # Set the port for the visualization server
server.launch()
