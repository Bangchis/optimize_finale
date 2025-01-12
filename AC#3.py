# PYTHON
from collections import deque
n = int(input())
domain = {}

for i in range(n):
    t = [int(x) for x in input().split()]
    domain[f"x{ i+ 1}"] = t[1:]


c = int(input())
constraints = []
for _ in range(c):
    temp = [int(x) for x in input().split()]
    constraints.append((f"x{temp[0]}", f"x{temp[1]}", temp[2]))

queue = deque()
for constraint in constraints:
    queue.append(constraint)


def AC3():
    global domain
    global queue
    global constraints
    while queue:
        ele = queue.popleft()
        if reviseAC3(ele):
            if not domain[ele[0]]:
                return False
            else:
                for constraint in constraints:
                    if ele[0] in constraint or ele[1] in constraint:
                        queue.append(constraint)

    return True


def reviseAC3(ele):
    global domain
    change = False

    for value0 in domain[ele[0]].copy():
        found = False
        for value1 in domain[ele[1]]:
            if value1 + ele[2] >= value0:
                found = True
                break
            else:
                continue

        if not found:
            domain[ele[0]].remove(value0)
            change = True

    for value1 in domain[ele[1]].copy():
        found = False
        for value0 in domain[ele[0]]:
            if value1 + ele[2] >= value0:
                found = True
                break
            else:
                continue

        if not found:

            domain[ele[1]].remove(value1)
            change = True

    return change


ans = AC3()

if ans == False:
    print("FAIL")
else:
    for i in range(n):
        print(len(domain[f"x{i + 1}"]), end=" ")
        for value in sorted(domain[f"x{i + 1}"]):
            print(value, end=" ")
        print()
