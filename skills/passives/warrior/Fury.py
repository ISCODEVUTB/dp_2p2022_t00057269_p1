from skills.Skills import Skills


class Fury(Skills):

    def __init__(self) -> None:
        self.kind = "passive"

    def clone(self):
        return Fury()
    