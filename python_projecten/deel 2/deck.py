import random

deck = []
suits = ['Harten', 'klaveren', 'schoppen', 'ruiten']
card_values = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "boer", "vrouw", "koning"]

for suit in suits:
    for value in card_values:
        deck.append(f"{suit} {value}")

deck.extend(["joker1", "joker2"])
random.shuffle(deck)

print(f"Deck ({len(deck)} kaarten): {deck}")

for i in range(7):
    card = deck.pop(0)
    print(f"Kaart {i+1}:{card}")

print(f"Deck ({len(deck)} kaarten): {deck}")

