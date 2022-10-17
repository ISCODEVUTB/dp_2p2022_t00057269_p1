from Characters import Character

class Human(Character):

    SIDE = "BLUE"

    def clone(self):
        cloned_human = Human()
        return cloned_human