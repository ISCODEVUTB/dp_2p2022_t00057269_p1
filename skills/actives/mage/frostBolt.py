from skills.Skills import Skills


class FrostBolt(Skills):

    def __init__(self) -> None:
        self.kind = "active"

    def clone(self):
        return FrostBolt()

 