# Girilen sayının karesini çıktı gösteren bir fonksiyon.

# def kare(x):
#     return x**2

# x = int(input('Sayı Giriniz: '))

# print(f'Girilen {x} saysının karesi {kare(x)}')


# Girilen 2 sayının toplamını ve çarpımını veren lambda ifadeleri kullan.

# x = int(input('1.Sayı: '))
# y = int(input('2.Sayı: '))


# topla = lambda x,y : x + y
# carp = lambda x,y : x * y

# print(f'Girilen {x} sayısının ve {y} saysının toplamı {topla(x,y)} çarpımı {carp(x,y)}')

# Bir liste içindeki sayısal elemanlarının çarpımını gösteren bir fonksiyon

# def multiply(mylist):
#     mult = 1
#     for x in mylist:
#         mult *= x
#     return mult

# list1=[3,5,6,10]

# print(multiply(list1))

# Kullanıcı tarafında girilen bir sayısının faktöriyelini gösteren fonks

# def faktöriyel(a):
#     if a == 0:
#         return 1
#     else:
#         return a * faktöriyel(a-1)

# a = int(input('Lütfen Sayı Giriniz : '))

# print(faktöriyel(a))

# Bir küpün alan hacim ve çevresini hesapla

# def küp_cevre(a):
#     return 12*a

# def küp_alan(a):
#     return 6*a**2

# def küp_hacim(a):
#     return a**3

# a = int(input('Lütfen Kenar Uzunluğunu Giriniz : '))
# print(küp_alan(a) , küp_cevre(a) , küp_hacim(a))