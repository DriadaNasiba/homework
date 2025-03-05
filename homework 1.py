class Person:
    def __init__(self, full_name, age, is_married):
        self.full_name = full_name
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        marriage_status = "Married" if self.is_married else "Single"
        print(f'name:{self.full_name}')
        print(f'age: {self.age}')
        print(f'is_married: {self.is_married}')


class Student(Person):
    def __init__(self, full_name, age, is_married, marks):
        super().__init__(full_name, age, is_married)
        self.marks = marks

    def average_mark(self):
        if self.marks:
            avg = sum(self.marks.values()) / len(self.marks)
            return avg
        return 0
class Teacher(Person):
    base_salary = 50000

    def __init__(self, full_name, age, is_married, experience):
        super().__init__(full_name, age, is_married)
        self.experience = experience
        self.base_salary = base_salary

    def calculate_salary(self):
        bonus = 0
        if self.experience > 3:
            bonus = (self.experience - 3) * 0.05 * Teacher.base_salary
        return Teacher.base_salary + bonus

    def introduce_myself(self):
        super().introduce_myself()
        print(f'experiece:{self.experience}')
        print(f'calculate_salary:{self.calculate_salary()}')


def create_students():
    student1 = Student("Alice Smith", 16, False, {"Math": 4, "English": 5, "History": 4})
    student2 = Student("Bob Johnson", 17, False, {"Math": 3, "English": 4, "History": 5})
    student3 = Student("Charlie Brown", 16, False, {"Math": 5, "English": 5, "History": 5})

    return [student1, student2, student3]

students = create_students()
for student in students:
    student.introduce_myself()
    print(f"Marks: {student.marks}")
    print(f"Average mark: {student.average_mark()}")
    print()

