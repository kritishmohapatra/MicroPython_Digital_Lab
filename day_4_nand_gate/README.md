# Day 04 — NAND Gate

**Series:** MicroPython Digital Lab  
**Board:** ESP32 DevKit C V4  
**Simulator:** [Run on Wokwi](https://wokwi.com/projects/458857534514801665)  

---

## What is a NAND Gate?

A NAND gate is the inverse of an AND gate.  
Output is LOW only when all inputs are HIGH. In every other combination, output is HIGH.  
It is also called a universal gate — any logic circuit can be built using only NAND gates.

---

## Truth Table

| A | B | Output |
|---|---|--------|
| 0 | 0 | 1      |
| 0 | 1 | 1      |
| 1 | 0 | 1      |
| 1 | 1 | 0      |

---

## Circuit

| Component | Details |
|-----------|---------|
| Input A | ESP32 GPIO 5 → NAND gate pin A |
| Input B | ESP32 GPIO 17 → NAND gate pin B |
| Output | NAND gate OUT → 1k resistor → LED → GND |

---

## How it works

GPIO 5 and GPIO 17 drive the two inputs of the NAND gate component.  
Inputs are given via serial monitor — type `A B` (e.g. `1 1` or `0 1`).  
The NAND gate hardware handles the logic — LED stays ON for all input combinations except `1 1`.

---

## How to simulate

1. Open the Wokwi link
2. Click the play button
3. Open the serial monitor
4. Try `0 0`, `0 1`, `1 0` — LED stays ON
5. Type `1 1` — LED turns OFF

---

## Files

- `main.py` — MicroPython source code
- `diagram.json` — Wokwi circuit

---

## Part of

[MicroPython Digital Lab](https://github.com/kritishmohapatra/MicroPython_Digital_Lab) — simulating digital logic circuits using MicroPython on ESP32.