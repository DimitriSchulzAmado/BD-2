from models.teacher import Teacher
from models.student import Student
from models.classroom import Classroom

def main():
    teacher = Teacher("Lucas")
    student1 = Student("Maria")
    student2 = Student("Pedro")
    classroom = Classroom(teacher, "Programação Orientada a Objetos")
    classroom.add_student(student1)
    classroom.add_student(student2)
    print(classroom.presence_list())

if __name__ == "__main__":
    main()