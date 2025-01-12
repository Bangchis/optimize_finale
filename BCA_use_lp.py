# PYTHON
from ortools.linear_solver import pywraplp


n, m = [int(i) for i in input().split()]

A = [[0 for j in range(m)] for i in range(n)]

for i in range(n):
    L = [int(i) for i in input().split()][1:]  # L = [ 5 1 3 5 10 12]

    for l in L:
        A[i][l-1] = 1

x = [[0 for j in range(m)] for i in range(n)]
nconst = int(input())  # 25
Const = []
for i in range(nconst):
    i, j = [int(i) for i in input().split()]
    Const.append((i-1, j-1))


# SETUP

solver = pywraplp.Solver.CreateSolver("SCIP")
inf = solver.infinity()

for i in range(n):
    for j in range(m):
        x[i][j] = solver.IntVar(lb=0, ub=A[i][j], name=f'x_{i}_{j}')

# thiết lập với 25 cái constraits
for constraint in Const:
    j1, j2 = constraint
    for i in range(n):
        solver.Add(x[i][j1] + x[i][j2] <= 1)

for j in range(m):
    solver.Add(solver.Sum(x[i][j] for i in range(n)) == 1)

# objective function
z = solver.NumVar(lb=0, ub=inf, name="z")
for i in range(n):
    solver.Add(z >= solver.Sum(x[i][j] for j in range(m)))

solver.Minimize(z)
solver.Solve()

object_sol = solver.Objective().Value()
print(int(object_sol))
