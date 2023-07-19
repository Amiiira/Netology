class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    
    def rate_lecturer(self, lecturer, course, rate):
        if isinstance(lecturer, Lecturer) and (course in self.finished_courses or course in self.courses_in_progress) and rate < 11:
            if course in lecturer.courses_attached:
                lecturer.rates[course] += [rate]
            else:
                lecturer.rates[course] = [rate]
        else:
            return 'Упс! Произошла ошибка'
        
    def __str__(self):
        sum = 0
        count = 0
        for grade in self.grades.values():
            for element in grade:
                sum += element
                count += 1
        
        mid = sum / count
        result = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {mid}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}' 
        return result  

    
    def __rates(self):
        sum = 0
        count = 0
        for course in self.grades.values():
            for rate in course:
                sum += rate
                count += 1
        average_rating = sum / count
        return average_rating
    

    def __lt__(self, other):
        if not isinstance(other, Student):
            return f'Упс! {other} не является студентом!'  
        average_self = self.__rates()
        average_other = other.__rates()
        return average_self <  average_other
                
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.rates = {}

    

class Lecturer(Mentor):
    def __rates(self):
        sum = 0
        count = 0
        for course in self.rates.values:
            for rate in course:
                sum += rate
                count += 1
        average_rating = sum / count
        return average_rating

    def __str__(self, rates):
        sum = 0
        for rate in self.rates:
            sum += rate
        result = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {Lecturer.__rates()}'
        return result
    
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return f'Упс! {other} не является преподавателем!'
        average_self = self.__rates
        average_other = other.__rates  
        return average_self < average_other


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def __str__(self):
        result = f'Имя: {self.name}\nФамилия: {self.surname}'
        return result

# Функция для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса
def calculate_average_grade(students, course):
    total_grades = 0
    total_students = 0

    for student in students:
        if course in student.grades:
            grades = student.grades[course]
            total_grades += sum(grades)
            total_students += len(grades)

    if total_students > 0:
        average_grade = total_grades / total_students
        return average_grade
    else:
        return 0

# Функция для посчета средней оценки за лекции всех лекторов в рамках курса
def calculate_average_lecture_rating(lecturers, course):
    total_ratings = 0
    total_lecturers = 0

    for lecturer in lecturers:
        if course in lecturer.rates:
            ratings = lecturer.rates[course]
            total_ratings += sum(ratings)
            total_lecturers += len(ratings)

    if total_lecturers > 0:
        average_rating = total_ratings / total_lecturers
        return average_rating
    else:
        return 0

# best_student = Student('Ruoy', 'Eman', 'your_gender')
# best_student.courses_in_progress += ['Python']
# best_student.finished_courses += ['Java']
 
# cool_mentor = Reviewer('Some', 'Buddy')
# cool_mentor.courses_attached += ['Python']
 
# cool_mentor.rate_hw(best_student, 'Python', 7)
# cool_mentor.rate_hw(best_student, 'Python', 6)
# cool_mentor.rate_hw(best_student, 'Python', 9)
 
# print(best_student.grades)

# print(best_student)

# Создаем студентов:
student_1 = Student('John', 'Mayer', 'male')
student_2 = Student('Bred', 'Pitt', 'male')
student_3 = Student('Lalisa', 'Manobal', 'female')

# Добавляем им курсы
student_1.courses_in_progress += ['Python',]
student_2.courses_in_progress += ['Python', 'Java']
student_3.courses_in_progress += ['Python', 'Kotlin']

student_1.finished_courses += ['Java']
student_2.finished_courses += ['-']
student_3.finished_courses += ['SQL']

# Добавляем ревьюверов и заклепряем за ними предметы
reviewer_1 = Reviewer('Some', 'Body')
reviewer_2 = Reviewer('Other', 'Body')

reviewer_1.courses_attached += ['Python']
reviewer_2.courses_attached += ['Java', 'Kotlin']

# Оцениваем:
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_2, 'Python', 6)
reviewer_1.rate_hw(student_2, 'Python', 10)
reviewer_1.rate_hw(student_3, 'Python', 5)
reviewer_1.rate_hw(student_3, 'Python', 7)

reviewer_2.rate_hw(student_2, 'Java', 9)
reviewer_2.rate_hw(student_2, 'Java', 9)
reviewer_2.rate_hw(student_3, 'Kotlin', 9)
reviewer_2.rate_hw(student_3, 'Kotlin', 9)

# Выводим студентов:
print(student_1)
print('-------')
print(student_2)
print('-------')
print(student_3)
print('-------')

#Сравниваем студентов:
print(student_1.__lt__(student_2))
print(student_2.__lt__(student_1))
print(student_3.__lt__(student_2))
print(student_3.__lt__(student_1))

# Сoздаем лекторов:
lecturer_1 = Lecturer('Jonny', 'Maitre')
lecturer_2 = Lecturer('Edward', 'SpongeBob')

lecturer_1.courses_attached = ['Python']
lecturer_2.courses_attached = ['Java', 'Kotlin']

student_1.rate_lecturer(lecturer_1, 'Python', 8)
student_2.rate_lecturer(lecturer_1, 'Python', 9)
student_3.rate_lecturer(lecturer_1, 'Python', 6)
student_2.rate_lecturer(lecturer_2, 'Java', 9)
student_3.rate_lecturer(lecturer_2, 'Kotlin', 10)

print(lecturer_1)
print('-----')
print(lecturer_2)
students = [student_1, student_2, student_3]  
course_name = "Python"  

average_grade = calculate_average_grade(students, course_name)
print(f"The average grade for {course_name} is: {average_grade}")