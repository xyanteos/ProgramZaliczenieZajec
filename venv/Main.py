##############ZADANIE B: posumowac czas z linii pliku (ulatwienie - tylko jeden czas w wierszu pliku).
######## Maciej N. indeks:37920
##godziny mamy wygenerowane w pliku Liczby.txt kazda linijka to nowa liczba ( godzina ) w formacie 00:00.
##zakladam, ze kazda para godzin to okres "pracy" od-do.
# Trzeba je zsumowac. (osobno godziny i minuty) i zrobic godziny+= minuty mod 60, a reszte minut wypluc na koniec.
import GeneratorGodzin
import WyliczMinuty
#wprowadzamy ilosc godzin, jaka ma wytworzyc program i upewniamy sie ze nie wykrzaczy
k = input('ile godzin ma wygenerowac i policzyc program? - liczba musi byc parzysta.')
try:
    k = int(k)
    if k%2 !=0 :
        print('Liczba miala byc parzysta!')
        exit()
except Exception as e:
    print(e)
    exit()

#wykorzystujemy (tj.) "generator" wypisany w innym pliku pythonowskim ( w innym programie z projektu )
GeneratorGodzin.wygeneruj(k)
#tworze tutaj jakies wartosci, ktore pozniej sie przydadza podczas zliczania godzin
godziny = 0
minuty = 0
tabelagodzin = []
tabelaminut = []

#Wczytujemy wartosci godzin i minut z pliku Liczby.txt
for line in open('Liczby.txt','r'):
    godziny+=int(line[:2])
    minuty+=int(line[-3:])
    tabelagodzin.append(int(line[:2]))
    tabelaminut.append(int(line[-3:]))
i=0
#funkcja zliczania minut wypisana w pliku WyliczMinuty.py
zlecialominut = WyliczMinuty.Minutnik(tabelagodzin,tabelaminut,k)
#tutaj dodaje wartosci godzinowe (pracy) jesli minuty przekroczyly 60
godzinyPracy = zlecialominut//60
minutyPracy=zlecialominut%60
print('godziny pracy : '+ str(godzinyPracy) + ' Minuty pracy : ' + str(minutyPracy))
#tutaj dodaje wartosci godzinowe jesli minuty przekroczyly 60
godziny+=minuty//60
minuty = minuty%60
print('suma wszystkich wypisanych godzin : {0} godzin, {1} minut'.format(godziny,minuty))


##\/ Ponizej wczesniejsza próba ale latwiej zamieniajac na minuty : {min1=godz1*60+minuty1} {min2=godz2*60+minuty2} {min1<=min2 : min=min2-min1} ; {min1>min2: min=24*60-min1+min2}
   ##nieudana (?) proba \/
    #if (tabelagodzin[i]<=tabelagodzin[i+1]):
#        if (tabelaminut[i]<=tabelaminut[i+1]):
#            minutyPracy+= tabelaminut[i+1]+tabelaminut[i]
#            godzinyPracy+= tabelagodzin[i+1]-tabelagodzin[i]
#        else:
#            minutyPracy+= 60-tabelaminut[i]+tabelaminut[i+1]
#            godzinyPracy+= tabelagodzin[i+1]-tabelagodzin[i]-1
#    else:
#        if (tabelaminut[i]<=tabelaminut[i+1]):
#            minutyPracy+= tabelaminut[i+1] - tabelaminut[i]
#            godzinyPracy += 24 - tabelagodzin[i] + tabelagodzin[i+1]
#        else:
#            minutyPracy+= 60-tabelaminut[i]+tabelaminut[i+1]
#            godzinyPracy+= 24-tabelagodzin[i]-1+tabelagodzin[i+1]
