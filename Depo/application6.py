#friends = ['ahmet', 'mehmet', 'ebru', 'mahmut', 'ayşe']  mahmut hariç diğer elemanları while ve for loop kullanarak yazdırın.

# friends = ['ahmet', 'mehmet', 'ebru', 'mahmut', 'ayşe']
# for key in friends:
#     if key == 'mahmut':
#         continue
#     print(key)

# friends = ['ahmet', 'mehmet', 'ebru', 'mahmut', 'ayşe']
# x = 0
# while (x < len(friends)):
#     friend = friends[x]
#     x = x + 1
#     if friend == 'mahmut':
#         continue
#     print(friend)

# kullanıcı tarafından girilen 2 rakam arasındaki çift sayıların çıktısını alın

# minNum = int(input('1.Sayıyı giriniz: '))
# maxNum = int(input('2.Sayıyı giriniz: '))

# for evenNum in range(minNum,maxNum):
#     if evenNum % 2 != 0:
#         continue
#     else:
#         print(evenNum)

# while döngüsü kullanarak 1 ile 100 arasında sayı tahminleri yapabilceniz bir program yazınız 

# import random
# xnum = random.randint(1, 100)

# num = int(input('Lütfen bir tahmin yapınız: '))

# while num  !=xnum:
#     if num  < xnum:
#         print(f'{num } daha büyük bir sayı giriniz')
#         num = int(input())
#     else:
#         print(f'{num } daha küçük bir sayı giriniz')
#         num  = int(input())

# print(f' Tebrikler {num } buldunuz!!!!')


# celciuses = [20, 25 ,30 ,35] derecelerini kelvin ve fahrenheit olarak iki ayrı listeye dönüştür.
# K = C + 273 
# F = C * 9 / 5 + 32

# celciuses = [20, 25 ,30 ,35]
# kelvin = []
# fahrenheit = []

# for c in celciuses:
#      k = c + 273
#      kelvin.append(k)
#      f = c * 9 / 5 + 32
#      fahrenheit.append(f)

# print(kelvin)
# print(fahrenheit)

# kullanıcıdan bir sayı girmesini isteyin ve o sayı ve öncekilerin toplamını yazalım

# sayı = int(input('Lütfen Sayı Gir: '))

# if sayı < 0:
#     print('Negatif Sayı Girdiniz')
# else:
#     sum = 0
#     while sayı > 0:
#         sum += sayı
#         sayı -= 1
# print('Toplam Sayı: ', sum)