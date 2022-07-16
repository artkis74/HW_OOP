class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lect(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grades(self):
        for grades in self.grades.values():
            average_grade = round(sum(grades) / len(grades), 1)
        return average_grade
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСреднняя оценка за домашние задания: ' \
              f'{self.average_grades()}\nКурсы в процессе изучения: {",".join(self.courses_in_progress)}\n'\
              f'Завершенные курсы: {",".join(self.finished_courses)}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        return self.average_grades() < other.average_grades()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grades(self):
        for grades in self.grades.values():
            average_grade = round(sum(grades) / len(grades), 1)
        return average_grade

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСреднняя оценка: {self.average_grades()}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        return self.average_grades() < other.average_grades()


class Revicewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student,
                      Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.finished_courses += ["Введение в программирование"]
best_student1 = Student('Some', 'Student', 'your_gender')
best_student1.courses_in_progress += ['Python', 'Git']
best_student1.finished_courses += ["Введение в программирование"]

cool_lecturer = Lecturer('Some', 'Buddy')
cool_lecturer.courses_attached += ['Python']
cool_lecturer1 = Lecturer('Bob', 'Black')
cool_lecturer1.courses_attached += ['Python']

cool_revicewer = Revicewer('Mike', 'Tyson')
cool_revicewer.courses_attached += ['Python']

cool_revicewer.rate_hw(best_student, 'Python', 10)
cool_revicewer.rate_hw(best_student, 'Python', 10)
cool_revicewer.rate_hw(best_student, 'Python', 10)
cool_revicewer.rate_hw(best_student1, 'Python', 2)
cool_revicewer.rate_hw(best_student1, 'Python', 5)
cool_revicewer.rate_hw(best_student1, 'Python', 7)

best_student.rate_lect(cool_lecturer, 'Python', 1)
best_student.rate_lect(cool_lecturer, 'Python', 10)
best_student.rate_lect(cool_lecturer, 'Python', 8)
best_student.rate_lect(cool_lecturer1, 'Python', 2)
best_student.rate_lect(cool_lecturer1, 'Python', 4)
best_student.rate_lect(cool_lecturer1, 'Python', 5)

print(best_student.grades)
print(cool_lecturer.grades)
print(cool_revicewer)
print(cool_lecturer.average_grades())
print(best_student.average_grades())
print(cool_lecturer1.average_grades())
print(cool_lecturer1)
print(cool_lecturer1 < cool_lecturer)
print(best_student1)
print(best_student > best_student1)