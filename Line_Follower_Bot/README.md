# 🤖 Line Follower Robot using Webots and e-puck

## 📌 Overview

This project demonstrates a simple **Line Follower Robot** simulation using the **e-puck robot** in **Webots**.
The robot follows a black path using **IR distance sensors** and adjusts its wheel speeds accordingly.

The controller is written in **Python** and uses sensor readings to detect the line position and steer the robot.

---

# ✨ Features

* Line following using IR sensors
* Differential drive control
* Real-time sensor monitoring
* Implemented in Python
* Simulated in Webots using the e-puck robot

---

# 🛠️ Technologies Used

* Webots R2025a
* Python
* e-puck Robot
* IR Distance Sensors

---

# ⚙️ Working Principle

The robot continuously reads values from:

* Left IR Sensor (`ir0`)
* Right IR Sensor (`ir1`)

## 🔍 Logic

* If the left sensor detects the line:

  * Robot turns left
* If the right sensor detects the line:

  * Robot turns right
* Otherwise:

  * Robot moves forward

The wheel velocities are adjusted dynamically to keep the robot aligned with the path.

---

# 📂 Project Structure

```bash
my_project/
│
├── controllers/
│   └── line_follower/
│       └── line_follower.py
│
├── worlds/
│   └── line_follower.wbt
│
└── README.md
```

---

# 📡 Sensors Used

| Sensor | Purpose                   |
| ------ | ------------------------- |
| IR0    | Detect left side of line  |
| IR1    | Detect right side of line |

---

# 🚗 Motor Control

The robot uses:

* Left wheel motor
* Right wheel motor

Motor speed changes based on sensor values to maintain line tracking.

---

# 💻 Sample Console Output

```bash
left: 6.56 right: 6.56
Go left
Go right
```

---

# ▶️ How to Run

1. Open **Webots**
2. Load the project world:

   ```bash
   worlds/line_follower.wbt
   ```
3. Run the simulation
4. The e-puck robot will start following the line automatically

---

# 🚀 Future Improvements

* PID-based line following
* Obstacle avoidance
* Multi-sensor line tracking
* Speed optimization
* Intersection detection

---

# 👨‍💻 Author

**Dipendra Teli**
Electrical and Electronics Engineering Student
Aditya College of Engineering and Technology
