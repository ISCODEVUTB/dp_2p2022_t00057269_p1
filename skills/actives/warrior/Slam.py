from skills.SkillsBuildier import SkillsBuilder
from skills.SkillsHandler import skillHandler


class Slam(SkillsBuilder):

    def buildDescription(self):
        self._skill.set_description(
            """
                a great slam with you righ handed weapon 
            """
        )
    
    def buildDmg(self):
        self._skill.set_dmg(15)
    
    def buildEfects(self):
        self._skill.set_efects(
            """
            cause the enemy become dizzy. 
            """
        )
    
    def buildHeal(self):
        self._skill.get_heal(0)
    
    def buildKind(self):
        self._skill.set_kind("active")

slam = Slam()
skillHandler.set_skill_builder(slam)
skillHandler.constructSkill()
bslam = skillHandler.get_Skill()