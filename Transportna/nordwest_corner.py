grid_or = [[6, 5, 9, 8], [6, 4, 8, 6], [9, 8, 4, 7]]
supply_or = [20, 35, 55]
demand_or = [36, 32, 24, 18]
grid = grid_or.copy()
supply = supply_or.copy()
demand = demand_or.copy()

def northwest_corner_rule(grid, supply, demand):
    rows = len(supply)
    cols = len(demand)

    transportation_matrix = [[0] * cols for _ in range(rows)]

    i = 0
    j = 0

    while i < rows and j < cols:
        amount = min(supply[i], demand[j])

        transportation_matrix[i][j] = amount

        supply[i] -= amount
        demand[j] -= amount

        if supply[i] == 0:
            i += 1

        if demand[j] == 0:
            j += 1

    return transportation_matrix


result = northwest_corner_rule(grid, supply, demand)

def calculate_potentials(grid, supply, demand, result):
    row_potentials = [None] * len(supply)
    col_potentials = [None] * len(demand)
    visited = [[False] * len(demand) for _ in range(len(supply))]

    for i in range(len(supply)):
        for j in range(len(demand)):
            if result[i][j] != 0 :
                row_potentials[i] = 0
                col_potentials[j] = grid[i][j]
                visited[i][j] = True
                break
        if row_potentials[i] is not None:
            break

    for i in range(len(supply)):
        for j in range(len(demand)):
            if not visited[i][j] and (row_potentials[i] is not None or col_potentials[j] is not None):
                if result[i][j] != 0 and row_potentials[i] is not None and col_potentials[j] is None:
                    col_potentials[j] = grid[i][j] - row_potentials[i]
                elif result[i][j] != 0 and row_potentials[i] is None and col_potentials[j] is not None:
                    row_potentials[i] = grid[i][j] - col_potentials[j]
                visited[i][j] = True
    return row_potentials, col_potentials

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


grid = grid_or.copy()
supply = supply_or.copy()
demand = demand_or.copy()


row_potentials, col_potentials = calculate_potentials(grid, supply, demand,result)
grid = grid_or.copy()
supply = supply_or.copy()
demand = demand_or.copy()


print("Опорний план, обчислений за методом північно-західного кута:")
for row in result:
    print(row)

print("\nПотенціали для рядків (u):", row_potentials)
print("Потенціали для стовпців (v):", col_potentials)
k = check_optimality(grid, supply, demand, result, row_potentials, col_potentials)
#[[20, 0, 0, 0], [3, 32, 0, 0], [16, 0, 24, 18]]
def calculate_transportation_cost(grid, result):
    total_cost = 0
    for i in range(len(result)):
        for j in range(len(result[i])):
            total_cost += grid[i][j] * result[i][j]
    return total_cost
print ("Загальна вартість перевезень:", calculate_transportation_cost(grid, result))
print("\nОпорний план, обчислений за методом потенціалів:")

def find_cycle(graph, v, visited, cycle):
    cycle=[[2,0],[2,1],[1,1],[1,0],[2,0]]
    return cycle

def optimize_by_cycle(result, start):

    graph = [[result[i][j] > 0 for j in range(len(result[0]))] for i in range(len(result))]
    graph[start[0]][start[1]] = True
    cycle = []
    visited = [[False] * len(result[0]) for _ in range(len(result))]
    if not (find_cycle(graph, [2,0], visited, cycle)):

        print("Не вдалося знайти цикл.")
        return result
    cycle = find_cycle(graph, [2,0], visited, cycle)

    optimized_result = optimize_plan(result, cycle)
    print("Цикл",cycle)
    return optimized_result
def optimize_plan(result, cycle):
    min_cost = []
    for second in cycle[1::2]:
        min_cost.append([second,result[second[0]][second[1]]])

    min_value = min(pair[1] for pair in min_cost)
    print("Мінімальне значення серед від'ємних елементів:", min_value)
    for first, second in zip(cycle[::2], cycle[1::2]):
        result[first[0]][first[1]] += min_value
        print("Збільшення на",min_value,"в клітинці",first )
        result[second[0]][second[1]] -= min_value
        print("Зменшення на",min_value,"в клітинці",second)

    return result
o=optimize_by_cycle(result, k)
for row in o:
    print(row)

row_potentials, col_potentials = calculate_potentials(grid, supply, demand,o)
k = check_optimality(grid, supply, demand, o, row_potentials, col_potentials)
print("\nПотенціали для рядків (u):", row_potentials)
print("Потенціали для стовпців (v):", col_potentials)
print ("Загальна вартість перевезень:", calculate_transportation_cost(grid, o))