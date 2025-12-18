from sys import argv
if len(argv) > 1 and argv[1].strip() in ("test", "t"):
    s = "test.txt"
else:
    s = "input.txt"
with open(s) as f:
    lines = list(bytearray(l.strip().encode()) for l in f.readlines())
R = len(lines)
C = len(lines[0])

def adj(r, c):
    coords = []
    if r != 0:
        coords.append((r-1, c))
        if c != 0:
            coords.append((r-1, c-1))
        if c != C-1:
            coords.append((r-1, c+1))
    if r != R-1:
        coords.append((r+1, c))
        if c != 0:
            coords.append((r+1, c-1))
        if c != C-1:
            coords.append((r+1, c+1))
    if c != 0:
        coords.append((r, c-1))
    if c != C-1:
        coords.append((r, c+1))
    return coords

key = 0
repeat = True
while repeat:
    repeat = False
    for r,  line in enumerate(lines):
        for c, val in enumerate(line):
            if val == ord("."):
                print(".", end="")
                continue
            count = 0
            for cr, cc in adj(r, c):
                if lines[cr][cc] == ord(b"@"):
                    if count == 3:
                        print("@", end="")
                        break
                    count += 1
            else:
                print("x", end="")
                lines[r][c] = ord(".")
                repeat=True
                key += 1
        print()
print(key)
