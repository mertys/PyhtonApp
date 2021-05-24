# try:
#     num = int(input('lütfen bir sayı giriniz: '))
# except:
#     print('Girdiğiniz değer bir sayı değildir')
# else:
#     print(f'Girdiğiniz değer: {num}')
# finally:
#     print('Sıkıntısız Çalışıyor')

#  File Not Found Error

# with open ('test.txt' , 'r') as f:
#     content = f.read()

try:
    with open ('test.txt' , 'r') as f:
        content = f.read()
except FileNotFoundError:
    print('Dosya Bulunamadı.')