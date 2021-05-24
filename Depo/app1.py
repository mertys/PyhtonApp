# import csv

# with open('data.csv', 'r' , encoding='utf-8') as f:
#     read_csv = csv.reader(f)
    
#     for friend_data in list(read_csv)[]:
#             name = friend_data[0]
#             age = friend_data[1]
#             gender = friend_data[2]
            
#             print(f'Name: {name} -  Age: {age} - Gender: {gender}')

import csv

with open('dt.csv', 'r' , encoding='utf-8') as f, open('dt2.csv', 'w' , encoding='utf-8',newline='') as f2: 
    read_csv = csv.reader(f , delimiter = ',')
    write_csv = csv.writer(f2 , delimiter = '@')

    for friend_data in read_csv:
        del friend_data[2]
        write_csv.writerow(friend_data)
