class Student:

    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)

class UniversteÖğrenci(Student):
#     pass

# u_student_1 = UniversteÖğrenci (
#     name = 'Mert', 
#     age = 27 ,
#     grades = [10,20,30]
# )

# print(u_student_1.age)
# print(u_student_1.name)
# print(u_student_1.average())
# print(help(UniversteÖğrenci))

  def __init__(self, name, age, grades, university):
      super().__init__(name, age, grades)
      self.university = university

u_student_1 = UniversteÖğrenci(
    name = 'Mert',
    age=27 ,
    grades=[50,30,40], 
    university='Sakarya Üni'
)
print(u_student_1.university)
print(u_student_1.average()
)