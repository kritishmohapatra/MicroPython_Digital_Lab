from machine import Pin

pinA = Pin(5, Pin.OUT)

print("NOT Gate Simulator")
print("Enter input as: A (e.g. 1 or 0)")
print("-" * 30)

while True:
    try:
        line = input("A: ").strip()
        parts = line.split()
        if len(parts) != 1:
            print("Enter exactly 1 value: 0 or 1")
            continue
        a = int(parts[0])
        if a not in (0, 1):
            print("Only 0 or 1 allowed")
            continue
        pinA.value(a)
        print(f"A={a}")
    except Exception as e:
        print("Error:", e)