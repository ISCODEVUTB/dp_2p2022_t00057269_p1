from Gear.Gear import Gear


class Shoulders(Gear):

    def __init__(self, type: str) -> None:
        super().__init__(type)
    
    def clone(self, type:str):
        return Shoulders(type)