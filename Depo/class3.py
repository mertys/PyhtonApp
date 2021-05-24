# class Circle:
#     pi = 3.14

#     def __init__(self , radius=1):
#         self.radius = radius

#     def area(self):
#         return self.radius * self.radius * self.pi

#     def __repr__(self):
#         return f'{__class__.__name__} object with {self.radius} radius'


class Student:

    def __init__(self , name , surname , age , grades):
        self.name = name
        self.surname = surname
        self.age = age
        self.grades = grades
    
    def average(self):
        return sum(self.grades) / len(self.grades)

    @property
    def fullname(self):
        return f'{self.name} {self.surname}'

student_1 = Student('Mert', 'Yurtseven' , 27 , [100,100,90])

student_1.name = 'Bervan'
student_1.surname = 'Daşlık'
student_1.grades = [50,50,50]

print(student_1.name)
print(student_1.surname)
print(student_1.fullname)
print(student_1.grades)
print(student_1.average())