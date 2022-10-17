from Weapons.Weapons import Weapons


class OneHand(Weapons):
    
    def clone(self):
        cloned_oneHand = OneHand()
        return cloned_oneHand