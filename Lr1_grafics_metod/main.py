from pulp import *

# Створення моделі для задачі лінійного програмування
model = LpProblem("Linear_Programming_Problem", LpMinimize)#LpMinimize

# Оголошення змінних
x1 = LpVariable("x1", lowBound=None, cat='Continuous')
x2 = LpVariable("x2", lowBound=None, cat='Continuous')

# Додавання обмежень
model += x1 - x2 >= 3
model += x1 + 5*x2 >= 5
model += 2*x1 + x2 >= 4

# Додавання цільової функції
model += 7*x1 + 5*x2

# Вирішення задачі
model.solve()

# Вивід результатів
print("Optimal solution:")
print("x1 =", value(x1))
print("x2 =", value(x2))
print("Objective function value (minimized):", value(model.objective))

