from Weapons.Weapons import Weapons


class Daggers(Weapons):
    
    def clone(self):
        cloned_dagger = Daggers()
        return cloned_dagger