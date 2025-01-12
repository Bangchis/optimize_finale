# PYTHON
from ortools.sat.python import cp_model

model = cp_model.CpModel()
n, m = map(int, input().split())
teacher = [[0 for _ in range(m)] for _ in range(n)]
teacher_range = []
for i in range(n):
    temp = list(map(int, input().split()))
    teacher_range.append(temp[1:])

c = int(input())
constraint = []
for _ in range(c):
    temp = tuple(map(int, input().split()))
    constraint.append(temp)

# constriant

for i in range(n):
    for j in range(m):
        if j + 1 in teacher_range[i]:
            teacher[i][j] = model.NewIntVar(0, 1, f"x{i}_{j}")
        else:
            teacher[i][j] = model.NewIntVar(0, 0, f"x{i}_{j}")

for j in range(m):
    model.Add(sum(teacher[i][j] for i in range(n)) == 1)

for iter in range(c):
    sub0, sub1 = constraint[iter]
    sub0 -= 1
    sub1 -= 1
    for i in range(n):
        model.Add(teacher[i][sub0] + teacher[i][sub1] <= 1)

z = model.NewIntVar(0, m, f"z")

for i in range(n):
    model.Add(z >= sum(teacher[i][j] for j in range(m)))


model.Minimize(z)

solver = cp_model.CpSolver()
status = solver.Solve(model)


if status == cp_model.OPTIMAL:
    print(int(solver.ObjectiveValue()))
else:
    print('NO_SOLUTION')
