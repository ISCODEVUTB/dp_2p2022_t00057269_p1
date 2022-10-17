from Races.Humans import Human
from Races.Orcs import Orc

class CharCreator:
    
    Human = Human()
    Orc = Orc()
    
    def retrieve_character(self, race:str):
        if race == "human":
            return self.Human.clone()
        if race == "Orc":
            return self.Orc.clone()

        return None 
