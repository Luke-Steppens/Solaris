
This readme exists in its origional form from uni module COMP209 and will be edited down asap








# Solaris – Gesture-Controlled Interactive Light Sculpture

Solaris is a responsive, gesture-controlled light installation that uses real-time computer vision and robotic movement to create an interactive visual experience. Built for the COMP209 university group project, Solaris brings together elements of mechanical design, embedded systems, and computer vision. The system detects hand gestures and translates them into precise servo movements, allowing users to manipulate beams of light as they pass through rotating prisms and glass orbs.

---

## Project Overview
<div align="center">
  <img src="Media/final%20render.png" alt="Final Render" width="600"/>
</div>
Solaris enables users to interact with beams of light that refract through prisms and orbs, which are mechanically rotated by a robotic system in response to hand movements. The system leverages hand tracking, servo-controlled articulation, and custom-designed 3D-printed components to create a visually dynamic installation.

---

## Team Members and their development logs

- **Adithi Jayaraman** - https://www.notion.so/COMP209-1820f7ecc39f8019a431de44047871cf?pvs=4
- **Dan Ward** - https://www.notion.so/COMP209-Notes-Dan-19073cfe815b80a4bc4dd21392c3a36d
- **Conor Bailie** - https://www.notion.so/COMP209-191f1daf6e6e80539bbcf3f1b4c1cee5
- **Luke Steppens** - https://www.notion.so/COMP209-Robot-Design-60538fde323a44ef86ece4d31390ee01?pvs=4

---

## Core Features

| Feature                     | Technology Stack                                     |
|----------------------------|------------------------------------------------------|
| **Gesture Detection**      | OpenCV & MediaPipe                                   |
| **Robotic Control**        | Arduino Uno + Servos (3 DOF robotic arm)             |
| **Inverse Kinematics**     | Custom Python logic using Law of Cosines & atan2     |
| **Standalone Execution**   | Raspberry Pi 3B with auto-executing hand tracking    |
| **Prism Control Mechanism**| Custom 3D-printed planetary gear system              |

---

## Repository Structure

```

.
├── CAD/                  # Mechanical component designs
├── Code/
│   ├── Final\_Script/     # Final working Python & Arduino scripts
│   └── Draft/            # Archived experimental code
├── Documentation/        # Technical notes, setup guides, sprint logs
├── Electronics/          
├── Media/                # Photos, renders, and demo videos
├── LICENSE
└── README.md             # This file

```

---

## Hardware Architecture

---

| **Component**                           | **Role & Function**                                                                                              |
| --------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| **Raspberry Pi 3B**                     | Main processing unit: captures webcam input, runs hand-tracking algorithms, and sends servo commands via serial. |
| **USB Webcam**                          | Captures real-time hand movements for gesture recognition using OpenCV and MediaPipe.                            |
| **Arduino Uno**                         | Interprets serial commands from the Raspberry Pi and controls servo motors accordingly.                          |
| **Raspberry Pi Pico** (early prototype) | Initially tested for direct servo control during the development phase.                                          |
| **3-DOF Robotic Arm**                   | Mechanically moves and positions optical elements based on hand gestures.                                        |
| **Glass Prisms & Orbs**                 | Optical components that bend, reflect, and scatter light, producing dynamic visual effects.                      |

---

## CAD & Mechanical Prototyping

The physical mounts were designed to hold glass orbs and prisms, with a focus on durability and smooth interaction. The final setup uses a large planetary gear system with precise gear ratios and bearing mounts.

### Prototype Timeline

#### Prototype 1: Basic Rotating Mount
- Single glass mount on a vertical shaft with bearings.
- Confirmed basic concept but suffered from poor front-weight balance.

#### Prototype 1.2: Motorised Gear Proof
- Implemented a miniature planetary gear system.
- Powered by a 3–6V DC motor via L298N H-Bridge, controlled by Arduino Uno.
- Proved gear logic and embedded housing feasibility.

#### Prototype 2: Modular Snap-Fit Design
- Reinforced spokes and improved gear tolerance.
- Orbs held via friction; prisms mounted with snap-fit.
- Reduced breakage and improved part interchangeability.

#### Final Model: Solaris Gear System
- Over 65 cm tall, featuring:
  - 3× gears (175 teeth each)
  - Outer ring gear with 525 teeth
  - Bearings and composite joints for smooth motion
- Most complex assembly; precision-critical design required iterative CAD planning.

---

## Software Pipeline

### Hand Tracking
- **MediaPipe + OpenCV**: Captures 21 hand landmarks in real time.
- Index finger (landmark 8) is used for positional tracking on the screen.
- Coordinate smoothing and Z-depth estimation included for improved accuracy.

### Arduino Communication
- Python script on Raspberry Pi sends joint angles over serial.
- Arduino Uno decodes values and adjusts servos via `Servo.h`.

---

## System Iterations

### Phase 1: Laptop-based Tracking
- Python script captured webcam feed on laptop.
- Angles computed locally and sent via serial.
- Used for validating tracking accuracy and angle mapping.

### Phase 2: ESP32-CAM
- Attempted to offload webcam + computation.
- Issues:
  - Long boot-up time
  - WiFi-dependent video feed caused jitter
  - Abandoned for real-time stability concerns

### Final Phase: Raspberry Pi 3B
- Full autonomy achieved with USB webcam and local computation.
- Auto-runs on boot via `.bashrc` and virtualenv.
- Sends data directly to Arduino Uno via `/dev/ttyUSB0`.
- Torch holder added to robotic arm for controlled light emission.

---

## Final Installation

- Mounted vertically in a dark space to emphasize light patterns.
- Gestures cause light to move and refract through prisms in real-time.
- Entire system is **plug-and-play**, no additional setup required:
  - No internet
  - No monitor
  - No manual pip installs or environment activation

---

## License

Licensed under the [Apache License 2.0](LICENSE). Free for educational and non-commercial use.

---

## Media & Demo

Demo footage and final installation images can be found in the [`Media/`](./Media/) folder.

---

## How to Run (Summary)

1. Power on Raspberry Pi 3B
2. Turn on the 12v barrty power 
3. System auto-launches hand tracking via `.bashrc`
4. Webcam captures hand motion
5. Raspberry Pi calculates joint angles
6. Angles sent to Arduino via serial
7. Arduino adjusts robotic arm and prism mount accordingly

```
