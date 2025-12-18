from sys import argv
if len(argv) > 1 and argv[1].strip() in ("test", "t"):
    s = "test.txt"
else:
    s = "input.txt"
with open(s) as f:
    lines = list(l.strip() for l in f.readlines())

blank = lines.index("")
ranges_ = lines[:blank]
IDs = lines[blank+1:]

ranges = set()
for r in ranges_:
    n1, n2 = r.split("-")
    ranges.add((int(n1), int(n2)))


key = 0
changing = True
while changing:
    print("================================")
    changing = False
    new = set()
    for i, (l, h) in enumerate(ranges):
        for j, (n1, n2) in enumerate(ranges):
            if i == j:
                continue
            if n1 < l <= n2:
                l = n1
                changing = True
        for j, (n1, n2) in enumerate(ranges):
            if i == j:
                continue
            if n1 <= h < n2:
                h = n2
                changing = True
        new.add((l, h))
        print(l, h)
    ranges = new

for l, h in ranges:
    key += h-l+1
print(key)