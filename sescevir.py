from gtts import gTTS
import os
from os import path

def dosyavarmi(dosya):
    return path.exists(dosya)

dosya = open("ss.txt" , encoding="utf-8")
yazi = dosya.read()
cikti = gTTS(text=yazi, lang="tr" , slow=False)
if dosyavarmi("SS.mp3"):
    print("Seslendiriliyor..")
    os.system("SS.mp3")
else:
    print("Dosya Oluşturuluyor..")
    cikti.save("SS.mp3")
    print("Seslendiriliyor..")
    os.system("SS.mp3")
dosya.close()
