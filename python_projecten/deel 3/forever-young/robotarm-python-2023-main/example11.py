from RobotArm import RobotArm

robotArm = RobotArm('exercise 11')
for _ in range(8): robotArm.moveRight()
for i in range(8):
    robotArm.grab()
    color = robotArm.scan()
    if color == 'white':
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveLeft()
        robotArm.moveLeft()
    else:
        robotArm.drop()
        robotArm.moveLeft()

robotArm.grab()
color = robotArm.scan()
if color == 'white':
    robotArm.moveRight()
    robotArm.drop()
else:
    robotArm.drop()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
