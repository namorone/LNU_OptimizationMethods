# def find_cycle(graph, v, visited, cycle):
#     x, y = v
#     if visited[x][y]:
#         return True
#     visited[x][y] = True
#     cycle.append(v)
#     print(cycle)
#     # Перевірка сусідів вершини v
#     for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
#         nx, ny = x + dx, y + dy
#         print(nx,ny)
#         if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]) and graph[nx][ny]:
#             if (nx, ny) in cycle[:-1]:
#                 # Цикл знайдено
#                 cycle.append((nx, ny))
#                 print(cycle,'cycle1')
#                 return True
#             if find_cycle(graph, (nx, ny), visited, cycle):
#                 print(cycle,'cycle2')
#                 return True,
#     # З цієї вершини немає циклу
#     cycle.pop()
#     return False
#     print (cycle,'cycle')
#
#
# def optimize_plan(result, cycle):
#     # Find the minimum quantity in the cycle
#     min_quantity = min(result[cycle[i[0]]][cycle[i[1]]] for i in zip(range(len(cycle)), range(1, len(cycle))) if
#                        result[cycle[i[0]]][cycle[i[1]]] > 0)
#
#     # Update the result by adjusting the quantities along the cycle
#     for i in zip(range(len(cycle)), range(1, len(cycle))):
#         result[cycle[i[0]]][cycle[i[1]]] += min_quantity
#         if result[cycle[i[0]]][cycle[i[1]]] == 0:
#             result[cycle[i[1]]][cycle[i[0]]] -= min_quantity
#
#     return result
#
#
# def optimize_by_cycle(result, start):
#     # Create a graph representing the current result
#     graph = [[result[i][j] > 0 for j in range(len(result[0]))] for i in range(len(result))]
#     graph[start[0]][start[1]] = True
#     print (graph)
#     # Initialize variables
#     cycle = []
#     visited = [[False] * len(result[0]) for _ in range(len(result))]
#     print (visited)
#     # Find a cycle in the graph
#     print(find_cycle(graph, [2,0], visited, cycle))
#
#         # print("Не вдалося знайти цикл.")
#         # return result
#
#     # Optimize the result using the found cycle
#     optimized_result = optimize_plan(result, cycle)
#
#     return optimized_result
#
#
# # Приклад використання
# result = [[20, 0, 0, 0], [16, 19, 0, 0], [0, 13, 24, 18]]
# optimized_result = optimize_by_cycle(result, [2,0])
# print("Оптимізований план:")
# for row in optimized_result:
#     print(row)

import networkx as nx

def optimize_by_cycle(result):
    # Створення графа, що представляє поточний результат
    graph = nx.Graph()
    for i in range(len(result)):
        for j in range(len(result[0])):
            if result[i][j] > 0:
                graph.add_edge((i, j), (i+1, j), weight=result[i][j])
                graph.add_edge((i, j), (i, j+1), weight=result[i][j])
    # Знайдемо всі цикли у графі
    cycles = list(nx.simple_cycles(graph))
    if not cycles:
        print("Не вдалося знайти цикл.")
        return result
    else:
        print("Цикли знайдено:", cycles)
        return cycles

result = [[20, 0, 0, 0], [16, 19, 0, 0], [0, 13, 24, 18]]
optimize_by_cycle(result)