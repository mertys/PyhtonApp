from member import Member

member_1 = Member('Mert')

member_1.add_book('1Q84' , 'Haruki Murakami')
member_1.add_book('İnce Memed' , 'Yaşar Kemal' )
member_1.add_book('Bir Gün Tek Başına' , 'Vedat Türkali')


member_1.save_to_file()