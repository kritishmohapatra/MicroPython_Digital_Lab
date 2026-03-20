# Day 05 — NOR Gate

**Series:** MicroPython Digital Lab  
**Board:** ESP32 DevKit C V4  
**Simulator:** [Run on Wokwi](https://wokwi.com/projects/458904903289969665
) 

---

## What is a NOR Gate?

A NOR gate is the inverse of an OR gate.  
Output is HIGH only when all inputs are LOW. In every other combination, output is LOW.  
Like NAND, it is also a universal gate — any logic circuit can be built using only NOR gates.

---

## Truth Table

| A | B | Output |
|---|---|--------|
| 0 | 0 | 1      |
| 0 | 1 | 0      |
| 1 | 0 | 0      |
| 1 | 1 | 0      |

---

## Circuit

| Component | Details |
|-----------|---------|
| Input A | ESP32 GPIO 5 → NOR gate pin A |
| Input B | ESP32 GPIO 17 → NOR gate pin B |
| Output | NOR gate OUT → 1k resistor → LED → GND |

---

## How it works

GPIO 5 and GPIO 17 drive the two inputs of the NOR gate component.  
Inputs are given via serial monitor — type `A B` (e.g. `1 1` or `0 1`).  
The NOR gate hardware handles the logic — LED turns ON only when both inputs are LOW.

---

## How to simulate

1. Open the Wokwi link
2. Click the play button
3. Open the serial monitor
4. Type `0 0` — LED turns ON
5. Try `0 1`, `1 0`, `1 1` — LED stays OFF

---

## Files

- `main.py` — MicroPython source code
- `diagram.json` — Wokwi circuit

---

## Part of

[MicroPython Digital Lab](https://github.com/kritishmohapatra/MicroPython_Digital_Lab) — simulating digital logic circuits using MicroPython on ESP32.