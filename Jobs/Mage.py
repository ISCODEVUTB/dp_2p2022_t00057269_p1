from Gear.GearCreator import gearCreator
from Jobs.JobsBuilder import JobsBuilder
from Weapons.WeaponsCreator import weaponsCreator
from skills.passives.mage.manaRegn import bmanaReng
from skills.actives.mage.frostBolt import fbold

class Mage(JobsBuilder):
    
    def buildGear(self):
        self.job.set_gear(gearCreator.retrieveGear("Cloth"))
    
    def buildPassives(self):
        self.job.set_passives(
            {
                "1": bmanaReng
            }
        )
    
    def buildSkills(self):
        self.job.set_skills(
            {
                "1": fbold
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