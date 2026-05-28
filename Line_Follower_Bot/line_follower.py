"""Smooth Stable Line Follower for e-puck"""

from controller import Robot

robot = Robot()

TIME_STEP = 32
MAX_SPEED = 6.28

# Motors
left_motor = robot.getDevice('left wheel motor')
right_motor = robot.getDevice('right wheel motor')

left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))

left_motor.setVelocity(0.0)
right_motor.setVelocity(0.0)

# Ground sensors
left_ir = robot.getDevice('ir1')
right_ir = robot.getDevice('ir0')

left_ir.enable(TIME_STEP)
right_ir.enable(TIME_STEP)

# Threshold
BLACK_THRESHOLD = 7.0

# Memory
last_turn = "left"

while robot.step(TIME_STEP) != -1:

    left_value = left_ir.getValue()
    right_value = right_ir.getValue()

    print(f"Left: {left_value:.2f} | Right: {right_value:.2f}")

    # Default smooth forward speed
    left_speed = 0.65 * MAX_SPEED
    right_speed = 0.65 * MAX_SPEED

    # LEFT SENSOR ON BLACK
    if left_value > BLACK_THRESHOLD and right_value < BLACK_THRESHOLD:

        print("Turn Left")

        # smoother turning
        left_speed = 0.40 * MAX_SPEED
        right_speed = 0.70 * MAX_SPEED

        last_turn = "left"

    # RIGHT SENSOR ON BLACK
    elif right_value > BLACK_THRESHOLD and left_value < BLACK_THRESHOLD:

        print("Turn Right")

        # smoother turning
        left_speed = 0.70 * MAX_SPEED
        right_speed = 0.40 * MAX_SPEED

        last_turn = "right"

    # BOTH ON BLACK
    elif left_value > BLACK_THRESHOLD and right_value > BLACK_THRESHOLD:

        print("Forward")

        left_speed = 0.72 * MAX_SPEED
        right_speed = 0.72 * MAX_SPEED

    # SEARCHING
    else:

        print("Searching")

        # gentle recovery
        if last_turn == "left":

            left_speed = 0.12 * MAX_SPEED
            right_speed = 0.32 * MAX_SPEED

        else:

            left_speed = 0.32 * MAX_SPEED
            right_speed = 0.12 * MAX_SPEED

    # Apply motor speeds
    left_motor.setVelocity(left_speed)
    right_motor.setVelocity(right_speed)