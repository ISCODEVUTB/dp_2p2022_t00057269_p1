from classjob.JobsBuilder import JobsBuilder
from Weapons.WeaponsCreator import weaponsCreator
from Gear.GearCreator import gearCreator
from skills.passives.warrior.Fury import bfury
from skills.actives.warrior.Slam import bslam

class warrior(JobsBuilder):

    def buildGear(self):
        self.job.set_gear(gearCreator.retrieveGear("Plates"))
    
    def buildPassives(self):
        
        self.job.set_passives(
            {
                "1": bfury
            }
        )
    
    def buildSkills(self):
        self.job.set_skills(
            {
                "1": bslam
            }
        )
    
    def buildWeapon(self):
        self.job.get_weapons(
            {
                "1": weaponsCreator.retrieveWeapon("Two hands"),
                "2": weaponsCreator.retrieveWeapon("One hand"),
                "3": weaponsCreator.retrieveWeapon("daggers"),
                "4": weaponsCreator.retrieveWeapon("staves")
            }
        )
    
    def bulidDescription(self):
        self.job.set_description(
            """
            warriors are braves brawlers ready to fitgh any battle 
            """
        )