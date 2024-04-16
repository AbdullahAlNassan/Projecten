import random

deelnemers = []

while True:

    deelneemer = input("voer een naam in:")

    if deelneemer in deelnemers:
        print("waarde is niet uniek. probeer het opnieuw")
    
    else:
        deelnemers.append(deelneemer)
        print("naam scussesvol toegevoegd")

    if len(deelnemers) >= 3:
        meer_namen = input("wil je meer namen toevoegen? (ja of nee)")

        if meer_namen == 'nee':
            break

nogos = [['Jan','Abdullah'],['Rudi','Jeroen'],['Rudi','Jan']]

while True:
    lootjes = list(deelnemers)
    random.shuffle(lootjes)
    eigen_lootje = True

    for i in range(len(deelnemers)):
        if deelnemers[i] == lootjes[i]:
            eigen_lootje = False
            break

    
    if eigen_lootje:
        break
    

for i in range(len(deelnemers)):
    print(f"{deelnemers[i]} koopt voor: {lootjes[i]}")