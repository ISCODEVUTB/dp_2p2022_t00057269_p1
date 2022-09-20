import unittest
from BlueSidedRaces import *
from EnemyProcessor import BlueEnemyProcessor
from RedSidedRaces import *
from Jobs import *
from IFicha import *
from EnemyProcessor import *


class charCreationTest(unittest.TestCase):

    IFicha = IFicha()

    humanoRouge = Human("Santi",Rogue())
    orcWarrior = Orc("Sebastian", Warrior())
    darkElfMage = DarkElf("vale",Mage())

    #human test
    def test_human_sexsetter(self):
        self.humanoRouge.set_sex("male")
        self.assertEquals(self.humanoRouge.sex,'male')

    def test_human_set_heigth(self):
        self.humanoRouge.set_heigth("6'5")
        self.assertEquals(self.humanoRouge.heigth,"6'5")

    def test_human_set_width(self):
        self.humanoRouge.set_width("50")
        self.assertEquals(self.humanoRouge.width,"50")

    def test_human_job(self):
        self.assertEquals(self.humanoRouge.job, Rogue())

    #orc Test
    def test_orc_sexsetter(self):
        self.orcWarrior.set_sex("male")
        self.assertEquals(self.orcWarrior.sex, "male")

    def test_orc_set_heigth(self):
        self.orcWarrior.set_heigth("7'8")
        self.assertEquals(self.orcWarrior.heigth,"7,8")

    def test_orc_set_width(self):
        self.orcWarrior.set_width("60")
        self.assertEqual(self.orcWarrior.width, "60")

    def test_orc_job(self):  
        self.assertAlmostEquals(selforcWarrior.job, Warrior())


    # dark elf test
    def test_de_sexsetter(self):
        self.darkElfMage.set_sex("female")
        self.assertEquals(self.darkElfMage.sex, "female")

    def test_de_set_heigth(self):    
        self.darkElfMage.set_heigth("5'7")
        self.assertEquals(self.darkElfMage.heigth,"5'7")

    def test_de_set_width(self):
        self.darkElfMage.set_width("30")
        self.assertEquals(self.darkElfMage.width,"30")
    
    def test_de_job(self):
        self.assertEquals(self.darkElfMage.job, Mage())

    def test_define_human_enemy(self):
        pross = BlueEnemyProcessor()
        self.assertAlmostEquals(self.IFicha.defineEnemy(self.humanoRouge), pross.IsEnemy(self.humanoRouge)) 

    def test_define_orc_enemy(self):
        pross = RedEnemyProcessor()
        self.assertAlmostEquals(self.IFicha.defineEnemy(self.orcWarrior), pross.IsEnemy(self.orcWarrior))

   def test_define_de_enemy(self):
        pross = BlueEnemyProcessor()
        self.assertAlmostEquals(self.IFicha.defineEnemy(self.darkElfMage), pross.IsEnemy(self.darkElfMage)) 


if __name__ == '__main__':
    unittest.main