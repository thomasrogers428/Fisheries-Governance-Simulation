
from mesa import Agent

class ProtectedArea(Agent):
    def __init__(self, unique_id, pos, model):
        super().__init__(unique_id, model)
        self.x = pos[0]
        self.y = pos[1]

    def portrayal(self):
        return {"Shape": "rect",
                "w": 1,
                "h": 1,
                "Filled": "true",
                "Layer": 0,
                "Color": "rgba(0,255,0,0.5)"}
