import numpy as np
from scipy.optimize import linprog

# Задання коефіцієнтів цільової функції та обмежень
c1 = [4, 3, 5, -20]  # Коефіцієнти цільової функції для першої задачі
A1 = [[1, 8, 7, -15], [-1, 5, 6, -11]]  # Коефіцієнти лівої частини нерівностей
b1 = [17, 9]  # Права частина нерівностей

c2 = [-6, -8, 1, -3]  # Коефіцієнти цільової функції для другої задачі
A2 = [[2, 5, 1, 2], [12, 6, 2, 1]]  # Коефіцієнти лівої частини нерівностей
b2 = [20, 72]  # Права частина нерівностей

# Розв'язання першої задачі
res1 = linprog(c1, A_eq=A1, b_eq=b1, method='highs')
print("Результати для першої задачі:")
print("Мінімум:", res1.fun)
print("Аргументи мінімуму:", res1.x)

# Розв'язання другої задачі
res2 = linprog(c2, A_eq=A2, b_eq=b2, method='highs')

print("\nРезультати для другої задачі:")
print("Мінімум:", res2.fun)
print("Аргументи мінімуму:", res2.x)

c3 = [1, 3, -1, -1,-1]  # Коефіцієнти цільової функції для другої задачі
A3 = [[1, -1, 1, 3, -3], [1, 1, -1, 1,1],[1,1,1,5,-1]]  # Коефіцієнти лівої частини нерівностей
b3 = [1, 1,5]  # Права частина нерівностей

res3 = linprog(c3, A_eq=A3, b_eq=b3, method='highs')
print("\nРезультати для другої задачі:")
print("Мінімум:", res3.fun)
print("Аргументи мінімуму:", res3.x)