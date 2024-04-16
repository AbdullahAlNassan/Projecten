from RobotArm import RobotArm

robotArm = RobotArm('exercise 4')

for _ in range(4):
    robotArm.grab()
    robotArm.moveRight()
    robotArm.moveRight()
    robotArm.drop()
    robotArm.moveLeft()
    robotArm.moveLeft()

robotArm.grab()
robotArm.moveRight()
robotArm.drop()

for _ in range(4):
    for action in [robotArm.moveRight, robotArm.grab, robotArm.moveLeft, robotArm.drop]:
        action()

# Wait until the window closes:
robotArm.wait()