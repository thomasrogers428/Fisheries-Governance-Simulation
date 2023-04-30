from fishery import Fishery

class FishingQuota():
    def __init__(self, fish_caught_quota):
        self.fish_caught_quota = fish_caught_quota
    
    def apply(self, model):
        for fishery in model.schedule.agents_by_type[Fishery]:
            if fishery.fish_caught >= self.fish_caught_quota:
                fishery.can_fish = False
            else:
                fishery.can_fish = True
