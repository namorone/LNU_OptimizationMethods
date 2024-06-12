import numpy as np
import matplotlib.pyplot as plt
from pulp import *

# Функції обмежень
def constraint1(x):
    return x -2

def constraint2(x):
    return  2 - x

def constraint3(x):
    return (x - 1) / 2



def abb_constreitn_to_model(model_):


    x1 = LpVariable("x1", lowBound=None, cat='Continuous')
    x2 = LpVariable("x2", lowBound=None, cat='Continuous')

    # Додавання обмежень
    model_ += x1 - x2 <= 2
    model_ += x1 + x2 <= 2
    model_ += x1 - 2 * x2 <= 1
    model_ += x1 >= 0
    model_ += x2 >= 0
    model_ += x1 + x2
    model_.solve()
    print(value(x1),value(x2))
    return value(x1),value(x2)


# Діапазон для x1
x_values = np.linspace(-10, 10, 400)

# Функція цільової функції
def objective_function(x1):
    return -x1 + 2

# Значення цільової функції на області допустимих значень
objective_values = objective_function(x_values)

model_max = LpProblem("Linear_Programming_Problem", LpMaximize)
max = abb_constreitn_to_model(model_max)
x_plvalues = np.linspace(0, 10, 400)
# Відображення області допустимих значень
plt.fill([0,1.667,1,0],[2,0.333,0,0], color='grey', alpha=0.5, label='ОДЗ')

x_pl2values = np.linspace(0, 10, 200)

# Графік обмежень
plt.plot(x_values, constraint1(x_values), label='x1 - x2 <= 2', color='blue')
plt.plot(x_values, constraint2(x_values), label='x1 + x2 <= 2', color='red')
plt.plot(x_values, constraint3(x_values), label='x1 - 2x2 <= 1', color='green')
plt.plot(x_pl2values,np.zeros_like(x_pl2values) , label='x1 >=0', color='yellow')
plt.plot(np.zeros_like(x_pl2values), x_pl2values, label='x2 >=0', color='orange')
plt.arrow(0, 0, 2, 2, head_width=0.5, head_length=0.7, fc='purple', ec='cyan', label='Gradient')


model_min = LpProblem("Linear_Programming_Problem", LpMinimize)
min = abb_constreitn_to_model(model_min)

# Мінімум та максимум цільової функції
plt.scatter(min[0], min[1], color='orange', label=f'Minimum F(x*) = {round(min[0],2)}+{round(min[1],2)} {round(min[0]+min[1],2)}')
plt.scatter( np.linspace(0, 1.667, 20),constraint2(np.linspace(0, 1.667, 20)) , color='purple', label=f'Maximum : F(x*) = {round(max[0]+max[1],2)}')

# Заголовок та підписи вісей
plt.title('Graphical Solution of Linear Programming Problem')
plt.xlabel('x1')
plt.ylabel('x2')

# Додавання легенди
plt.legend()

# Показ графіка
plt.grid(True)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.show()

