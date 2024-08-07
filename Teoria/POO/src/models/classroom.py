from models.teacher import Teacher

class Classroom:
    def __init__(self, teacher, issue):
        self.teacher = teacher.name
        self.issue = issue
        self.students = []
        
    def add_student(self, student):
        self.students.append(student)
    
    def presence_list(self):
        print(f'Presença na aula sobre {self.issue}, ministrada pelo professor {self.teacher}:')
        for student in self.students:
            print(f'O aluno {student.name} está presente.')
        