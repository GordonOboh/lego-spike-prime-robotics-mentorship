---
layout: default
title: 2025-2026 — Driving Base with Gripper
---

# 2025-2026 — Driving Base with Gripper

A new cohort, more gender-diverse, and a project that grew from simple lessons into a game designed by the scholars themselves.

---

## The Journey

```mermaid
flowchart LR
    subgraph W1["Warm-Up"]
        A[Pass the Brick<br/>collaborative activity] --> B[Show previous year's<br/>car & line follower]
    end
    
    subgraph W2["Skill Building"]
        B --> C[Training Camp 1:<br/>Driving Around]
    end
    
    subgraph W3["Final Project"]
        C --> D[Driving Base<br/>+ Gripper]
        D --> E[Scholar suggests<br/>making a game]
        E --> F["Scholars design<br/>rules & setup"]
    end
```

### 1. Pass the Brick

I started the scholars with a simple collaborative activity — [Pass the Brick](https://education.lego.com/en-us/lessons/prime-extra-resources/pass-the-brick/). No complex code, just teamwork and getting comfortable with the robots. They loved it.

### 2. Inspiration from Last Year

Once they were comfortable, I showed them what the 2024-2025 cohort had built — the RC car and the line-following robot. They saw where this was headed and were eager to get there.

### 3. Training Camp 1: Driving Around

We worked through [Training Camp 1 — Driving Around](https://education.lego.com/en-us/lessons/prime-competition-ready/training-camp-1-driving-around/), a structured lesson on controlling a driving base. They picked it up fast, and I made sure to acknowledge every win — the first straight line, the first turn without crashing.

### 4. Driving Base + Gripper

The final project: combining a driving base with a gripper. Not just moving, but interacting — grabbing, carrying, and manipulating objects.

---

## Programs

### `DriveBase_1.py`

Xbox controller-controlled driving base with gripper, built with Pybricks.

**Hardware setup:**
- Left motor: Port C (counterclockwise)
- Right motor: Port D
- Gripper motor: Port E
- Drive base: 56mm wheels, 112mm axle track

<img src="xbox_1.png" width="400" alt="Xbox controller button layout">

*Xbox controller button layout*

**Control flow:**

```mermaid
flowchart LR
    subgraph Input["Controller"]
        Triggers["Triggers L/R<br/>forward/reverse"]
        Joysticks["Joysticks L/R<br/>steering"]
        Buttons["A | B | X | Y<br/>DPad Up/Down"]
    end
    
    subgraph Logic["Logic"]
        Turbo["trim_or_turbo()<br/>A=100% | Y=25% | else=75%"]
        Trim["transmission_manual()<br/>DPad Up/Down adjusts<br/>speed trim (0-7)"]
        Gripper["gripper()<br/>B=close | X=open<br/>experimental: stall-detection"]
    end
    
    subgraph Output["Output"]
        Drive["DriveBase.drive()<br/>speed + steering"]
        Rumble["Controller.rumble()<br/>trigger feedback"]
        Display["Hub display<br/>shows trim level"]
    end
    
    Triggers --> Trim
    Joysticks --> Drive
    Buttons --> Turbo
    Buttons --> Gripper
    Turbo --> Drive
    Trim --> Drive
```

**Features:**
- **Transmission**: D-pad up/down adjusts speed trim (0-7), shown on hub display
- **Gripper modes**: "sure" (position-targeted) and "experimental" (stall-detected with rumble feedback)
- **Rumble feedback**: Triggers vibrate based on forward/reverse power
- **Multiple shutdown buttons**: Center, View, Menu, Guide, Upload, LB, RB all shut down the hub
- **Trim/Turbo**: Same system as previous year — A for full power, Y for 25%, default 75%

---

## The Game

After adding the gripper, one of the scholars suggested turning it into a **game**. I showed them how to set up the controllers, then stepped back and let them figure out the rules and the setup themselves. They owned it from there.

<img src="driving-base-gripper/images/IMG_7742.jpg" width="600" alt="Scholars testing and setting up the game">
<img src="driving-base-gripper/images/IMG_7744.jpg" width="600" alt="Section of the game field">

*Scholars setting up the game*

### Driving Base with Gripper Test

{::nomarkdown}<video src="driving-base-gripper/videos/IMG_7536.mp4" width="600" controls></video>{:/nomarkdown}

*Testing the drive base with gripper*

### Game Play

{::nomarkdown}<video src="driving-base-gripper/videos/IMG_7743.mp4" width="600" controls></video>{:/nomarkdown}

*Scholars trying out the game*

### Drawing with the Robot

{::nomarkdown}<video src="driving-base-gripper/videos/IMG_9262.mp4" width="600" controls></video>{:/nomarkdown}

*Drawing with the robot*

---

## Showcase

Staff, parents, and scholars from other schools came to see the game and robot built by the Robotics scholars.

<img src="showcase/images/IMG_9401.jpg" width="600" alt="Visitors engaging with the project">
<img src="showcase/images/IMG_9406.jpg" width="600" alt="Visitors engaging with the project">
<img src="showcase/images/IMG_9407.jpg" width="600" alt="Visitors engaging with the project">
<img src="showcase/images/IMG_9408.jpg" width="600" alt="Visitors engaging with the project">
<img src="showcase/images/IMG_9409.jpg" width="600" alt="Visitors engaging with the project">

*Visitors engaging with the project at the showcase*
