from RobotArm import RobotArm

robotArm = RobotArm('exercise 3')


for i in range(2, 9, 2):
    robotArm.grab()
    for _ in range(i): robotArm.moveRight()
    robotArm.drop()
    for _ in range(i): robotArm.moveLeft()

# Na jouw code wachten tot het sluiten van het window:
robotArm.wait()
