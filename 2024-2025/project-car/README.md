---
layout: default
title: Project Car
---

# Project Car — LEGO SPIKE Prime RC Car

A LEGO SPIKE Prime car inspired by a TikTok video of someone's project car. Built by a group of robotics scholars under my guidance for a school showcase.

## Programs

### `car_devine.py`
Enhanced RC car with:
- **Two scholar modes**: "good" (ultrasonic sensor on port C, green light) and "experiment" (no ultrasonic, red light)
- **Headlamp control**: 4 modes via D-pad — Off, Front lights, Back lights, All lights
- **Obstacle warning**: Ultrasonic sensor triggers controller rumble when within 100cm (intensity increases as distance decreases)
- **Port auto-detection**: Scans ports for connected devices on startup

### Control Flow

```mermaid
flowchart LR
    subgraph Input["Controller Inputs"]
        Triggers["Triggers (L/R)"]
        Joysticks["Joysticks (L/R)"]
        DPad["D-Pad"]
        Buttons["A / Y / Menu"]
    end

    subgraph Processing["Processing"]
        Drive["drive_power = Right - Left<br/>(forward / reverse)"]
        Steer["steer = joystick_left.x + joystick_right.x<br/>clamped to ±100"]
        Turbo["trim_or_turbo()<br/>A=100% | Y=25% | else=75%"]
        Headlamps["headlamps(dpad)<br/>toggle Off/Front/Back/All"]
        Obstacle["obstacle_warning()<br/>distance < 100cm → rumble"]
    end

    subgraph Output["Robot Output"]
        Motors["Drive Motor (Port E)<br/>Steer Motor (Port A)"]
        Lights["Ultrasonic Sensor LEDs<br/>(headlamps)"]
        Rumble["Controller Rumble<br/>(haptic feedback)"]
    end

    Triggers --> Drive
    Joysticks --> Steer
    Buttons --> Turbo
    Drive --> Turbo
    Turbo --> Motors
    Steer --> Motors
    DPad --> Headlamps
    Headlamps --> Lights
    Obstacle --> Rumble
```

## Build Process

| Stage | Image |
|-------|-------|
| Early build — rear wheel drive and gear setup | <img src="images/IMG_5153.jpg" width="300"> <img src="images/IMG_5155.jpg" width="300"> <img src="images/IMG_5156.jpg" width="300"> |
| Driving motor close-up | <img src="images/IMG_5154.jpg" width="300"> |
| Almost complete — waiting on ultrasonic sensors (headlights) | <img src="images/IMG_5152.jpg" width="300"> |
| Finished robot | <img src="images/IMG_5157.jpg" width="300"> |

## Videos

### Headlight Demo
Ultrasonic sensor headlight demo — 4 modes: Off, Low, High, All.

<video src="videos/IMG_4618 (2).mp4" width="600" controls></video>

*Headlight demo*

### Racing
Students racing the finished cars.

<video src="videos/IMG_5159.mp4" width="600" controls></video>

*Scholars racing the finished cars*

## Reference

Screenshots from the TikTok video that inspired the build — an IRL project car suggested by a scholar.

<img src="reference/Screenshot%202025-03-10%20232014.png" width="400">
<img src="reference/Screenshot%202025-03-10%20232034.png" width="400">
<img src="reference/Screenshot%202025-03-10%20231940.png" width="400">

*Design inspiration from TikTok/YouTube*
