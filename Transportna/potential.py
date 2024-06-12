import pulp
import numpy as np

# Define the transportation problem parameters
costs = np.array([[6,5,9,8], [6,4,8,6], [9,8,4,7]])
supply = np.array([20, 35, 55])
demand = np.array([36, 32, 24, 18])
# Create a PuLP LP problem object
problem = pulp.LpProblem("Transportation Problem", pulp.LpMinimize)


rows = len(supply)
cols = len(demand)
var_matrix = pulp.LpVariable.dicts("x", ((i, j) for i in range(rows) for j in range(cols)), lowBound=0, cat='Continuous')

# Define the objective function
problem += pulp.lpSum([costs[i][j] * var_matrix[(i, j)] for i in range(rows) for j in range(cols)])

# Define the supply constraints
for i in range(rows):
    problem += pulp.lpSum([var_matrix[(i, j)] for j in range(cols)]) == supply[i]

# Define the demand constraints
for j in range(cols):
    problem += pulp.lpSum([var_matrix[(i, j)] for i in range(rows)]) == demand[j]

# Solve the problem
problem.solve()

# Print the optimal solution
result=[]
print("Optimal solution:")
for i in range(rows):
    for j in range(cols):
       result.append(int(pulp.value(var_matrix[(i,j)])))

subarrays = [result[i:i+cols] for i in range(0, len(result), cols)]

for subarray in subarrays:
    print(subarray)

# Print the optimal cost
print(f"Optimal cost: {pulp.value(problem.objective)}")

##########################################################################

def minimal_elements(costs_or, supply_or, demand_or):
    costs = costs_or.copy()
    supply = supply_or.copy()
    demand = demand_or.copy()
    if supply.sum() == demand.sum():
        volume_of_deliveries = np.zeros(costs.shape, dtype="int32")
        indices = np.unravel_index(np.argsort(costs, axis=None), costs.shape)
        for i in range(len(supply) * len(demand)):
            min_index = indices[0][i], indices[1][i]
            temp = min(supply[min_index[0]], demand[min_index[1]])
            supply[min_index[0]] -= temp
            demand[min_index[1]] -= temp
            volume_of_deliveries[min_index[0], min_index[1]] = temp

            if (supply == 0).all() and (demand == 0).all():
                break
    print ( volume_of_deliveries)
    potentials(costs_or, volume_of_deliveries)


def potentials(costs_or, volume_of_deliveries):
    volume_of_delivery = volume_of_deliveries.copy()
    u = np.full(int(costs_or.size / costs_or[0].size),None)
    v = np.full(costs_or[0].size,None)
    u[0]=0
    for i in range(u.size):
        for j in range(v.size):
            if volume_of_delivery[i][j]!=0:
                if u[i]!=None:
                    v[j]=costs_or[i][j]-u[i]
                elif v[j]!=None:
                    u[i]=costs_or[i][j]-v[j]
    print(u,v)
    check_optimality(costs_or, supply, demand, volume_of_deliveries, u, v)

def check_optimality(grid, supply, demand, result, row_potentials, col_potentials):
    zero_p=[]
    for i in range(len(supply)):
        for j in range(len(demand)):
            if result[i][j] == 0:
                 if row_potentials[i] + col_potentials[j] > grid[i][j]:
                    zero_p.append([i,j])


    if len(zero_p)==0:
        print("Розв'язок є оптимальним.")
        return True
    else:
        print("Розв'язок не є оптимальним. Потрібно провести перевантаження.",max(zero_p))
        return max(zero_p)

minimal_elements(costs, supply, demand)