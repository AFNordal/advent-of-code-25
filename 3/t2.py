from sys import argv
if len(argv) > 1 and argv[1].strip() in ("test", "t"):
    s = "test.txt"
else:
    s = "input.txt"
with open(s) as f:
    lines = list(l.strip() for l in f.readlines())

def find_digit(digits, n_to_go, start_idx, acc):
    n_to_go -= 1
    if n_to_go == 0:
        return acc + max(digits[start_idx:])
    search = digits[start_idx:-n_to_go]
    print(search, start_idx, n_to_go)
    d1 = max(search)
    d1i = search.index(d1) + start_idx
    return find_digit(digits, n_to_go, d1i+1, 10*(acc+d1))

key = 0
for l in lines:
    nums = list(map(int, l))
    key += find_digit(nums, 12, 0, 0)
print(key)


