# Day 03 — NOT Gate

**Series:** MicroPython Digital Lab  
**Board:** ESP32 DevKit C V4  
**Simulator:** [Run on Wokwi](https://wokwi.com/projects/458828728113140737)  

---

## What is a NOT Gate?

A NOT gate inverts the input — HIGH becomes LOW and LOW becomes HIGH.  
It is also called an inverter.

---

## Truth Table

| A | Output |
|---|--------|
| 0 | 1      |
| 1 | 0      |

---

## Circuit

| Component | Details |
|-----------|---------|
| Input A | ESP32 GPIO 5 → NOT gate pin A |
| Output | NOT gate OUT → 1k resistor → LED → GND |

---

## How it works

GPIO 5 drives the input of the NOT gate component.  
Input is given via serial monitor — type `A` (e.g. `1` or `0`).  
The NOT gate hardware handles the logic — LED turns ON when input is LOW, OFF when input is HIGH.

---

## How to simulate

1. Open the Wokwi link
2. Click the play button
3. Open the serial monitor
4. Type `0` — LED turns ON
5. Type `1` — LED turns OFF

---

## Files

- `main.py` — MicroPython source code
- `diagram.json` — Wokwi circuit

---

## Part of

[MicroPython Digital Lab](https://github.com/kritishmohapatra/MicroPython_Digital_Lab) — simulating digital logic circuits using MicroPython on ESP32.