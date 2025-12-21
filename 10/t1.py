from sys import argv
if len(argv) > 1 and argv[1].strip() in ("test", "t"):
    s = "test.txt"
else:
    s = "input.txt"
with open(s) as f:
    lines = list(l.strip().split(" ") for l in f.readlines())

def l2i(s):
    n = 0
    for i, c in enumerate(s[1:-1]):
        if c == "#":
            n += 1 << i
    return n

def b2i(l):
    r = []
    for s in l:
        i = sum(1 << int(i) for i in s[1:-1].split(","))
        r.append(i)
    return r

def xor_search(target, buttons, state, idx, presses):
    if target == state:
        return presses
    if idx == len(buttons):
        return 10000
    
    # press
    p = xor_search(target, buttons, state ^ buttons[idx], idx+1, presses+1)
    # don't press
    np = xor_search(target, buttons, state, idx+1, presses)
    return min(p, np)
        

key = 0
for l in lines:
    lights, buttons, _ = l[0], l[1:-1], l[-1]
    li, bi = l2i(lights), b2i(buttons)
    key += xor_search(li, bi, 0, 0, 0)
print(key)