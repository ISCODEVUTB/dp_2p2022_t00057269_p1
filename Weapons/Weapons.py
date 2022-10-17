from abc import ABC


class Weapons(ABC):
    DAMAGE = int
    AGI: float
    INT: float
    STA: float
    CRIT = None
    VERSA = None
    CEL = None
    MAESTRY = None

    def clone(self):
        ...

    def set_DAMAGE(self, dmg: int):
        self.DAMAGE = dmg

    def set_AGI(self, agi: float):
        self.AGI = agi
    
    def set_INT(self, int: float):
        self.INT = int
    
    def set_STA(self, sta: float):
        self.STA = sta
    
    def set_CRIT(self, crit: float):
        self.CRIT = crit
    
    def set_VERSA(self,versa: float):
        self.VERSA = versa
    
    def set_CEL(self, cel: float):
        self.CEL = cel
    
    def set_MAESTRY(self, maestry: float):
        self.MAESTRY = maestry
    
    def getName(self):
        return self.__class__.__name__

