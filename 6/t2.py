from sys import argv
if len(argv) > 1 and argv[1].strip() in ("test", "t"):
    s = "test.txt"
else:
    s = "input.txt"
with open(s) as f:
    lines = list(l.strip("\n") for l in f.readlines())

ops = lines[-1].split()[::-1]
N = len(ops)
numlines = lines[:-1]
M = len(numlines)
nums = [[]]
for i in range(len(numlines[0])-1, -1, -1):
    if all(numlines[j][i]==" " for j in range(M)):
        nums.append([])
        continue
    n = 0
    pos = 0
    for j in range(M):
        ch = numlines[M-j-1][i]
        if ch == " ":
            continue
        n += int(ch)*(10**pos)
        pos += 1
    nums[-1].append(n)

print(nums)
print(ops)

def add(i, j=None):
    if j is None:
        return i
    return i+j

def mul(i, j=None):
    if j is None:
        return i
    return i*j

key = 0
for i in range(N):
    op = add if ops[i] == "+" else mul
    num = None
    for n2 in nums[i]:
        num = op(n2, num)
    key += num

print(key)
