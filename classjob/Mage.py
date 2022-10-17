from Gear.GearCreator import gearCreator
from classjob.JobsBuilder import JobsBuilder
from Weapons.WeaponsCreator import weaponsCreator
from skills.SkillsCreator import SkillsCreator



class Mage(JobsBuilder):

    skillCreator = SkillsCreator()

    def buildGear(self):
        self.job.set_gear(gearCreator.retrieveGear("Cloth"))
    
    def buildPassives(self):
        self.job.set_passives(
            {
                "1": self.skillCreator.retrieveSkill("mana regeneration")
            }
        )
    
    def buildSkills(self):
        self.job.set_skills(
            {
                "1": self.skillCreator.retrieveSkill("frostbolt")
            }
        )
    
    def buildWeapon(self):
        self.job.get_weapons(
            {
                "1": weaponsCreator.retrieveWeapon("One hand"),
                "2": weaponsCreator.retrieveWeapon("daggers"),
                "3": weaponsCreator.retrieveWeapon("stave")
            }
        )
    
    def bulidDescription(self):
        self.job.set_description(
            """
            mages are skillfull magic users capable to create food an drinks via spells.
            """
        )