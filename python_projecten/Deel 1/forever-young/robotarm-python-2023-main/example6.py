from RobotArm import RobotArm

robotArm = RobotArm('exercise 6')

# Jouw python instructies zet je vanaf hier:

robotArm.moveRight()

for _ in range(3):
    for a in [robotArm.grab, robotArm.moveLeft, robotArm.drop, robotArm.moveRight]:
        a()
    
    for a in [robotArm.grab, robotArm.moveRight, robotArm.drop, robotArm.moveLeft]:
        a()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()

