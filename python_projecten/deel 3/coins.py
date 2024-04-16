
# naam student: Abdullah Al Nassan
# studentnummer: 99077332
# doel van het programma: 
# functie van het programma:
# structuur van het programma:

te_betalen_bedrag = int(float(input('Te betalen bedrag: ')) * 100)
betaald_bedrag = int(float(input('Betaald bedrag: ')) * 100)
wisselgeld = betaald_bedrag - te_betalen_bedrag
if wisselgeld > 0:
    munt_waarde = 500
    while wisselgeld > 0 and munt_waarde > 0:
        aantal_munten = wisselgeld // munt_waarde
        if aantal_munten > 0:
            print(f'Geef maximaal {aantal_munten} munt(en) van {munt_waarde / 100} euro terug!')
            aantal_teruggegeven_munten = int(input(f'Hoeveel munten van {munt_waarde / 100} euro heb je teruggegeven? '))
            wisselgeld -= aantal_teruggegeven_munten * munt_waarde
        if munt_waarde == 500:
            munt_waarde = 200
        elif munt_waarde == 200:
            munt_waarde = 100
        elif munt_waarde == 100:
            munt_waarde = 50
        elif munt_waarde == 50:
            munt_waarde = 20
        elif munt_waarde == 20:
            munt_waarde = 10
        elif munt_waarde == 10:
            munt_waarde = 5
        elif munt_waarde == 5:
            munt_waarde = 2
        elif munt_waarde == 2:
            munt_waarde = 1
        else:
            munt_waarde = 0
if wisselgeld > 0:
    print(f'Wisselgeld niet teruggegeven: {wisselgeld / 100} euro')
else:
    print('Klaar')