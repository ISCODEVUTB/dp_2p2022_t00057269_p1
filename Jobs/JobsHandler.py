from JobsBuilder import JobsBuilder;

class JobsHandler:
    jobsBuldier: JobsBuilder

    def set_Job_Buldier(self, jb: JobsBuilder):
        self.jobsBuldier = jb
    
    def get_Job(self):
        return self.jobsBuldier.getJob()
    
    def contructJob(self):
        self.JobsBuilder.createNewJob()
        self.JobsBuilder.buildSkills()
        self.JobsBuilder.buildPassives()
        self.JobsBuilder.bulidDescription()
        self.JobsBuilder.buildWeapon()
        self.JobsBuilder.buildGear()