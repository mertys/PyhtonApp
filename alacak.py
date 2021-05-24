import sqlite3
from pprint import pprint

connection = sqlite3.connect("Borc.db")

cursor = connection.cursor()

#cursor.execute("CREATE TABLE alacakverecek(ad TEXT , alacak INTEGER , verecek INTEGER )")

ad = input('Adı: ')
alacak = input('Alacak Miktar: ')
verecek = input('Verilecek Miktar: ')

cursor.execute("SELECT * FROM alacakverecek as b WHERE b.ad = '{}'".format(ad))
kullanıcı_verisi = cursor.fetchall()

if len(kullanıcı_verisi) > 0:
    top_alacak = int(alacak) + int(kullanıcı_verisi[0][1])
    top_vericek = int(verecek) + int(kullanıcı_verisi[0][2])
    # kullanıcıvar güncelleme işi yap
    cursor.execute("UPDATE alacakverecek SET alacak={0}, verecek={1} WHERE alacakverecek.ad='{2}'".format(top_alacak, top_vericek, ad))
    connection.commit()
else:
    # kullanıcı yok yeni kayıt oluştur
    cursor.execute(f"INSERT INTO alacakverecek VALUES('{ad}',{alacak},{verecek})")
    connection.commit()



cursor.execute("SELECT * FROM alacakverecek".format(ad))
kullanıcı_verisi = cursor.fetchall()

connection.close()

pprint(kullanıcı_verisi)