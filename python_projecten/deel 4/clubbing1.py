# Constantes
PRIJS_COLA = 1.80
PRIJS_BIER = 2.40
PRIJS_CHAMPAGNE = 12.30

DRANKJES = ('cola', 'bier', 'champagne')
VIP_LIST = ('jeroen', 'jouke', 'rudi')

print('Welkom in de kroeg!')

leeftijd = int(input('Hoe oud ben je? '))

if leeftijd < 18:
    print('Sorry, je mag niet naar binnen.')
    print(f'Probeer het over {18 - leeftijd} jaar nog eens.')
    exit()

naam = input('Wat is je naam? ')

if naam in VIP_LIST and leeftijd >= 21:
    kleur = 'blauw'
    print(f'Je krijgt van mij een {kleur} bandje') 
elif naam in VIP_LIST and leeftijd < 21:
    kleur = 'rood' 
    print(f'Je krijgt van mij een {kleur} bandje')

if (naam not in VIP_LIST and leeftijd >= 21 ):
    print('Je krijgt van mij een stempel')

drankje = input('Wat wil je drinken? ')

if drankje not in DRANKJES:
    print('Sorry, ik weet niet wat je bedoelt. Hier is een glaasje water.')
else:
    if (drankje == 'bier' and leeftijd < 21) or (drankje == 'champagne' and naam in VIP_LIST and kleur != 'blauw'):
        print('Sorry, je mag geen alcohol bestellen onder de 21')
        print(f'Probeer het over {21 - leeftijd} jaar nog eens.')
    elif (drankje == 'bier' and leeftijd >= 21 and naam not in VIP_LIST) or (drankje == 'champagne' and naam in VIP_LIST and kleur == 'blauw') or (drankje == 'cola' and naam not in VIP_LIST):
        if drankje == 'bier':
            prijs = PRIJS_BIER
        elif drankje == 'cola':
            prijs = PRIJS_COLA
        elif drankje == 'champagne':
            prijs = PRIJS_CHAMPAGNE
        print(f'Alsjeblieft, je {drankje}, dat is dan €{prijs}')
    elif (drankje == 'bier' and naam in VIP_LIST and kleur == 'blauw') or (drankje == 'cola' and naam in VIP_LIST):
        print('Alsjeblieft complimenten van het huis')
    elif drankje == 'champagne' and naam not in VIP_LIST:
        print('Sorry, alleen vips mogen champagne bestellen.')

print('Tot ziens!')

