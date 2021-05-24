#Student isimli bir class oluştur
#properties(attributes) 3 adet name age grades
#metdods 1 adet grades (notlar) ortalamasını gösteriyor
class Student:

    school_name = 'X lisesi'
    number_of_student = 0

    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades
        Student.number_of_student += 1

    def average(self):
        return sum(self.grades) / len(self.grades)

    def schoolName(self):
        return f'Okulumuzun Adı {self.school_name}'

    @classmethod
    def display_okul_adı(cls, okulun_adı):
        cls.okul_adı = okulun_adı

    @staticmethod
    def statik():
        return f'Sadece bu mesajı gönderiyorum'

Student.display_okul_adı('Y lisesi')

student_1 = Student(
    name ='mahmut',
    age = 18,
    grades = [50, 35, 40, 55]
)

student_2 = Student(
    name = 'Mert',
    age = 45 ,
    grades = [100, 80, 90, 100]
)

print(Student.statik())
print(student_1.statik())
print(student_2.statik())