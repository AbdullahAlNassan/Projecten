from RobotArm import RobotArm

robotArm = RobotArm('exercise 8')

robotArm.moveRight()
for i in range(7):
    robotArm.grab()
    for a in range(8):
        robotArm.moveRight()
    robotArm.drop()
    for c in range(8):
        # if i > 5:
        #     robotArm.wait()
        robotArm.moveLeft()


robotArm.wait()
