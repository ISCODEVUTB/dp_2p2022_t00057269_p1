from abc import ABC
from Jobs import Jobs


class Character(ABC):

    sex = ""
    name = ""
    description = ""
    width = 0.0
    height = 0.0
    SIDE: str
    job: Jobs 

    def clone(self):
        ...

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def get_side(self):
        return self.SIDE
    
    def get_racial(self):
        return self.racial

    def get_job(self):
        return self.job.get_name()

    def set_job(self, job: Jobs):
        self.job = job

    def get_sex(self):
        return self.sex

    def set_sex(self, sex):
        self.sex = sex

    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description

    def get_width(self):
        return self.width

    def set_width(self, width):
        self.width = width

    def get_heigth(self):
        return self.height

    def set_heigth(self, heigth):
        self.height = heigth


    def __str__(self) -> str:
        return str({
            "name": self.name,
            "gender": self.sex,
            "description": self.description,
            "width": self.width,
            "heigth":self.height,
            "side": self.SIDE,
            "job": self.job.__class__.__name__
        })