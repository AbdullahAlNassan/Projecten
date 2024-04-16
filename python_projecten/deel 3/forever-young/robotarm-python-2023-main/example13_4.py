from RobotArm import RobotArm

robotArm = RobotArm('democratie')

colors = {'blue': 0, 'green': 0, 'red': 0}

# Scannen en tellen van kleuren
for i in range(9):
    robotArm.moveRight()
    robotArm.grab()
    color = robotArm.scan()
    colors[color] += 1
    robotArm.drop()

# Terugkeren naar het startpunt
for _ in range(8):
    robotArm.moveLeft()

# Stacking op basis van de meest voorkomende kleur
most_common_color = max(colors, key=colors.get)

for i in range(6):
    robotArm.grab()
    for _ in range(9):
        if most_common_color == 'blue':
            robotArm.moveLeft()
        elif most_common_color == 'green':
            robotArm.moveRight()
        else:
            robotArm.moveLeft()
    robotArm.drop()
    for _ in range(8):
        if most_common_color == 'blue':
            robotArm.moveRight()
        elif most_common_color == 'green':
            robotArm.moveLeft()
        else:
            robotArm.moveRight()

# Na jouw code wachten tot het sluiten van het window:
robotArm.wait()

