#data.txt dosyasını reading modda açalım ve aşağıdaki komutlar üzerine konuşalım

# with open('data.txt','r') as my_file:
#     print(my_file.read()) #Read komutu data.txt dosyasındaki tüm bilgiyi konsola yazdırır.
#     print(my_file.read(5)) #parametre aldığı kadar bilgi gösterir
#     my_file.seek(0) #0 değeri aldığında dosyanın başına götürür
#     print(my_file.read(6))
#     print(my_file.tell()) #Hangi sırada olduğunu gösterir.

# //courses = [Pyhton,Java, C## , Ruby] liste elemanlarını bir dosyaya alt alta yazalım

# courses = ['Pyhton', 'Java' , 'C##' , 'Ruby']
# with open('courses.txt' , 'w') as my_file:
#     for course in courses:
#         my_file.write(f'{course}\n')

# movies.txt dosyasını okuyarak her bir sırayı bir listede gösterelim.

# with open ('movies.txt' , 'r') as my_file:
#     file_content = my_file.readlines()
#     file_content = [ element.strip('\n') for element in file_content if '\n' in element]
#     print(file_content) 

#movies.txt dosyasının içindeki bilgiler ile kopyala

# with open ('movies.txt' , 'r') as my_file:
#     with open ('movies2.txt' , 'w') as my_file2:
#         for line in my_file:
#             my_file2.write(line)


