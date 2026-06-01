from controller import Robot

robot = Robot()

TIME_STEP = 32
MAX_SPEED = 6.28

# ======================================
# Motors
# ======================================
left_motor = robot.getDevice('left wheel motor')
right_motor = robot.getDevice('right wheel motor')

left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))

left_motor.setVelocity(0.0)
right_motor.setVelocity(0.0)

# ======================================
# Sensors
# ======================================
ps = []

for i in range(8):
    sensor = robot.getDevice(f'ps{i}')
    sensor.enable(TIME_STEP)
    ps.append(sensor)

# ======================================
# Main Loop
# ======================================
while robot.step(TIME_STEP) != -1:

    values = [sensor.getValue() for sensor in ps]

    # Front detection
    front_wall = max(values[0], values[7])

    # Right wall detection
    right_wall = values[1]

    # ======================================
    # Default forward speed
    # ======================================
    left_speed = 4.0
    right_speed = 4.0

    # ======================================
    # RIGHT WALL FOLLOWING LOGIC
    # ======================================

    # FRONT WALL -> TURN LEFT
    if front_wall > 90:

        print("Front Wall -> Turn Left")

        left_speed = -2.0
        right_speed = 4.0

    # TOO CLOSE TO RIGHT WALL
    elif right_wall > 85:

        print("Too Close -> Adjust Left")

        left_speed = 3.0
        right_speed = 4.5

    # FOLLOW RIGHT WALL
    elif right_wall > 70:

        print("Following Right Wall")

        left_speed = 4.5
        right_speed = 3.5

    # WALL ENDED -> SHARP RIGHT TURN
    else:

        print("Wall Ended -> Sharp Right")

        left_speed = 4.5
        right_speed = 1.0

    # ======================================
    # Apply Speeds
    # ======================================
    left_motor.setVelocity(left_speed)
    right_motor.setVelocity(right_speed)