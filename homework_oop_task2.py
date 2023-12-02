class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.courses_attached =[]
        self.grades = {}

class Reviewer(Mentor):
    def __init__(self, name, surname):
        self.courses_attached = []


    def rate_hw_student(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
 


student_1 = Student('David', 'Smith', 'your_gender')
student_1.courses_in_progress += ['Python']
 
lecturer_1 = Lecturer('Sam', 'Noname')
lecturer_1.courses_attached += ['Python']
student_1.rate_lecturer(lecturer_1, 'Python', 10)
student_1.rate_lecturer(lecturer_1, 'Python', 7)
student_1.rate_lecturer(lecturer_1, 'Python', 9)

reviewer_1 = Reviewer('Some', 'Buddy')
reviewer_1.courses_attached += ['Python']
 
reviewer_1.rate_hw_student(student_1, 'Python', 10)
reviewer_1.rate_hw_student(student_1, 'Python', 10)
reviewer_1.rate_hw_student(student_1, 'Python', 10)
 
print(student_1.grades)
print(lecturer_1.grades)