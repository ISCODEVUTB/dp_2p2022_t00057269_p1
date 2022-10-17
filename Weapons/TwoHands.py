from turtle import clone
from Weapons.Weapons import Weapons


class TwoHands(Weapons):
    
    def clone(self):
        cloned_TwoHands = TwoHands()
        return cloned_TwoHands