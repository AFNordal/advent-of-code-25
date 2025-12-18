with open("input.txt") as f:
    lines = list(l.strip() for l in f.readlines())

key1 = 0
key2 = 0
val = 50
for l in lines:
    dir = l[0]
    n = int(l[1:])
    if n == 0:
        continue
    elif dir == "R":
        key2 += (n + val) // 100
        val = (val + n) % 100
    else:
        key2 += (n + 100 - val) // 100
        if val == 0:
            key2 -= 1
        val = (val - n) % 100
    if val == 0:
        key1 += 1
print(key1, key2)

