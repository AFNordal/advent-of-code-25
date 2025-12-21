from sys import argv
from math import gcd

if len(argv) > 1 and argv[1].strip() in ("test", "t"):
    s = "test.txt"
else:
    s = "input.txt"
with open(s) as f:
    lines = list(l.strip().split(" ") for l in f.readlines())


def printmat(A, b=None):
    for i in range(len(A)):
        print("[" + " ".join(f"{num:2}" for num in A[i]), end="")
        if b is not None:
            print(f" | {b[i]:2}", end="")
        print("]")


def switchrows(A, b, i, j):
    A[i], A[j] = A[j], A[i]
    b[i], b[j] = b[j], b[i]


def subtract(A, b, i, j):
    for k in range(len(A[0])):
        A[i][k] -= A[j][k]
    b[i] -= b[j]


def add(A, b, i, j, times):
    for k in range(len(A[0])):
        A[i][k] += times * A[j][k]
    b[i] += times * b[j]


def div(A, b, i, n):
    for k in range(len(A[0])):
        assert A[i][k] % n == 0, f"{A[i][k]} / {n}"
        A[i][k] //= n
    assert b[i] % n == 0
    b[i] //= n


def mul(A, b, i, n):
    for k in range(len(A[0])):
        A[i][k] *= n
    b[i] *= n


def negate(A, b, i):
    for k in range(len(A[0])):
        A[i][k] = -A[i][k]
    b[i] = -b[i]


def search_free_vars(A, b, free_vars, bounds, ptr=0, values=[]):
    if ptr < len(free_vars):  # Not end of recursion
        var = free_vars[ptr]
        record = 9999999
        # Call itself for each value for current free variable
        for i in range(bounds[var] + 1):
            v = values[:] + [i]
            _presses = search_free_vars(A, b, free_vars, bounds, ptr + 1, values=v)
            record = min(record, _presses)
        return record

    else:  # end of recursion. Evaluate "solution"
        presses = sum(values)
        for i in range(len(A)):
            row_presses = b[i]
            for var, val in zip(free_vars, values):
                row_presses -= A[i][var] * val
            for pivot in A[i]:  # Find pivot (LHS) to divide RHS
                if pivot != 0:
                    break
            if row_presses % pivot != 0: # Not an integer solution
                return 9999999999
            row_presses //= pivot 
            if row_presses < 0: # Not a positive solution
                return 9999999999
            presses += row_presses
        return presses


key = 0
for l in lines[:]:
    # Load data (equation is A*x=b)
    _, buttons, jolts = l[0], list(dict.fromkeys(l[1:-1])), l[-1]
    b = list(map(int, jolts[1:-1].split(",")))
    A = [list([0 for _ in buttons]) for _ in b]
    M, N = len(buttons), len(b)
    # Find bounds of each variable
    bounds = [999999 for _ in buttons]
    for i, btn in enumerate(buttons):
        for j in btn[1:-1].split(","):
            A[int(j)][i] = 1
            bounds[i] = min(bounds[i], b[int(j)])

    print("PROBLEM: =================")
    printmat(A, b)
    print("==========================")

    free_vars = []
    top_ptr = 0
    for j in range(M):
        # Find first row below top_ptr with non-zero element in col j
        for i in range(top_ptr, N):
            if A[i][j] != 0:
                switchrows(A, b, i, top_ptr)
                break
        else:
            # No such row <=> free variable. Skip to next col
            free_vars.append(j)
            continue
        # Find all other rows with non-zero element in col j
        for i in range(N):
            if i == top_ptr:
                continue
            if A[i][j] != 0:
                # Reduce row i by the one we placed at top_ptr
                divisor = gcd(-A[i][j], A[top_ptr][j])
                mul(A, b, i, A[top_ptr][j])
                add(A, b, i, top_ptr, -A[i][j] // A[top_ptr][j])
                div(A, b, i, divisor)
        top_ptr += 1

    print("REDUCED: =================")
    printmat(A, b)
    print("==========================")

    # Remove zero-rows and solve trivial equations
    presses = 0
    A2 = []
    b2 = []
    for i in range(N):
        found = -1
        for j in range(M):
            if A[i][j] != 0:
                if found == -1:
                    found = j
                else:
                    A2.append(A[i])
                    b2.append(b[i])
                    break
        else:  # only one non-zero elem in row (trivial case)
            if found != -1:
                _p = b[i] // A[i][found]
                presses += _p

    # Exhaustive BFS on free variables
    p = search_free_vars(A2, b2, free_vars, bounds)
    presses += p
    print("SOLUTION:", presses, end="\n\n")
    key += presses


print(key)
