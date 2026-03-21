# Day 07 — XNOR Gate

**Series:** MicroPython Digital Lab  
**Board:** ESP32 DevKit C V4  
**Simulator:** [Run on Wokwi](https://wokwi.com/projects/459109888603341825)

## What is a XNOR Gate?

A XNOR (Exclusive NOR) gate is the inverse of a XOR gate.  
Output is HIGH only when both inputs are the same — both LOW or both HIGH.  
When inputs are different, output is LOW.

---

## Truth Table

| A | B | Output |
|---|---|--------|
| 0 | 0 | 1      |
| 0 | 1 | 0      |
| 1 | 0 | 0      |
| 1 | 1 | 1      |

---

## Circuit

| Component | Details |
|-----------|---------|
| Input A | ESP32 GPIO 5 → XNOR gate pin A |
| Input B | ESP32 GPIO 17 → XNOR gate pin B |
| Output | XNOR gate OUT → 1k resistor → LED → GND |

---

## How it works

GPIO 5 and GPIO 17 drive the two inputs of the XNOR gate component.  
Inputs are given via serial monitor — type `A B` (e.g. `1 1` or `0 0`).  
The XNOR gate hardware handles the logic — LED turns ON only when both inputs are the same.

---

## How to simulate

1. Open the Wokwi link
2. Click the play button
3. Open the serial monitor
4. Try `0 0` or `1 1` — LED turns ON
5. Try `0 1` or `1 0` — LED stays OFF

---

## Files

- `main.py` — MicroPython source code
- `diagram.json` — Wokwi circuit

---

## Part of

[MicroPython Digital Lab](https://github.com/kritishmohapatra/MicroPython_Digital_Lab) — simulating digital logic circuits using MicroPython on ESP32.