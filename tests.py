from BlueSidedRaces import *
from RedSidedRaces import *
from Jobs import *
from IFicha import *


IFicha = IFicha()

humanoRouge = Human("Santi",Rogue())
orcWarrior = Orc("Sebastian", Warrior())
darkElfMage = DarkElf("vale",Mage())

#human test
humanoRouge.set_sex("male")
humanoRouge.set_heigth("6'5")
humanoRouge.set_width("50")
humanoRouge.set_description("feroz combatiente")


#orc Test
orcWarrior.set_sex("male")
orcWarrior.set_heigth("7'8")
orcWarrior.set_width("60")
orcWarrior.set_description("combatiente que se las sabe todas")


# dark elf test
darkElfMage.set_sex("female")
darkElfMage.set_heigth("5'7")
darkElfMage.set_width("30")
darkElfMage.set_description("hermosa maga")




IFicha.defineEnemy(humanoRouge)
IFicha.add(humanoRouge)
print("\n")

IFicha.defineEnemy(orcWarrior)
IFicha.add(orcWarrior)
print("\n")

IFicha.defineEnemy(darkElfMage)
IFicha.add(darkElfMage)
print("\n")


