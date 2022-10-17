from Characters import Character

class EnemyProcessor:
    def is_enemy(sefl, char:Character):
        if char.get_side() == "BLUE":
            print("enemy ---> RED")
            return "RED"
        elif char.get_side() == "RED":
            print("enemy ---> BLUE")
            return "BLUE"