from sys import argv
if len(argv) > 1 and argv[1].strip() in ("test", "t"):
    s = "test.txt"
else:
    s = "input.txt"
with open(s) as f:
    lines = list(l.strip() for l in f.readlines())
# print(lines)
ops = lines[-1].split()
nums = []
for l in lines[:-1]:
    nums.append(list(map(int, l.split())))

def add(i, j=None):
    if j is None:
        return i
    return i+j

def mul(i, j=None):
    if j is None:
        return i
    return i*j

key = 0
for i in range(len(ops)):
    op = add if ops[i] == "+" else mul
    num = None
    for j in range(len(nums)):
        num = op(nums[j][i], num)
    key += num

print(key)
