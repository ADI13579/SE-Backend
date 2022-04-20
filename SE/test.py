
from models import  Program, Semester, Subject, MasterSubject, Department


prog = Program.objects.filter(prog_code="BCT")
sub = Subject.objects.get(sub_code="SC")
# sub.sub_code=data['subCode']
sub.sub_name = "new name"
print(sub.sub_name )
sub.level = "BE"
sub.prog_code = prog[0]
# sub.implemented_on=datetime.date(int(data['batch']),1,1)
sub.save
