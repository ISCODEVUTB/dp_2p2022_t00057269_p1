from Weapons.Weapons import Weapons


class Stave(Weapons):
    
    def clone(self):
        cloned_stave = Stave()
        return cloned_stave