import random

def wygeneruj(ile):
    #jesli jakims cudem pomimo zabezpieczen w pliku Main dostanie sie do tej funkcji liczba nieparzysta,
    #to program wyjdzie z funkcji.
    if ile%2!=0:
        exit()
    fo = open('Liczby.txt','w')
    ilosc = ile
    ##tworzenie (ile) roznych linijek z godzinami, kazda para godzin w jednej linijce zeby bylo latwiej porownac
    for i in range(ilosc):
        godziny1 = str(random.randint(0,23))
        minuty1 = str(random.randint(0,59))
        if int(minuty1)<10 :
            minuty1 = '0'+minuty1
        if int(godziny1)<10 :
            godziny1 = '0'+godziny1
        fo.write('{0}:{1}\n'.format(godziny1,minuty1))
    fo.close()

###odczytanie tych liczb ( godzin )
#for line in open('Liczby.txt','r'):
#    print(line)