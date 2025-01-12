# PYTHON
from ortools.sat.python import cp_model

model = cp_model.CpModel()
n, m = map(int, input().split())

edges = []
for i in range(m):
    temp = list(map(int, input().split()))
    edges.append((temp[0] - 1, temp[1] - 1, temp[2]))


x = [model.NewIntVar(0, 1, f"x_{edge}") for edge in range(m)]
y = [model.NewIntVar(0, 1, f"y_{edge}") for edge in range(m)]


for edge in range(m):
    model.Add(x[edge] + y[edge] <= 1)


for vertex in range(n):
    if vertex == 0:
        model.Add(sum(x[index]
                  for index in range(m) if edges[index][0] == 0) == 1)
        model.Add(sum(y[index]
                  for index in range(m) if edges[index][0] == 0) == 1)
    elif vertex == n-1:
        model.Add(sum(x[index]
                  for index in range(m) if edges[index][1] == n-1) == 1)
        model.Add(sum(y[index]
                  for index in range(m) if edges[index][1] == n-1) == 1)
    else:
        model.Add(sum(x[index] for index in range(
            m) if edges[index][0] == vertex) <= 1)
        model.Add(sum(y[index] for index in range(
            m) if edges[index][0] == vertex) <= 1)
        model.Add(sum(x[index] for index in range(
            m) if edges[index][1] == vertex) <= 1)
        model.Add(sum(y[index] for index in range(
            m) if edges[index][1] == vertex) <= 1)

        model.Add(sum(x[index] for index in range(m) if edges[index][0] == vertex) == sum(
            x[index] for index in range(m) if edges[index][1] == vertex))
        model.Add(sum(y[index] for index in range(m) if edges[index][0] == vertex) == sum(
            y[index] for index in range(m) if edges[index][1] == vertex))


objective = sum(edges[edge][2] * (x[edge] + y[edge]) for edge in range(m))
model.Minimize(objective)

solver = cp_model.CpSolver()
status = solver.Solve(model)
if status == cp_model.OPTIMAL:
    print(solver.Value(objective))
    # print("solution")
    # for i in range(n):
    #     for j in range(n):
    #         print(f'x[{i}][{j}] = {solver.Value(x[i][j])}')

    # for i in range(n):
    #     for j in range(n):
    #         print(f'y[{i}][{j}] = {solver.Value(y[i][j])}')

    # print()
    # print(dfs(x,n))
    # print()
    # print(dfs(y,n))


else:
    print("NOT_FEASIBLE")
