# class Human:
#     def __init__(self):
#         self.friends = []

#     def add_friends(self , friend):
#         raise NotImplementedError('Arkadaş Eklenemedi')


# human_1 = Human()
# human_1.add_friends('Mert')
# print(human_1.friends)
# human_1.add_friends('Hayri')
# print(human_1.friends)

class TypeErrorHatalar(TypeError):
    def __init__(self,message,errorcode):
        super().__init__(f'Hata Kodu: {errorcode}: {message}')
        self.errorcode = errorcode
        
friends = ['Mert','Hayri','Ayşe']

def select_best_friend(friend):
    if type(friend) is not str:
        raise TypeErrorHatalar ('Arkadaş string olmalı ', 700)
    if friend not in friends:
        raise ValueError('Arkadaş Bulunamadı')
    print(f'En İyi Arkadaşım: {friend}')

select_best_friend(True)
