from Races.Humans import Human
from Races.Orcs import Orc

class CharCreator:
    
    human = Human()
    orc = Orc()
    
    def retrieve_character(self, race:str):
        if race == "human":
            return self.human.clone()
        if race == "orc":
            return self.orc.clone()
        return None 
