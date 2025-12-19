from sys import argv
from tqdm import tqdm

class Edge:
    def __init__(self, t1, t2, ox=0, oy=0):
        self.x1, self.y1 = t1[0] * 2, t1[1] * 2
        self.x2, self.y2 = t2[0] * 2, t2[1] * 2
        if self.x1 == self.x2:
            self.v = True
            self.y1, self.y2 = sorted((self.y1, self.y2))
            self.y1 += oy
            self.y2 -= oy
            self.x1 += ox
            self.x2 += ox
        elif self.y1 == self.y2:
            self.v = False
            self.x1, self.x2 = sorted((self.x1, self.x2))
            self.y1 += oy
            self.y2 += oy
            self.x1 += ox
            self.x2 -= ox
        else:
            raise Exception

    def ix(s, o):
        if s.v == o.v:
            return False
        elif s.v:
            if o.x1 < s.x1 < o.x2 and s.y1 < o.y1 < s.y2:
                return True
        else:
            if s.x1 < o.x1 < s.x2 and o.y1 < s.y1 < o.y2:
                return True
        return False


if len(argv) > 1 and argv[1].strip() in ("test", "t"):
    s = "test.txt"
else:
    s = "input.txt"

with open(s) as f:
    tiles = list(list(map(int, l.strip().split(","))) for l in f.readlines())
N = len(tiles)

edges = []
for i in range(N):
    edges.append(Edge(tiles[i], tiles[(i + 1) % N]))

arr = []
for i, t1 in enumerate(tqdm(tiles)):
    for j, t2 in enumerate(tiles):
        _t1 = (min(t1[0], t2[0]), min(t1[1], t2[1]))
        _t2 = (max(t1[0], t2[0]), max(t1[1], t2[1]))
        e = [
            Edge(
                _t1,
                (_t1[0], _t2[1]),
                oy=1 if _t1[1] != _t2[1] else 0,
                ox=1 if _t1[0] != _t2[0] else 0,
            ),
            Edge(
                _t1,
                (_t2[0], _t1[1]),
                oy=1 if _t1[1] != _t2[1] else 0,
                ox=1 if _t1[0] != _t2[0] else 0,
            ),
            Edge(
                (_t1[0], _t2[1]),
                _t2,
                oy=-1 if _t1[1] != _t2[1] else 0,
                ox=1 if _t1[0] != _t2[0] else 0,
            ),
            Edge(
                (_t2[0], _t1[1]),
                _t2,
                oy=1 if _t1[1] != _t2[1] else 0,
                ox=-1 if _t1[0] != _t2[0] else 0,
            ),
        ]
        c = False
        for e2 in edges:
            if any(e2.ix(e1) for e1 in e):
                c = True
                break
        if c:
            continue
        d = (abs(t1[0] - t2[0]) + 1) * (abs(t1[1] - t2[1]) + 1)
        arr.append((t1, t2, d))

arr.sort(key=lambda x: x[2], reverse=True)
print(arr[0][2])
