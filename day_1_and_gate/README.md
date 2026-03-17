# Day 01 — AND Gate

**Series:** MicroPython Digital Lab  
**Board:** ESP32 DevKit C V4  
**Simulator:** [Run on Wokwi](https://wokwi.com/projects/458750462926204929)
---

## What is an AND Gate?

An AND gate outputs HIGH only when all inputs are HIGH.  
In any other combination, the output is LOW.

---

## Truth Table

| A | B | Output |
|---|---|--------|
| 0 | 0 | 0      |
| 0 | 1 | 0      |
| 1 | 0 | 0      |
| 1 | 1 | 1      |

---

## Circuit

| Component | Details |
|-----------|---------|
| Input A | ESP32 GPIO 5 → AND gate pin A |
| Input B | ESP32 GPIO 17 → AND gate pin B |
| Output | AND gate OUT → 1k resistor → LED → GND |

---

## How it works

GPIO 5 and GPIO 17 are configured as outputs and drive the two inputs of the AND gate component.  
Inputs are given via serial monitor — type `A B` (e.g. `1 1` or `0 1`).  
The AND gate hardware handles the logic — LED turns ON only when both inputs are HIGH.

---

## How to simulate

1. Open the Wokwi link
2. Click the play button
3. Open the serial monitor
4. Type `1 1` and press Enter — LED turns ON
5. Try `1 0`, `0 1`, `0 0` — LED stays OFF

---

## Files

- `main.py` — MicroPython source code
- `diagram.json` — Wokwi circuit

---

## Part of

[MicroPython Digital Lab](https://github.com/kritishmohapatra/MicroPython_Digital_Lab) — simulating digital logic circuits using MicroPython on ESP32.