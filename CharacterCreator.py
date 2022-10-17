from Races.Humans import Humans
from Races.Orcs import Orcs

class CharCreator:
    
    Human = Humans()
    Orc = Orcs()
    
    def retrieve_character(self, race:str):
        if race == "human":
            return self.Human.clone()
        if race == "Orc":
            return self.Orc.clone()

        return None 
