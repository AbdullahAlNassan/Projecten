from RobotArm import RobotArm

robotArm = RobotArm('exercise 10')

for g in range(0, 10, 2):
    robotArm.grab()
    for _ in range(9 - g):
         robotArm.moveRight()
    robotArm.drop()
    for _ in  range(8 - g):
         robotArm.moveLeft()


robotArm.wait()
