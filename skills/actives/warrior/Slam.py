from skills.Skills import Skills

class Slam(Skills):

    def __init__(self) -> None:
        self.kind = "active"

    def clone(self):
        return Slam()