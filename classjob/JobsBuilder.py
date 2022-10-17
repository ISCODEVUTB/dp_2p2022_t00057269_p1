from abc import  ABC, abstractmethod
from Jobs import Jobs

class JobsBuilder(ABC):
    _job: Jobs

    def get_job(self):
        return self.job
    
    def createNewJob(self):
        self.job = Jobs()
    
    def buildSkills(self):
        ...
    
    def buildPassives(self):
        ...
    
    def bulidDescription(self):
        ...

    def buildWeapon(self):
        ...
    
    def buildGear(self):
        ...