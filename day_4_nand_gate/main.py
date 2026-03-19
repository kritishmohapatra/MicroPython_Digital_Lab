from machine import Pin

pinA = Pin(5, Pin.OUT)
pinB = Pin(17, Pin.OUT)

print("NAND Gate Simulator")
print("Enter input as: A B (e.g. 1 1 or 0 1)")
print("-" * 30)

while True:
    try:
        line = input("A B: ").strip()
        parts = line.split()
        if len(parts) != 2:
            print("Enter exactly 2 values: 0 or 1")
            continue
        a = int(parts[0])
        b = int(parts[1])
        if a not in (0, 1) or b not in (0, 1):
            print("Only 0 or 1 allowed")
            continue
        pinA.value(a)
        pinB.value(b)
        print(f"A={a} | B={b}")
    except Exception as e:
        print("Error:", e)