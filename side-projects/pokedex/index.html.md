# Pokedex

> A handheld Raspberry Pi object-recognition side project with a camera, display, speaker, and browseable detection history.

Canonical page: https://dragutinoreski.com/side-projects/pokedex/

Source repository: https://github.com/dragutin-oreski/pokedex

Creator: Dragutin Oreški

## Summary

The goal was to build a device that looks like a Pokedex and works like one: point it at something, press a button, and it tells you what it is. It is battery-powered, carryable, and designed to work without a laptop in the loop.

The classifier runs only on demand when the trigger button is pressed, so the device does not spam itself with every frame. New detections are saved to a local "seen" list that can be browsed later with side buttons. There is also a small joke baked in: when it sees a dog, it calls it "bobi".

## Hardware

- Brain: Raspberry Pi 4.
- Eyes: 8MP Raspberry Pi camera.
- Screen: 2.4 inch LCD.
- Voice: Speaker and amplifier.
- Shell: 3D-printed case.

## How It Works

1. The device boots into a low-power background screen and waits for GPIO button input.
2. Pressing the main button triggers a camera capture.
3. The captured frame runs through an OpenCV DNN object detector with a 0.6 confidence threshold.
4. For every class the device has never seen, the LCD shows a matching dex image and the speaker reads the name out loud via text-to-speech.
5. A second button browses previously recognized objects.
6. A third button resets the detection history.

## Bill of Materials

- Raspberry Pi 4 Model B: the brain.
- Pi Camera V2: the eyes.
- Waveshare LCD: the dex screen.
- Speaker: the voice.
- Adafruit amplifier: drives the speaker.
- 3D-printed shell: painted red.

## Software Notes

The repository ships the Python code that runs on the device, not the full operating-system layer. The project page recommends Q-engineering images or prebuilt wheels for Raspberry Pi OpenCV/Paddle setup.

Things to change next time:

- Print the case in red filament directly so it does not need painting.
- Widen the cylinders on the front grill so they do not clog with paint.

## Links and Credits

- Project page: https://dragutinoreski.com/side-projects/pokedex/
- Source: https://github.com/dragutin-oreski/pokedex
- Inspiration video: https://www.youtube.com/watch?v=fbpM0oHZSb4
- Sam Makes channel: https://www.youtube.com/@sammakes3512
- Co-conspirator: Ivan Kunović, https://www.linkedin.com/in/ivankunovic/
