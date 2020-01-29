def Minutnik(tabelagodzin,tabelaminut,k):
    i=0
    zlecialominut = 0
    while i<k:
        minuty1 = (tabelagodzin[i]*60) + tabelaminut[i]
        minuty2 = (tabelagodzin[i+1]*60) + tabelaminut[i+1]
        #print(minuty1)
        #print(minuty2)
        if (minuty1<=minuty2):
            zlecialominut+= minuty2-minuty1
        else:
            zlecialominut+= (24*60)-minuty1+minuty2

        ##wynik wtedy bedzie godz=min//60  min=min%60.
        ##no... i obliczenia mozna wrzucic do innego pliku przeciez. ten niech bedzie ladny ;)

        i+=2
    return zlecialominut