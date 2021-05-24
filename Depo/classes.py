# class Car:
#     brand = None
#     model = None
#     year = None
    
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year
#     def brandmodel(self):
#         return f'Araba markası {self.brand} ve modeli {self.model} '


# car_1 = Car(brand="BMW", model="i5", year=1992)
# car_2 = Car(brand="audi", model="x5", year=1998)

# print(car_1)
# print(car_1.brand)

# print(car_1.brandmodel())



class Movie:
    def __init__(self , name, director):
        self.name = name
        self.director = director


movie_1 = Movie(
    name='Dövüş Kulübü',
    director='Mert Yurtseven'
)

movie_2 = Movie(
    name='Babel',
    director='Irarutu'
)

print(movie_1.director)
print(movie_2.director)
