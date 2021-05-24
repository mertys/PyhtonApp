#ikinci ve son liste elemanının çıktısını büyük harfle alma
# dersler = ['mat' , 'fen' , 'müzik' , 'beden' , 'kimya']
# print(dersler[1].upper())
# print(dersler[4].upper())
# print(dersler[-1].upper())
#-------------------------------------------
#fizik ve kimya elamanlarının çıktısını al
#ilk iki elamanın çıktısını al 
#son iki elamanın çıktısını al

# print(dersler[1:3])
# print(dersler[:2])
# print(dersler[-2:])

#--------------------------------------------
#fizik ve kimyayı birlikte ve ayrı ayrı çıktı
#son elamanın çıktısını len yardımı ile al

# dersler = ['mat' , ['fen' , 'müzik' ], 'beden' , 'kimya']
# print(dersler[1])
# print(dersler[1][0])
# print(dersler[1][1])
# print(dersler[len(dersler)-1])

#---------------------------------------------

#liste uzunluğunu gösterme tarih dersini ekle çoğrafya ekle başka bir yol

# dersler = ['mat' , 'fen' , 'müzik' , 'beden' , 'kimya']

# print(len(dersler))
# dersler.append('tarih')
# print(dersler)
# dersler[len(dersler):] = ['çoğrafya']
# print(dersler)

#----------------------------------------------

#tarih dersini liste başına ekle insert ile çoğrafya liste sonuna

# dersler.insert(0,'tarih')
# print(dersler)

# dersler.insert(len(dersler), 'coğrafya')
# print(dersler)

#kimya dersini del ile kaldır fen dersini remove ile kaldır

# del dersler[4]
# print(dersler)

# dersler.remove('fen')
# print(dersler)

#--------------------------------------

#listeyi artacak ve azalacak şekilde sırala
 
#numbers = [2, 5, 6, 8, 9, 7, 10, 3, 4, 1, ]
#numbers.sort()
#print(numbers)
#numbers.reverse()
#print(numbers)

#----------------------------------------
#içteki listelerin son elemanlarıyla yeni bir liste oluşturma

# dersler = [['mat' , 'fen'] , ['müzik'] , ['beden' , 'kimya']]

#yöntem 1

#dersler2 = []
#dersler2.append(dersler[0][-1])
#dersler2.append(dersler[1][-1])
#dersler2.append(dersler[2][-1])
#print(dersler2)

#yöntem 2

#dersler2 = []

#for ders in dersler:
 #   dersler2.append(ders[-1])
#print(dersler2)

#1 den 10 a kadar sayıların karelerinden list oluştrma

#yöntem 1
# squares = []

#for num in range(1,11):
 #   squares.append(num**2)
#print(squares)

#yöntem 2
squares = [num**2 for num in range(1,11)]
print(squares)
