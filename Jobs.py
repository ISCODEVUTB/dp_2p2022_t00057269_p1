class Jobs:
    skills = dict
    description = ""
    passives = dict
    weapons = dict
    gear = dict

    def set_description(self, description):
        self.description = description

    def get_description(self):
        return self.description

    def set_passives(self, passives):
        self.passives = passives

    def get_passives(self) -> dict:
        return self.passives

    def set_weapons(self, weapon):
        self.weapons = weapon
        
    def get_weapons(self) -> dict:
        return self.weapons

    def set_gear(self, gear):
        self.gear = gear

    def get_gear(self) -> dict:
        return self.gear
    
    def set_skills(self, skill):
        self.skills = skill

    def get_skills(self) -> dict:
        return self.skills

    def get_name(self):
        return self.__class__.__name__