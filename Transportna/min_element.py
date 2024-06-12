# Функція для перевірки валідності векторів запасів і потреб


def validate_vectors(supply, demand):
    total_supply = sum(supply)
    total_demand = sum(demand)
    if total_supply != total_demand:
        raise ValueError("Total supply and demand do not match")

# Функція для розв'язання транспортної задачі
def transport(supply, demand, costs):
    grid = []
    for i in range(len(supply)):
        row = []
        for j in range(len(demand)):
            row.append(0)
        grid.append(row)

    while True:
        # знаходимо мінімальну ціну
        min_cost = float('inf')
        for i in range(len(supply)):
            for j in range(len(demand)):
                if supply[i] > 0 and demand[j] > 0 and costs[i][j] < min_cost:
                    min_cost = costs[i][j]

        # якщо мінімальна ціна не знайдена, закінчуємо
        if min_cost == float('inf'):
            break

        # знаходимо всі клітинки з мінімальною ціною і заповнюємо їх
        for i in range(len(supply)):
            for j in range(len(demand)):
                if supply[i] > 0 and demand[j] > 0 and costs[i][j] == min_cost:
                    amount = min(supply[i], demand[j])
                    grid[i][j] += amount
                    supply[i] -= amount
                    demand[j] -= amount

    return grid

def print_min_cost(costs, solution):
    total_cost = 0
    for i in range(len(solution)):
        row = solution[i]
        for j in range(len(row)):
            amount = row[j]
            if amount > 0:
                cost = costs[i][j]
                total_cost += amount * cost
    print(f"Minimum cost: {total_cost}")



costs = [[6,5,9,8], [6,4,8,6], [9,8,4,7]]
supply = [20, 35, 55]
demand = [36, 32, 24, 18]
solution = transport(supply, demand, costs)

#print_solution(solution)
print_min_cost(costs, solution)


for i, j, amount, cost in solution:
    print(f"Moving {amount} units from source {i} to destination {j} at a cost of {cost}.")