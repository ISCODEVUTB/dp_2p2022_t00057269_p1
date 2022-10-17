from skills.Skills import Skills

class manaRegn(Skills):
    
    def __init__(self) -> None:
        self.kind = "passive"

    def clone(self):
        return manaRegn()