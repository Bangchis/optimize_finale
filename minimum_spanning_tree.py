# PYTHON
# PYTHON
from ortools.sat.python import cp_model

model = cp_model.CpModel()

# input handler
n, m, s, L = (int(x) for x in input().split())
edges = []
time_and_cost = {}
neighborhood = {}
for edge in range(m):
    all = [int(x) for x in input().split()]
    edges.append((all[0] - 1, all[1] - 1))
    time_and_cost[(all[0] - 1, all[1] - 1)] = (all[2], all[3])

for ele in edges:
    if ele[0] not in neighborhood:
        neighborhood[ele[0]] = [ele[1]]
    else:
        neighborhood[ele[0]].append(ele[1])

In = {}
for key in neighborhood:
    for x in neighborhood[key]:
        In[x] = In.get(x, []) + [key]


z = {}
x = [model.NewIntVar(0, n - 1, f'x{i}') for i in range(n)]
y = [model.NewIntVar(0, 5500, f'y{i}') for i in range(n)]
for edge in edges:
    z[edge] = model.NewIntVar(0, 1, f'z{edge[0]}_{edge[1]}')
########################################

model.Add(y[s - 1] == 0)
for i in range(n):
    if i != s - 1:
        model.AddAllowedAssignments([x[i]], [[int(v)] for v in In[i]])


#################
for i in range(n):
    if i != s - 1:
        for j in In[i]:

            condition_met = model.NewBoolVar(f"condition_met_{j}_{i}")
            # Ràng buộc khi x[i] == j
            model.Add(x[i] == j).OnlyEnforceIf(condition_met)
            model.Add(z[(j, i)] == 1).OnlyEnforceIf(condition_met)
            model.Add(y[j] + time_and_cost[(j, i)][0] ==
                      y[i]).OnlyEnforceIf(condition_met)

            # Ràng buộc khi x[i] != j
            model.Add(x[i] != j).OnlyEnforceIf(condition_met.Not())
            model.Add(z[(j, i)] == 0).OnlyEnforceIf(condition_met.Not())

for j in range(n):
    model.Add(y[j] <= L)
# objective
objective = sum(z[(i, j)] * time_and_cost[(i, j)][1] for (i, j) in z)

model.Minimize(objective)

solver = cp_model.CpSolver()
status = solver.Solve(model)


# In kết quả
if status == cp_model.OPTIMAL:
    # print('Solution:')
    # print(f'Objective value = {solver.ObjectiveValue()}\n')
    # for i in range(n):
    #     if i != s - 1:
    #         print(f'x[{i}] = {solver.Value(x[i])}')
    # print()
    # for j in range(n):
    #     print(f'y[{j}] = {solver.Value(y[j])}', end = " ")
    # print()

    # for key in z:
    #     print(f'z[{key}] = {solver.Value(z[key])}', end = " ")
    print(int(solver.ObjectiveValue()))
else:
    print('NO_SOLUTION')
    # print(f'Objective value = {solver.ObjectiveValue()}\n')
