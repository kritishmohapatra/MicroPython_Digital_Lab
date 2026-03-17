# MicroPython Digital Lab

> Simulating digital logic circuits using MicroPython on ESP32 — fully interactive, zero hardware required.

This series is **not** about replacing hardware ICs.  
It's about understanding digital logic through **code, simulation, and visualization** — one circuit at a time.

Built and maintained by [@0D_KR](https://x.com/0D_KR) · Part of the [#100DaysOfIoT](https://github.com/kritishmohapatra/100_Days_100_IoT_Projects) journey.

---

## Why MicroPython?

- No breadboard, ICs, or oscilloscope needed — just an ESP32 and [Wokwi](https://wokwi.com)
- Every circuit is **instantly shareable** via a Wokwi link
- Same truth tables, same behavior — but you can **read the logic in code**
- Perfect entry point for EE students bridging theory and embedded systems

---

## Series Roadmap

### Phase 1 — Logic Gates (Days 01–07)

| Day | Circuit | Output | Wokwi |
|-----|---------|--------|-------|
| 01 | AND Gate | LED ON only when both inputs HIGH | [▶ Run](https://wokwi.com/projects/458750462926204929) |
| 02 | OR Gate | LED ON when either input HIGH | [▶ Run](#) |
| 03 | NOT Gate | LED inverts input | [▶ Run](#) |
| 04 | NAND Gate | Inverse of AND | [▶ Run](#) |
| 05 | NOR Gate | Inverse of OR | [▶ Run](#) |
| 06 | XOR Gate | LED ON when inputs differ | [▶ Run](#) |
| 07 | XNOR + Universal Gate Demo | NAND builds everything | [▶ Run](#) |

### Phase 2 — Combinational Circuits (Days 08–17)

| Day | Circuit | Output | Wokwi |
|-----|---------|--------|-------|
| 08 | Half Adder | Sum + Carry LEDs | [▶ Run](#) |
| 09 | Full Adder | 3-input sum with carry | [▶ Run](#) |
| 10 | 4-bit Ripple Carry Adder | 4-LED binary output | [▶ Run](#) |
| 11 | 2:1 MUX | Select between 2 inputs | [▶ Run](#) |
| 12 | 4:1 MUX | Select between 4 inputs | [▶ Run](#) |
| 13 | 2:4 Decoder | Active-low LED decoding | [▶ Run](#) |
| 14 | 3:8 Decoder | Full binary to one-hot | [▶ Run](#) |
| 15 | Encoder (4:2) | Priority encoding | [▶ Run](#) |
| 16 | Comparator (1-bit) | Equal / Greater / Less LEDs | [▶ Run](#) |
| 17 | Priority Encoder | Highest active input wins | [▶ Run](#) |

### Phase 3 — Sequential Circuits (Days 18–25)

| Day | Circuit | Output | Wokwi |
|-----|---------|--------|-------|
| 18 | SR Flip-Flop | Set/Reset latch | [▶ Run](#) |
| 19 | D Flip-Flop | Edge-triggered latch | [▶ Run](#) |
| 20 | JK Flip-Flop | Toggle mode demo | [▶ Run](#) |
| 21 | T Flip-Flop | Clock divider | [▶ Run](#) |
| 22 | 3-bit Ripple Counter | Binary count on LEDs | [▶ Run](#) |
| 23 | Synchronous Counter | Clean clocked counting | [▶ Run](#) |
| 24 | Ring Counter | Rotating LED pattern | [▶ Run](#) |
| 25 | Johnson Counter | Shift register pattern | [▶ Run](#) |

---

## Folder Structure

```
MicroPython-Digital-Lab/
├── 01_and_gate/
│   ├── main.py          ← MicroPython source code
│   ├── diagram.json     ← Wokwi circuit file
│   └── README.md        ← Truth table + explanation
├── 02_or_gate/
│   └── ...
├── assets/
│   └── *.gif            ← Demo recordings
└── README.md            ← This file
```

---

## Hardware / Simulator

| Item | Details |
|------|---------|
| Board | ESP32 DevKit V1 |
| Simulator | [Wokwi](https://wokwi.com) |
| Language | MicroPython |
| Inputs | Push buttons (GPIO with PULL_DOWN) |
| Output | LEDs |

---

## Getting Started

1. Click any **▶ Run** link in the table above — Wokwi opens instantly in your browser
2. Press the simulated buttons to toggle inputs
3. Watch the LED(s) reflect the circuit's truth table in real time
4. Read `main.py` to understand the logic behind it

No hardware required. No setup needed.

---

## Each Day's README includes

- Circuit description
- Truth table
- MicroPython code walkthrough
- Wokwi simulation link
- Key concept explained in plain language

---

## Connect

- X / Twitter: [@0D_KR](https://x.com/0D_KR)
- GitHub: [kritishmohapatra](https://github.com/kritishmohapatra)
- Series: [#100DaysOfIoT](https://github.com/kritishmohapatra/100_Days_100_IoT_Projects)

---

## License

MIT License — free to use, fork, and learn from.

---

*If this helped you understand digital logic better, drop a star on the repo!*