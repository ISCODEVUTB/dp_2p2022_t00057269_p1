from Gear.Gear import Gear


class Gloves(Gear):

    def __init__(self, type: str) -> None:
        super().__init__(type)
    
    def clone(self, type):
        return Gloves(type)