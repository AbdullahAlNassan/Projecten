from RobotArm import RobotArm

robotArm = RobotArm('exercise 7')

for a in range(5):
    for _ in range(6): robotArm.moveRight(), robotArm.grab(), robotArm.moveLeft(), robotArm.drop()

    if a < 4: robotArm.moveRight(), robotArm.moveRight()

robotArm.wait()

