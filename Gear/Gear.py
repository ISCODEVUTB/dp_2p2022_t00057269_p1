from abc import ABC


class Gear(ABC):
    armor: int
    AGI: int
    STA: int
    INT: int
    type: str

    def __init__(self, type: str) -> None:
        self.type = type

    def clone(self, type:str):
        ...

    def get_armor(self):
        return self.AGI
    
    def set_armor(self, armor: int):
        self.armor = armor
    
    def get_AGI(self):
        return self.AGI

    def set_AGI(self, agi: int):
        self.AGI = agi
    
    def get_STA(self):
        return self.STA
    
    def set_STA(self, sta: int):
        self.STA = sta
    
    def get_INT(self):
        return self.INT
    
    def set_INT(self, int: int):
        self.INT = int
    
    def get_type(self):
        return self.type

    def set_type(self, type: str):
        self.type = type
