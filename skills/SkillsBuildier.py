from abc import ABC
from skills.Skills import Skills


class SkillsBuilder(ABC):
    _skill: Skills

    def get_skill(self):
        return self._skill
    
    def createNewSkill(self):
        self._skill = Skills()
    
    def buildEfects(self):
        ...
    
    def buildDescription(self):
        ...
    
    def buildKind(self):
        ...
    
    def buildDmg(self):
        ...
    
    def buildHeal(self):
        ...