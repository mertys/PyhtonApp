#boş liste tuple set ve dictionary oluştur

# list1 = []
# list2 = list()
# print(type(list1))
# print(type(list2))

# tuple1 = ()
# tuple2 = tuple()
# print(type(tuple1))
# print(type(tuple2))


# set2 = set()
# print(type(set2))

# dict1 = {}
# dict2 = dict()
# print(type(dict1))
# print(type(dict2))



#değeri sayı olan 3 elemanlı bir dic oluştur 2.sayıyı ve sayıların ortalamasını çıkar

# friends = {'mert':27 , 'bervan':28 , 'anan':35}
# print(friends['bervan'])
# print(sum(friends.values())/ len(friends))


#2okul arkadaşı ve numaralardan oluşan bi dict oluştur başka bir arkadaş ekle ekli olanı sil update ile numarasını değiştir ve arkadaş ekle

# friends= {'mert':333 ,'bervan':444}
# friends['şahrut'] = 555
# print(friends)
# del friends['bervan']
# print(friends)
# friends.update({'mert':888 , 'bervan':999})
# print(friends)


# yukardaki dict yapısında bulunan elamanların karesini alıp aynı dict yapısını update et

# my_dict = {'odd_numbers' : [1,2,3]}

# my_dict = {'odd_numbers' : [1,2,3]}
# my_dict['odd_numbers'] = [my_dict['odd_numbers'][0]**2, my_dict['odd_numbers'][1]**2, my_dict['odd_numbers'][2]**2]
# print(my_dict)

# my_dict2 = {'even_numbers':[2,5,6,4,8,7,9,1,12]} tüm elemanların karesini al dict update et for döngüsü ile yap

# my_dict2 = {'even_numbers':[2,5,6,4,8,7,9,1,12]}

# for x in my_dict2.values():
#     my_list = []
#     for y in  x:
#         my_list.append(y**2)

# my_dict2['even_numbers'] = my_list
# print(my_dict2)

#key ler ve value lerden liste oluştur ve value ler toplamını çıkar

# my_friends = {'mert':25,'emre':35,'bervan':45}
# my_key_list = []
# my_value_list =[]

# for k , v in my_friends.items():
#     my_key_list.append(k)
#     my_value_list.append(v)

# print(my_key_list)
# print(my_value_list)
# print(sum(my_value_list))


#dict comp ile 1 den 10 a kadar olan sayılar sayıları key kareleri value olacak şekilde tek satırda oluştur

# numbers = { x: x**2 for x in range(1,11) }
# print(numbers)