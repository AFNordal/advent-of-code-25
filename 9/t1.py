from sys import argv

if len(argv) > 1 and argv[1].strip() in ("test", "t"):
    s = "test.txt"
else:
    s = "input.txt"
with open(s) as f:
    tiles = list(list(map(int, l.strip().split(","))) for l in f.readlines())

rec = 0
for i, t1 in enumerate(tiles):
    for j, t2 in enumerate(tiles):
        d = abs(t1[0]-t2[0]+1)*abs(t1[1]-t2[1]+1)
        rec = max(d, rec)

print(rec)