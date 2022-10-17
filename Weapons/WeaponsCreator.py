from Weapons.Dagger import Daggers
from Weapons.Shield import Shield
from Weapons.Stave import Stave
from Weapons.TwoHands import TwoHands
from Weapons.OneHand import OneHand


class WeaponCreator:

    twoHand = TwoHands()
    oneHand = OneHand()
    daggers = Daggers()
    shield = Shield()
    stave = Stave()

    def retrieveWeapon(self, weapon: str):
        if weapon == "Two Hands":
            return self.twoHand.clone()
        if weapon == "One hand":
            return self.oneHand.clone()
        if weapon == "daggers":
            return self.daggers.clone()
        if weapon == "shield":
            return self.shield.clone()
        if weapon == "stave":
            return self.stave.clone()

weaponsCreator = WeaponCreator()


    