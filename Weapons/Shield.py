from Weapons.Weapons import Weapons


class Shield(Weapons):
    BLOCK: float

    def set_BLOCK(self, block: float):
        self.BLOCK = block
    
    def get_BLOCK(self):
        return self.BLOCK
    
    def clone(self):
        cloned_shield = Shield()
        return cloned_shield