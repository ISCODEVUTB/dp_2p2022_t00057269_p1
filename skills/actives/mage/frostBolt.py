from skills.SkillsBuildier import SkillsBuilder
from skills.SkillsHandler import skillHandler


class FrostBolt(SkillsBuilder):

    def buildDescription(self):
        self._skill.set_description(
            """
                cast a frost bold at the direcction of the enemy 
            """
        )
    
    def buildDmg(self):
        self._skill.set_dmg(30)
    
    def buildEfects(self):
        self._skill.set_efects(
            """
            cause the enemy gets slowed for 2 seconds. 
            """
        )
    
    def buildHeal(self):
        self._skill.get_heal(0)
    
    def buildKind(self):
        self._skill.set_kind("active")

fbold = FrostBolt()
skillHandler.set_skill_builder(fbold)
skillHandler.constructSkill()
bfbold = skillHandler.get_Skill()