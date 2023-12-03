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


    def all_average_rating(self):
        list_grades = [list_grades for all_grades in self.grades.values() for list_grades in all_grades]
        return sum(list_grades) / len(list_grades)
        

    def average_rating(self, course):
        sum_course = 0
        len_course = 0
        for crs in self.grades.keys():
            if crs == course:
                sum_course += sum(self.grades[course])
                len_course += len(self.grades[course])
        result = sum_course / len_course
        return result


    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.all_average_rating()}" + \
            f"\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершенные курсы: {','.join(self.finished_courses)}"


    def __lt__(self, other):
        if isinstance(other, Student):
            return self.all_average_rating() < other.all_average_rating()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached =[]
        self.grades = {}

    def all_average_rating(self):
        list_grades = [list_grades for all_grades in self.grades.values() for list_grades in all_grades]
        return sum(list_grades) / len(list_grades)


    def average_rating(self, course):
        sum_course = 0
        len_course = 0
        for crs in self.grades.keys():
            if crs == course:
                sum_course += sum(self.grades[course])
                len_course += len(self.grades[course])
        result = sum_course / len_course
        return result


    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.all_average_rating() < other.all_average_rating()


    def __str__(self):
        return f"\nИмя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.all_average_rating()}"
    

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_hw_student(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
 

def average_grade(students_list, course):
    sum = 0
    sum_len = 0
    for stud in students_list:
        stud_sum = stud.average_rating(course)
        sum += stud_sum
        sum_len += 1
    result = sum / sum_len
    return print(result)


student_1 = Student('David', 'Smith', 'your_gender')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Git']
student_1.finished_courses += ['Введение в программирование']

student_2 = Student('Maria', 'Ivanova', 'your_gender')
student_2.courses_in_progress += ['Python']
student_2.courses_in_progress += ['Git']
student_2.finished_courses += ['Введение в программирование']

lecturer_1 = Lecturer('Sam', 'Frodo')
lecturer_1.courses_attached += ['Python']
lecturer_1.courses_attached += ['Git']
student_1.rate_lecturer(lecturer_1, 'Python', 10)
student_1.rate_lecturer(lecturer_1, 'Python', 9)
student_1.rate_lecturer(lecturer_1, 'Python', 9)
student_2.rate_lecturer(lecturer_1, 'Git', 6)

lecturer_2 = Lecturer('Jonn', 'Davis')
lecturer_2.courses_attached += ['Python']
student_2.rate_lecturer(lecturer_2, 'Python', 10)
student_2.rate_lecturer(lecturer_2, 'Python', 10)
student_2.rate_lecturer(lecturer_2, 'Python', 9)

reviewer_1 = Reviewer('Brus', 'Lee')
reviewer_1.courses_attached += ['Python']
reviewer_1.courses_attached += ['Git']
reviewer_1.rate_hw_student(student_1, 'Python', 10)
reviewer_1.rate_hw_student(student_1, 'Python', 10)
reviewer_1.rate_hw_student(student_1, 'Python', 7)
reviewer_1.rate_hw_student(student_1, 'Git', 8)

reviewer_2 = Reviewer('Anna', 'Smirnova')
reviewer_2.courses_attached += ['Python']
reviewer_2.courses_attached += ['Git']
reviewer_2.rate_hw_student(student_2, 'Python', 10)
reviewer_2.rate_hw_student(student_2, 'Python', 10)
reviewer_2.rate_hw_student(student_2, 'Python', 6)
reviewer_2.rate_hw_student(student_2, 'Git', 8)

print(student_1)
print(student_2)
print(student_1.grades)
print(student_2.grades)
print(lecturer_1.grades)
print(lecturer_2.grades)
print(lecturer_1)
print(lecturer_2)
print(lecturer_1 < lecturer_2)
print(student_1 < student_2)


student_list = [student_1, student_2]
average_grade(student_list, 'Python')
