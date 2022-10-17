from Gear.Gear import Gear


class Bottom(Gear):

    def __init__(self, type: str) -> None:
        super().__init__(type)
    
    def clone(self, type:str):
        return Gear(type)