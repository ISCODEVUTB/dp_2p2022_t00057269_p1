from SkillsBuildier import SkillsBuilder
from passives.warrior.Fury import Fury 


class SkillHandler:

    skillsBuilder: SkillsBuilder

    def set_skill_builder(self, sb: SkillsBuilder):
        self.skillsBuilder = sb

    def get_Skill(self):
        return self.skillsBuilder.get_skill()
    
    def constructSkill(self):
        self.skillsBuilder.createNewSkill()
        self.skillsBuilder.buildDescription()
        self.skillsBuilder.buildDmg()
        self.skillsBuilder.buildEfects()
        self.skillsBuilder.buildHeal()
        self.skillsBuilder.buildKind()

skillHandler = SkillHandler()
fury = Fury()