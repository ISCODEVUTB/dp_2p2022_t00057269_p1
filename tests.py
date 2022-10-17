import unittest
from CharacterCreator import CharCreator
from skills.SkillsCreator import SkillsCreator
from skills.passives.mage.manaRegn import manaRegn
from classjob.JobsHandler import JobsHandler
from classjob.Mage import Mage
from classjob.Warrior import warrior
from Weapons.WeaponsCreator import WeaponCreator
from Gear.GearCreator import GearCreator
from EnemyProcessor import EnemyProcessor


class objects_creation_test(unittest.TestCase):

    gearCreator = GearCreator()
    weaponsCreator = WeaponCreator()
    charCreator = CharCreator()
    skillsCreator = SkillsCreator()
    jobHandler = JobsHandler()
    habi = manaRegn() 
    mage = Mage()
    warrior = warrior()
    ep = EnemyProcessor()

    def  ep_test(self):
        char = self.charCreator.retrieve_character("orc")
        enemy = self.ep.isEnemy(char)
        self.assertEquals(enemy, "BLUE")

    def character_creation_test(self):
        char = self.charCreator.retrieve_character("human")
        char.set_name("santiago")
        char.set_sex("hombre")
        name = char.get(name)
        charRace = char.__class__.__name__
        self.assertEqual(name,"Santiago")
    
    def skill_creation_test(self):
        fury = self.skillsCreator.retrieveSkill("fury")
        self.assertEquals(fury.__class__.__name__, "Fury")
    
    def mage_creation_test(self):
        self.jobHandler.set_Job_Buldier(self.mage)
        self.jobHandler.contructJob()
        constructed_job = self.jobHandler.get_Job()
        self.assertEquals(constructed_job.__class__.__name__, "Jobs")
    
    def mage_creation_test(self):
        self.jobHandler.set_Job_Buldier(self.mage)
        self.jobHandler.contructJob()
        constructed_job = self.jobHandler.get_Job()
        self.assertEquals(constructed_job.__class__.__name__, "Jobs")
    
    def warrior_creation_test(self):
        self.jobHandler.set_Job_Buldier(self.warrior)
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
