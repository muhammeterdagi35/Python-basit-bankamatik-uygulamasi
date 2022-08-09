print(
    '''
    0-Çıkış
    1-Bakiye sorgulama
    2-Para çekme
    3-Para yatırma

    '''
)

bakiye = 1000
while True:
    islem = input('Bir işlem seçiniz:')
    if islem == '0':
        print('Çıkış yapıldı')
        break
    
    elif islem == '1':
        print(f'Mevcut bakiyeniz:{bakiye}')

    elif islem == '2':
        tutar = int(input('Çekmek istediğiniz tutarı giriniz:'))
        
        if bakiye - tutar < 0:
            print('Yetersiz bakiye')

        else:
            bakiye -= tutar
            print(f'Seçtiğiniz tutarı çektiniz mevcut bakyeniz: {bakiye}')

    elif islem == '3':
        tutar = int(input('Yatırmak istediğiniz tutarı giriniz:'))
        bakiye += tutar
        print(f'Seçtiğiniz tutarı yatırdınız mevcut bakyeniz: {bakiye}')

    else:
        print('Geçersiz işlem girdiniz')

    