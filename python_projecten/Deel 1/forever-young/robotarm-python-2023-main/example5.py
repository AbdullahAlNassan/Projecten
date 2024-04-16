from RobotArm import RobotArm

robotArm = RobotArm('exercise 5')

# Jouw python instructies zet je vanaf hier:
for _ in range(7):
    robotArm.moveRight()

for _ in range(7):
    for a in [robotArm.grab, robotArm.moveRight, robotArm.drop, robotArm.moveLeft, robotArm.moveLeft]:
        a()

robotArm.grab()
robotArm.moveRight()
robotArm.drop()


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()