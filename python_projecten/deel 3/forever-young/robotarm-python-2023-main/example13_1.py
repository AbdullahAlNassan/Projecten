from RobotArm import RobotArm

robotArm = RobotArm()
robotArm.randomLevel(1, 7)

for i in range(7):
    robotArm.grab()
    block = robotArm.scan() 
    if block:
        for _ in range(1 + i):
            robotArm.moveRight()
        robotArm.drop()
        for _ in range(1 + i):
            robotArm.moveLeft()
    else:
        robotArm.wait()
