from sys import argv

if len(argv) > 1 and argv[1].strip() in ("test", "t"):
    s = "test.txt"
else:
    s = "input.txt"

with open(s) as f:
    ranges = list(l.strip() for l in f.readline().split(","))

key = 0
for rng in ranges:
    n1, n2 = rng.split("-")
    for n in range(int(n1), int(n2) + 1):
        sn = str(n)
        if len(sn) % 2 == 0:
            half = len(sn) // 2
            if sn[:half] == sn[half:]:
                key += n

print(key)
