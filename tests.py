import unittest
from CharacterCreator import CharCreator
from skills.SkillsHandler import SkillHandler
from skills.passives.mage.manaRegn import manaRegn
from Jobs.JobsHandler import JobsHandler
from Jobs.Mage import Mage
from Weapons.WeaponsCreator import WeaponCreator
from Gear.GearCreator import GearCreator


class objectsCreationTest(unittest.TestCase):

    gearCreator = GearCreator()
    weaponsCreator = WeaponCreator()
    charCreator = CharCreator()
    skillHandler = SkillHandler()
    jobHandler = JobsHandler()
    habi = manaRegn() 
    job = Mage()

    def character_creation_test(self):
        char = self.charCreator.retrieve_character("human")
        charRace = char.__class__.__name__
        self.assertEqual(charRace,"Human")
    
    def skill_creation_test(self):
        self.skillHandler.set_skill_builder(self.habi)
        self.skillHandler.constructSkill()
        contructed_skill = self.skillHandler.get_Skill()
        self.assertEquals(contructed_skill.__class__.__name__, "Skill")
    
    def job_creation_test(self):
        self.jobHandler.set_Job_Buldier(self.job)
        self.jobHandler.contructJob()
        constructed_job = self.jobHandler.get_Job()
        self.assertEquals(constructed_job.__class__.__name__, "Jobs")
    
    def weapon_creation_test(self):
        weapon = self.weaponsCreator.retrieveWeapon("staves")
        weapon_name = weapon.__class__.__name__
        self.assertEquals(weapon_name, "Stave")
    
    def gear_creation_test(self):
        gear = str(self.gearCreator.retrieveGear("plate"))
        self.assertEquals(gear, """{
                "head":self.Head.clone(type),
                "shoulders": self.Shoulders(type),
                "top": self.Top.clone(type),
                "bottom": self.Botton.clone(type),
                "gloves": self.Gloves.clone(type),
                "shoes": self.Shoes.clone(type)
                }""")
                
        


