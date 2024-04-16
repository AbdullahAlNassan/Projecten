
from RobotArm import RobotArm

robotArm = RobotArm('soorten')

for i in range(6):
    robotArm.grab()
    color = robotArm.scan()
    if color == 'blue':
        for a in range(9 - i):
            robotArm.moveRight()
        robotArm.drop()
        if i > 4:
            robotArm.wait()
        for a in range(8 - i):
            robotArm.moveLeft()
    elif color == 'green':
        for a in range(8 - i):
            robotArm.moveRight()
        robotArm.drop()
        if i > 4:
            robotArm.wait()
        for a in range(7 - i):
            robotArm.moveLeft()
    else:
        for j in range(7 - i):
            robotArm.moveRight()
        robotArm.drop()
        if i > 4:
            robotArm.wait()
        for a in range(6 - i):
            robotArm.moveLeft()


