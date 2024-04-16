import time, math, random

player_attack = 1
player_defense = 0
player_health = 3
ruppee = 0
sleutel = False
bom = 0
naar_kamer_3_8 = ''
naar_kamer_3_6 = ''
naar_kamer_12_4 = ''
kies_kamer = ''
kies_kamer_3 = ''
kies_kamer_7 = ''


# === [kamer 1] === #
print('Door de twee grote deuren loop je een gang binnen.')
print('Het ruikt hier muf en vochtig.')
print('Je ziet een deur voor je.')
print('')
time.sleep(1)

# === [kamer 7] === #
print('Je loopt de kamer in en vind je een ruppee')
kans_ruppee = random.randint(1, 10)
if kans_ruppee == 1:
    print('helaas is er geen ruppee in de kamer')
else:
    print('hoppaa! je hebt een ruppee gevonden.')    
    ruppee += 1

kies_kamer_7 = input("naar welke kamer ga je? 2 of 8?")

# === [kamer 2] === #
if kies_kamer_7 == '2':
    print('Je stapt door de deur heen en je ziet een standbeeld voor je.')
    print('Het standbeeld heeft een sleutel vast.')
    print('Op zijn borst zit een numpad met de toesten 9 t/m 0.')
    num1 = random.randint(10, 25)
    num2 = random.randint(-5, 75)
    print(f'Daarboven zie je een som staan {num1} + {num2}')
    antwoord = int(input('Wat toest je in?'))

    if antwoord == num1 + num2:
        print('je hebt een ruppee gevonden')
        ruppee += 1
    else:
        print('Er gebeurt niets....')

    print('Je zie een deur achter het standbeeld.')
    print('')
    time.sleep(1)

    kies_kamer = input("naar welke kamer ga je? 6 of 8?")

# === [kamer 6] === #
if kies_kamer_7 == '2':
    if kies_kamer == '6':
        zombie_attack = 1
        zombie_defense = 0
        zombie_health = 2
        print('je loopt de kamer binnen.')
        print('Je loopt tegen een zombie aan.')

        zombie_hit_damage = (zombie_attack - player_defense)
        if zombie_hit_damage <= 0:
            print('Jij hebt een te goede verdedigign voor de zombie, hij kan je geen schade doen.')
        else:
            # Bereken het aantal aanvallen dat de zombie nodig heeft om de speler te verslaan (zombie_attack_amount)
            zombie_attack_amount = math.ceil(player_health / zombie_hit_damage)
            
            # Bereken de schade die de speler kan toebrengen (player_hit_damage)
            player_hit_damage = (player_attack - zombie_defense)
            # Bereken het aantal aanvallen dat de speler nodig heeft om de zombie te verslaan (player_attack_amount)
            player_attack_amount = math.ceil(zombie_health / player_hit_damage)

        # Als player_attack_amount kleiner is dan zombie_attack_amount:
            if player_attack_amount < zombie_attack_amount:
                # Verminder player_health met de totale schade van de zombie
                player_health -= zombie_attack_amount * zombie_hit_damage
                print(f'In {player_attack_amount} rondes versla je de zombie.')
                print(f'Je health is nu {player_health}.')
                naar_kamer_3_6 = input('wil je gelijk naar kamer 3? (ja/nee)')
            else:
                print('Helaas is de zombie te sterk voor je.')
                print('Game over.')
                exit()
        print('')
        time.sleep(1)
    else:
        pass
else:
    pass


# === [kamer 8] === #
if naar_kamer_3_6 == 'nee' or kies_kamer_7 == '8':
    print('je komt een gokmachine tegen.')
    gokken = input('wil je de gokmachine gebruiken? (ja/nee)')

    if gokken.lower() == 'ja':
        try1 = random.randint(1, 6)
        try2 = random.randint(1, 6)
        totaal = try1 + try2

        print(f'je dubbelstenen hebben {try1} en {try2} gerold')

        if totaal > 7:
            ruppee *= 2
            print('mooi!! je ruppees zijn verdubbeld.')
        elif totaal < 7:
            player_health -= 1
        else:
            ruppee *= 2
            player_health -= 1

    else:
        print('helaas!')

    naar_kamer_3_8 = input('wil je gelijk naar kamer 3? (ja/nee)')

# === [kamer 9] === #
if naar_kamer_3_8 == 'nee':
    bonus = random.choice(['defence', 'health'])

    if bonus == 'defence':
        player_defense += 1
    else:
        player_health += 2

else:
    pass

# === [kamer 3] === #
print(f"Je kan nu items kopen. je hebt {ruppee} ruppees:")
print('elk item kost 1 ruppee')
if ruppee > 0:
    koop_sleutel = input('wil je de sleutel kopen?(ja/nee)')
    if koop_sleutel == 'ja':
        sleutel = True
        ruppee -= 1
    items = ['schild', 'bom',]
    if ruppee >= 2:
        item = input("wilt u een bom en schild kopen?(ja/nee)")
        if item == 'ja':
            player_attack += 2
            player_defense += 1
            ruppee -= 2
            bom += 1
            item = 'bom en schild'

        else:
            item = input("wilt u een bom of schild kopen?")
            if item == 'bom':
                player_attack += 2
                ruppee -= 1
                bom += 1
            else:
                player_defense += 1
                ruppee -= 1
            

    elif ruppee > 0:
        item = input("wilt u een bom of schild kopen?")
        if item == 'bom':
            player_attack += 2
            ruppee -= 1
            bom += 1
        else:
            player_defense += 1
            ruppee -= 1
    else:
        print('Helaas je hebt 0 ruppees je kan niks meer kopen')
