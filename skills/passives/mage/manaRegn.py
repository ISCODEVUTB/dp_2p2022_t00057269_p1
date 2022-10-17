from skills.SkillsBuildier import SkillsBuilder
from skills.SkillsHandler import SkillHandler

class manaRegn(SkillsBuilder):

    def buildDescription(self):
        self._skill.set_description(
            """
                mana regen increase by the amount of mana you have, alse gain 20% more mana from
                objects 
            """
        )
    
    def buildDmg(self):
        self._skill.set_dmg(0)
    
    def buildEfects(self):
        self._skill.set_efects(
            """
            if you wear a object than gives you mana you gain 20% more of the mana value. 
            """
        )
    
    def buildHeal(self):
        self._skill.get_heal(0)
    
    def buildKind(self):
        self._skill.set_kind("passive")

manaren = manaRegn()
skillHandler = SkillHandler()
skillHandler.set_skill_builder(manaRegn)
skillHandler.constructSkill()
bmanaReng = skillHandler.get_Skill()