aantal_lijstjes = int(input("Hoeveel lijstjes wil je? "))

# Lijst om alle lijstjes op te slaan
alle_lijstjes = []

for i in range(aantal_lijstjes):
    lengte_lijstje = int(input(f"Geef de lengte van lijstje {i + 1}: "))

    lijstje = list(range(i + 1, (i + 1) * (lengte_lijstje + 1), i + 1))
    
    # Voeg het lijstje toe aan de lijst van alle lijstjes
    alle_lijstjes.append(lijstje)

print("Alle lijstjes:")
for lijstje in alle_lijstjes:
    print(lijstje)

