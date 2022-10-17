from CharacterCreator import CharCreator
from classjob.Mage import Mage
from classjob.Warrior import warrior
from classjob.JobsHandler import JobsHandler 

jobsHandler = JobsHandler()
characterCreator = CharCreator()

print("chose a race")
print(
    "type"
    "1. human"
    "2. Orc"
    )
option = input("your option")
char = characterCreator.retrieve_character(option)
cname = input("give a name: ")
char.set_name(cname)
csex = input("character gender")
char.set_sex(csex)
cwitgd = float(input("character width"))
char.set_width(cwitgd)
cheight = float(input("character height"))
char.set_heigth(cheight)

option2 = input("choose a job for the character (type-> mage or warrior ")
if option2 == "mage":
    job = Mage()
    jobsHandler.set_Job_Buldier(job)
    jobsHandler.contructJob()
    char.set_job(jobsHandler.get_Job())
if option2 == "warrior":
    job = warrior()
    jobsHandler.set_Job_Buldier(job)
    jobsHandler.contructJob()
    char.set_job(jobsHandler.get_Job())

print(char.__str__())

    

