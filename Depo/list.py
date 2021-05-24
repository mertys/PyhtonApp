# cities = ['tokyo' , 'madrid' , 'londra' , 'kiev']

# print(cities.index('tokyo')) listede kaçıncı indexde olduğunu gösterir
# print('ankara' in cities) liste içinde olup olmadığını kontrol eder

# str_email = 'mertys1234@gmail.com'
# my_list2 = str_email.split('@')
# print(my_list2) 

# for number in range(1,10):
#    print(number)              1 den 10 a kadar olan sayıları yazdır. 10 dahil değil.

# for number in range(1,10,4): 3 parametre artış sayısı
   # print(number)  

# numbers = list(range(1,11))
# print(numbers)
                                                 #1den 11 e kadar olan sayıları liste hallnde yazdırma
# numbers = [number for number in range(1,11)]
# print(numbers)

cities = ['izmir', 'ankara' , 'istanbul']
print(cities)
cities2 = cities[:]
print(cities2)
cities.append('artvin')   #listeye eleman ekleme
print(cities)
print(cities2)