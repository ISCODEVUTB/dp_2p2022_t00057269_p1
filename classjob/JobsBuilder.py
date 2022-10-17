from abc import  abstractmethod
from Jobs import Jobs

class JobsBuilder:
    _job: Jobs

    def get_job(self):
        return self.job
    
    def createNewJob(self):
        self.job = Jobs()
    
    @abstractmethod
    def buildSkills(self):
        ...
    
    @abstractmethod
    def buildPassives(self):
        ...
    
    @abstractmethod
    def bulidDescription(self):
        ...

    @abstractmethod
    def buildWeapon(self):
        ...
    
    @abstractmethod
    def buildGear(self):
        ...