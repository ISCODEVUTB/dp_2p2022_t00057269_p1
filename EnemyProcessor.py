from Characters import Character

class EnemyProcessor:
    def isEnemy(char:Character):
        if char.get_side() == "BLUE":
            print("enemy ---> RED")
        elif char.get_side() == "RED":
            print("enemy ---> BLUE")