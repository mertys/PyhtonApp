#list 1 ve list 2 yi topla ve çarp

""" list_1 = [14,12,26,32]
list_2 = [4,5,2,1]

print(list(map(lambda x,y: x + y, list_1 , list_2)))
print(list(map(lambda x,y: x * y, list_1 , list_2))) """

#list comprehesiıob yöntemi ile fahrenheit fh = [99,108,176,234] derecelerini celcius derecelerine çevirelim c = (f-32)*(5/9)

""" fh = [99,108,176,234]

print([(f-32)*(5/9) for f in fh]) """

#print(map(len , [[1],[2],[3]] ))  ? ekran çıktısı ne olur ?
"""
print(map(len , [[1],[2],[3]] ))
"""

#str_List = ['Mustafa' , 'Ahmet' , 'Arin' , 'Cem' , 'Aysegul' , 'Hakan'] ismin uzunluğu 4 harf ve küçük olanlar için yeni bir liste 

""" 
str_List = ['Mustafa' , 'Ahmet' , 'Arin' , 'Cem' , 'Aysegul' , 'Hakan']
print(list(filter(lambda name: len(name) <=4,str_List)))
"""


#list_1 = [2,98,17,4,36,1] listedeki en küçük elemanı bul min vs sort
"""
list_1 = [2,98,17,4,36,1]
list_1.sort()
print(list_1[0])
"""
"""
list1 = [1]
list2 = [1,2]
list3 = [1,2,3] en uzun listeyi key kullanarak bulunuz
"""
# list1 = [1]
# list2 = [1,2]
# list3 = [1,2,3]

# print('En uzun liste: ',max(list1,list2,list3, key=len))

"""
mytuple = (0,1,False)
mydict = {0:"Apple",1:"Orange"}
myset = {0,1,0}
any  fonksiyonu için dönen değerler ?
"""
mytuple = (0,1,False)
mydict = {0:"Apple",1:"Orange"}
myset = {0,1,0}

print(any(mytuple))
print(any(mydict))
print(any(myset))
