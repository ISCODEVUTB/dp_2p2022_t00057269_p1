from abc import ABC


class Skills(ABC):
    kind: str
    dmg: int
    heal: int
    description: str
    efects:str

    def __init__(self) -> None:
        print("hello")

    def clone(self):
        ...

    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description
    
    def get_kind(self):
        return self.kind
    
    def set_kind(self, kind):
        self.kind = kind
    
    def get_dmg(self):
        return self.dmg

    def set_dmg(self, dmg):
        self.dmg = dmg
    
    def get_heal(self):
        return self.heal

    def set_heal(self, heal):
        self.heal = heal

    def get_efects(self):
        return self.efects

    def set_efects(self, efect):
        self.efects = efect


