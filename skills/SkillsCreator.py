from skills.passives.warrior.Fury import Fury
from skills.passives.mage.manaRegn import manaRegn
from skills.actives.mage.frostBolt import FrostBolt
from skills.actives.warrior.Slam import Slam


class SkillsCreator():
    fury = Fury()
    manaRegn = manaRegn()
    frosbold = FrostBolt()
    Slam = Slam()

    def retrieveSkill(self, name:str):
        if name == "fury":
            return self.fury.clone()
        if name == "mana regeneration":
            return self.manaRegn.clone()
        if name == "frostbold":
            return self.frosbold.clone()
        if name == "slam":
            return self.Slam.clone()