else:
    print('Helaas je hebt 0 ruppees je kan niks kopen')

print('je komt eem deur tegen. Je duwt hem open en stap een hele lange kamer binnen.')
print(f'In deze kamer staat een tafel er is iets op de tafel.')
print(f'Je pakt het op en houdt het bij je.')
print('Op naar de volgende deur.')
print('')
time.sleep(1)
if bom > 0:
    kies_kamer_3 = input('wil je naar kamer 4 of 11 of de hek opblazen en naar 13?')
else:
    kies_kamer_3 = input('wil je naar kamer 4 of 11')

# === [kamer 13] === #
if kies_kamer_3 == '13':
    print('je loopt de kamer binnen en vindt de zwaard')
    print('je pakt hem op')
    player_attack += 2

else:
    pass

# === [kamer 4] === #
if kies_kamer_3 == '4':
    monster_attack = 2
    monster_defense = 0
    monster_health = 3

    print('Je loopt tegen een monster aan.')

    monster_hit_damage = (monster_attack - player_defense)
    if monster_hit_damage <= 0:
        print('Jij hebt een te goede verdediging voor de monster, hij kan je geen schade doen.')
    else:
        # Bereken het aantal aanvallen dat de monster nodig heeft om de speler te verslaan (monster_attack_amount)
        monster_attack_amount = math.ceil(player_health / monster_hit_damage)
        
        # Bereken de schade die de speler kan toebrengen (player_hit_damage)
        player_hit_damage = (player_attack - monster_defense)
        # Bereken het aantal aanvallen dat de speler nodig heeft om de monster te verslaan (player_attack_amount)
        player_attack_amount = math.ceil(monster_health / player_hit_damage)

        # Als player_attack_amount kleiner is dan monster_attack_amount:
        if player_attack_amount < monster_attack_amount:
            # Verminder player_health met de totale schade van de monster
            player_health -= monster_attack_amount * monster_hit_damage
            print(f'In {player_attack_amount} rondes versla je de monster.')
            print(f'Je health is nu {player_health}.')
        else:
            print('Helaas is de monster te sterk voor je.')
            print('Game over.')
            exit()
    print('')
    time.sleep(1)
    naar_kamer_12_4 = input('wil je naar kamer 12 of 10?')
else:
    pass

# === [kamer 12] === #
if naar_kamer_12_4 == '12':
    print('je loopt de kamer in de val je in een put!!')
    print('je bent dood.')
    print('Game over.')
    exit()

else:
    pass

# === [kamer 11] === #
print('je loopt de kamer binnen. Deze kamer zit vol met pijlen die uit de muur schieten')
if player_defense < 0:
    print('helaas heb je geen schild om je zelf te beschermen')
    print('Game over!')
else:
    print('bescherm je zelf met je schild!')
    time.sleep(1)
    print('yeehh! je hebt de kamer levend gepasseerd.')
    print('op naar de volgende kamer')


# === [kamer 10] === #
boss_attack = 3
boss_defense = 1
boss_health = 5

print('Je loopt tegen een nieuwe monster aan (the boss).')

boss_hit_damage = (boss_attack - player_defense)
# Bereken de schade die de speler kan toebrengen (player_hit_damage)
player_hit_damage = (player_attack - boss_defense)

if boss_hit_damage <= 0:
    print('Jij hebt een te goede verdediging voor de monster, hij kan je geen schade doen.')
else:
    if player_hit_damage == 0:
        print('Je hebt geen genoeg kracht.')
        print('Game over.')
        exit()


# Bereken het aantal aanvallen dat de monster nodig heeft om de speler te verslaan (monster_attack_amount)
boss_attack_amount = math.ceil(player_health / boss_hit_damage)

# Bereken het aantal aanvallen dat de speler nodig heeft om de monster te verslaan (player_attack_amount)
player_attack_amount = math.ceil(boss_health / player_hit_damage)

# Als player_attack_amount kleiner is dan monster_attack_amount:
if player_attack_amount < boss_attack_amount:
    # Verminder player_health met de totale schade van de monster
    player_health -= boss_attack_amount * boss_hit_damage
    print(f'In {player_attack_amount} rondes versla je de monster.')
    print(f'Je health is nu {player_health}.')
else:
    print('Helaas is de boss te sterk voor je.')
    print('Game over.')
    exit()
print('')
time.sleep(1)

# === [kamer 5] === #
print('Voorzichtig open je de deur, je wilt niet nog een zombie tegenkomen.')
print('Tot je verbazing zie je een schatkist in het midden van de kamer staan.')
print('Je loopt er naartoe.')
if sleutel:
    print('Met de sleutel die je hebt gevonden open je de schatkist. Gefeliciteerd je hebt gewonnen!!!!')
else:
    print('Je hebt helaas geen sleutel om de schatkist te kunnen openen. je hebt verloren :(')