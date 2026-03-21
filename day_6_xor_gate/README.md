# Day 06 — XOR Gate

**Series:** MicroPython Digital Lab  
**Board:** ESP32 DevKit C V4  
**Simulator:** [Run on Wokwi](https://wokwi.com/projects/459108592904037377) 

---

## What is a XOR Gate?

A XOR (Exclusive OR) gate outputs HIGH only when the inputs are different.  
When both inputs are same — both LOW or both HIGH — output is LOW.

---

## Truth Table

| A | B | Output |
|---|---|--------|
| 0 | 0 | 0      |
| 0 | 1 | 1      |
| 1 | 0 | 1      |
| 1 | 1 | 0      |

---

## Circuit

| Component | Details |
|-----------|---------|
| Input A | ESP32 GPIO 5 → XOR gate pin A |
| Input B | ESP32 GPIO 17 → XOR gate pin B |
| Output | XOR gate OUT → 1k resistor → LED → GND |

---

## How it works

GPIO 5 and GPIO 17 drive the two inputs of the XOR gate component.  
Inputs are given via serial monitor — type `A B` (e.g. `1 0` or `0 1`).  
The XOR gate hardware handles the logic — LED turns ON only when inputs are different.

---

## How to simulate

1. Open the Wokwi link
2. Click the play button
3. Open the serial monitor
4. Try `0 1` or `1 0` — LED turns ON
5. Try `0 0` or `1 1` — LED stays OFF

---

## Files

- `main.py` — MicroPython source code
- `diagram.json` — Wokwi circuit

---

## Part of

[MicroPython Digital Lab](https://github.com/kritishmohapatra/MicroPython_Digital_Lab) — simulating digital logic circuits using MicroPython on ESP32.