# Day 02 — OR Gate

**Series:** MicroPython Digital Lab  
**Board:** ESP32 DevKit C V4  
**Simulator:** [Run on Wokwi](https://wokwi.com/projects/458769568748320769) 

---

## What is an OR Gate?

An OR gate outputs HIGH when at least one input is HIGH.  
Output is LOW only when all inputs are LOW.

---

## Truth Table

| A | B | Output |
|---|---|--------|
| 0 | 0 | 0      |
| 0 | 1 | 1      |
| 1 | 0 | 1      |
| 1 | 1 | 1      |

---

## Circuit

| Component | Details |
|-----------|---------|
| Input A | ESP32 GPIO 5 → OR gate pin A |
| Input B | ESP32 GPIO 17 → OR gate pin B |
| Output | OR gate OUT → 1k resistor → LED → GND |

---

## How it works

GPIO 5 and GPIO 17 drive the two inputs of the OR gate component.  
Inputs are given via serial monitor — type `A B` (e.g. `1 0` or `0 1`).  
The OR gate hardware handles the logic — LED turns ON when either or both inputs are HIGH.

---

## How to simulate

1. Open the Wokwi link
2. Click the play button
3. Open the serial monitor
4. Try `0 1` or `1 0` — LED turns ON
5. Try `0 0` — LED stays OFF

---

## Files

- `main.py` — MicroPython source code
- `diagram.json` — Wokwi circuit

---

## Part of

[MicroPython Digital Lab](https://github.com/kritishmohapatra/MicroPython_Digital_Lab) — simulating digital logic circuits using MicroPython on ESP32.