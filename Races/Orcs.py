from Characters import Character

class Orc(Character):

    SIDE = "RED"

    def clone(self):
        cloned_orc = Orc()
        return cloned_orc