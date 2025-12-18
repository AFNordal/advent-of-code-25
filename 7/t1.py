from sys import argv
if len(argv) > 1 and argv[1].strip() in ("test", "t"):
    s = "test.txt"
else:
    s = "input.txt"
with open(s) as f:
    lines = list(l.strip() for l in f.readlines())


arr = []
for l in lines:
    arr.append([])
    for c in l:
        if c == ".":
            arr[-1].append(0) # empty
        elif c == "^":
            arr[-1].append(1) # split
        elif c == "S":
            arr[-1].append(2) # beam

key = 0
for r, row in enumerate(arr):
    for c, ch in enumerate(row):
        if r == 0:
            break
        if arr[r][c] == 0 and arr[r-1][c] == 2: # empty and beam above
            arr[r][c] = 2
        elif arr[r][c] == 1 and arr[r-1][c] == 2: # split and beam above
            arr[r][c-1] = 2
            arr[r][c+1] = 2
            key += 1
print(key)