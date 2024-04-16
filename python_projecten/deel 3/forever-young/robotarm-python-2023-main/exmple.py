from RobotArm import RobotArm

robotArm = RobotArm('exercise 9')

for a in range(1, 5):
    for i in range(a):
        for _ in range(a):
            robotArm.grab()
            for b in range(5): robotArm.moveRight()
            robotArm.drop()
            for c in range(4): robotArm.moveLeft()
        if i < a - 1:
            for _ in range(5): robotArm.moveRight()  # Verplaats de stapel vijf stappen naar rechts

robotArm.wait()



