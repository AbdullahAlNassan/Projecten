def vertaal_tekst(tekst, woordenboek):
    woorden = tekst.split()
    vertaalde_tekst = []

    for woord in woorden:
        print(woord)
        vertaal_woord = woordenboek.get(woord, woord)
        vertaalde_tekst.append(vertaal_woord)

    return ' '.join(vertaalde_tekst)

vertaalwoorden = {
    'hart': 'heart',
    'auto': 'car',
    'werk': 'work',
    'hond': 'dog',
    'vader': 'father',
    'tas': 'bag',
}

input_tekst = input("Voer een stukje tekst in: ")

vertaalde_tekst = vertaal_tekst(input_tekst, vertaalwoorden)

print("Vertaalde tekst:")
print(vertaalde_tekst)
