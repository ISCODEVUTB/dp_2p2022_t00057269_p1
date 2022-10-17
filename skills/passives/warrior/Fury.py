from skills.SkillsBuildier import SkillsBuilder
from skills.SkillsHandler import skillHandler



class Fury(SkillsBuilder):

    def buildDescription(self):
        self._skill.set_description(
            """
            every time you aare in combage generate 5 fury for second,
            meele atacks and damage generate
            fury per amount of damage given or taken 
            """
        )
    
    def buildDmg(self):
        self._skill.set_dmg(0)
    
    def buildHeal(self):
        self._skill.set_heal(0)
    
    def buildEfects(self):
        self._skill.set_efects(
            """
                every time you hit gain fury depends on the amoun of dmg you make
            """
            )
    
    def buildKind(self):
        self._skill.set_kind("passive")

fury = Fury()
skillHandler.set_skill_builder(Fury)
skillHandler.constructSkill()
bfury = skillHandler.get_Skill()
    