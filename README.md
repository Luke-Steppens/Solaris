
This readme exists in its origional form from uni module COMP209 and will be edited down asap








# Solaris – Gesture-Controlled Interactive Light Sculpture

Solaris is a responsive, gesture-controlled light installation that uses real-time computer vision and robotic movement to create an interactive visual experience. Built for the COMP209 university group project, Solaris brings together elements of mechanical design, embedded systems, and computer vision. The system detects hand gestures and translates them into precise servo movements, allowing users to manipulate beams of light as they pass through rotating prisms and glass orbs.

---

## Project Overview
<p align="center">
  <img src="https://github.com/Luke-Steppens/Solaris/blob/main/Media/Photos/WhatsApp%20Image%202026-08-04%20at%2006.53.04.jpeg?raw=true" width="650">
</p>


<p align="center">
  <img src="https://github.com/Luke-Steppens/Solaris/blob/main/Media/Photos/WhatsApp%20Image%202026-08-04%20at%2006.54.34.jpeg?raw=true" width="650">
</p>




Solaris enables users to interact with beams of light that refract through prisms and orbs, which are mechanically rotated by a robotic system in response to hand movements. The system leverages hand tracking, servo-controlled articulation, and custom-designed 3D-printed components to create a visually dynamic installation.

---

## Team Members and their development logs

<p align="center">
  <img src="https://github.com/Luke-Steppens/Solaris/blob/main/Media/Photos/WhatsApp%20Image%202026-08-04%20at%2007.07.57.jpeg?raw=true" width="650">
</p>

- **Adithi Jayaraman** - https://www.notion.so/COMP209-1820f7ecc39f8019a431de44047871cf?pvs=4
- **Dan Ward** - https://www.notion.so/COMP209-Notes-Dan-19073cfe815b80a4bc4dd21392c3a36d
- **Conor Bailie** - https://www.notion.so/COMP209-191f1daf6e6e80539bbcf3f1b4c1cee5
- **Luke Steppens** - https://www.notion.so/COMP209-Robot-Design-60538fde323a44ef86ece4d31390ee01?pvs=4

---
## Individual Contribution

For this project I was the designer of the artefact. This included fabrication of parts and the construction of the device. 


Step 1

- Design and fabricate a miniature planetary gear system and motorise it
This test configuration allowed me to highlight potential future issues and assess suitability for the project.




<img width="1280" height="720" alt="MiniPrism v24again" src="https://github.com/user-attachments/assets/90567f3b-94dd-43d6-a9dd-e7611d9f9716" />



<p align="center">
<img width="504" height="549" alt="WhatsAppVideo2026-08-04at10 07 54-ezgif com-crop" src="https://github.com/user-attachments/assets/43bb198c-a70c-4533-8953-37261362796c" />


---

Step 2

- Design primative glass mount
Creating this basic design highlighted future weight distribution concerns and glass mounting types to be attached to each planetary gear. The eventual mounts utilised the limited elasticity of PLA for an easy, secure friction fit. 
In the final piece, this part would be the hardest to finalise when went through many iterations.




<p align="center">
  
https://github.com/user-attachments/assets/e6f30164-5d48-40ff-9c3f-a2aaa589af57

---


Step 3
- Planetary gear and housing
This main housing needed to contain all gearing elements and keep balance whilst over 2KG of glass rotated within it.

<p align="center">
<img width="600" height="800" alt="WhatsApp Image 2026-08-04 at 10 32 14" src="https://github.com/user-attachments/assets/84fb9686-7f2d-4bc6-9349-bcc6acac21cc" />



---

Final Design






https://github.com/user-attachments/assets/c0ae6e90-3917-4fb3-a8e9-6cd88678b772




---








<p align="center">
  <img src="https://github.com/Luke-Steppens/Solaris/blob/main/Media/PDF%20to%20JPG/front%20&%20side_page-0001.jpg?raw=true" width="1000">
</p>


<p align="center">
  <img src="https://github.com/Luke-Steppens/Solaris/blob/main/Media/PDF%20to%20JPG/exploded%20view_page-0001.jpg?raw=true" width="1000">
</p>

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
