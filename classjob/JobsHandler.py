from classjob.JobsBuilder import JobsBuilder;

class JobsHandler:
    jobsBuilder: JobsBuilder

    def set_Job_Buldier(self, jb: JobsBuilder):
        self.jobsBuilder = jb
    
    def get_Job(self):
        return self.jobsBuilder.get_job()
    
    def contructJob(self):
        self.jobsBuilder.createNewJob()
        self.jobsBuilder.buildSkills()
        self.jobsBuilder.buildPassives()
        self.jobsBuilder.bulidDescription()
        self.jobsBuilder.buildWeapon()
        self.jobsBuilder.buildGear()