import random

hoofd_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
klein_letters = hoofd_letters.lower()
cijfers = "0123456789"
symbolen = "@#$%&_?"

hoofdL_count = random.randint(2, 6)
kleinL_count = 8
cijf_count = random.randint(4, 7)
sym_count = 3

alle_karakters = cijfers 

lengte = 24

for i in range(5):
    hoofdL = "".join(random.choices(hoofd_letters, k=hoofdL_count))
    kleinL = "".join(random.choices(klein_letters, k=kleinL_count))
    cijf = "".join(random.choices(cijfers, k=cijf_count))
    sym = "".join(random.sample(symbolen, k=sym_count))

    overgebleven_lengte = lengte - hoofdL_count - kleinL_count - cijf_count - sym_count
    overgebleven_karakters = "".join(random.choices(alle_karakters, k=overgebleven_lengte))

    wachtwoord = hoofdL + kleinL + cijf + sym + overgebleven_karakters
    wachtwoord = list("".join(random.sample(wachtwoord, len(wachtwoord)))) 

    # Een hoofdletter mag niet op de twee middelste posities staan.
    mid_index = len(wachtwoord) // 2
    while wachtwoord[mid_index - 1] in hoofd_letters or wachtwoord[mid_index] in hoofd_letters:
        wachtwoord[mid_index - 1], wachtwoord[mid_index] = random.choice(alle_karakters), random.choice(alle_karakters)

    # Het wachtwoord mag niet met een kleine letter eindigen.
    while wachtwoord[-1] in klein_letters:
        wachtwoord[-1] = random.choice(alle_karakters)

    # De speciale tekens mogen niet op de eerste of laatste positie staan
    while wachtwoord[0] in symbolen or wachtwoord[-1] in symbolen:
        wachtwoord[0] = random.choice(hoofd_letters + klein_letters + cijfers)
        wachtwoord[-1] = random.choice(hoofd_letters + klein_letters + cijfers)

    # Op de eerste 3 posities mag geen cijfer staan
    for i in range(3):
        while wachtwoord[i] in cijfers:
            wachtwoord[i] = random.choice(hoofd_letters + klein_letters + symbolen)

    print("".join(wachtwoord))




