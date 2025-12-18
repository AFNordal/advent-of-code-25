from sys import argv


class JB:
    def __init__(self, id):
        self.circuit: Circuit = None
        self.id = id

class Circuit:
    def __init__(self):
        self.jbs = set()

    def add(self, jb: JB):
        self.jbs.add(jb)
        jb.circuit = self
    
    def connect(self, other):
        self.jbs = self.jbs.union(other.jbs)
        for jb in other.jbs:
            jb.circuit = self

def idtup(i, j):
    return (min(i, j), max(i, j))

if len(argv) > 1 and argv[1].strip() in ("test", "t"):
    s = "test.txt"
    N = 10
else:
    s = "input.txt"
    N = 1000
with open(s) as f:
    boxes = list(list(map(int, l.strip().split(","))) for l in f.readlines())

D = []
jbs = []
# circuits = []
for i, (x, y, z) in enumerate(boxes):
    _jb = JB(len(jbs))
    _circ = Circuit()
    _circ.add(_jb)
    # circuits.append(_circ)
    jbs.append(_jb)

    for j, (x2, y2, z2) in enumerate(boxes[:i]):
        D.append(((j, i), (x-x2)**2+(y-y2)**2+(z-z2)**2))
D.sort(key=lambda x: x[1])

for d in D[:N]:
    (jb1, jb2), dist = d
    jbs[jb1].circuit.connect(jbs[jb2].circuit)

circuits = set()
for jb in jbs:
    circuits.add(jb.circuit)
circuits = sorted([len(x.jbs) for x in circuits], reverse=True)
print(circuits[0]*circuits[1]*circuits[2])