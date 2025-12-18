from sys import argv
if len(argv) > 1 and argv[1].strip() in ("test", "t"):
    s = "test.txt"
else:
    s = "input.txt"
with open(s) as f:
    lines = list(l.strip() for l in f.readlines())

blank = lines.index("")
ranges = lines[:blank]
IDs = lines[blank+1:]

key = 0
for ID in IDs:
    ID = int(ID)
    for r in ranges:
        n1, n2 = r.split("-")
        n1, n2 = int(n1), int(n2)
        if n1 <= ID <= n2:
            key += 1
            break
print(key)