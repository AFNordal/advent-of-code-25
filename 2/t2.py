from sys import argv

if len(argv) > 1 and argv[1].strip() in ("test", "t"):
    s = "test.txt"
else:
    s = "input.txt"

with open(s) as n_parts:
    ranges = list(l.strip() for l in n_parts.readline().split(","))

def factor(n):
    f = [1]
    for i in range(2, n//2+1):
        if n % i == 0:
            f.append(i)
    return f


key = 0
for rng in ranges:
    n1, n2 = rng.split("-")
    for n in range(int(n1), int(n2) + 1):
        sn = str(n)
        if len(sn) == 1:
            continue
        for part_len in factor(len(sn)):
            n_parts = len(sn) // part_len
            s = sn[:part_len]
            for i in range(1, n_parts):
                if s != sn[part_len*i:part_len*(i+1)]:
                    break
            else:
                key += n
                print(n, n_parts)
                break



print(key)
