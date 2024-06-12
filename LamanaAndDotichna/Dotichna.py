import numpy as np
import matplotlib.pyplot as plt

def F(x):
    return x**2 - x + 2

def F_prime(x):
    return 2 * x - 1

def F_double_prime(x):
    return 2
def dsk_method(F, x0, h):
    F_x0 = F(x0)
    F_x_minus_h = F(x0 - h)
    F_x_plus_h = F(x0 + h)

    if F_x_minus_h >= F_x0 <= F_x_plus_h:
        return x0 - h, x0 + h
    elif F_x_minus_h < F_x0:
        i = 1
        while F(x0 - h) < F(x0):
            x0 = x0 - i*h
            i+=1
        return x0 - i*h, x0
    elif F_x_plus_h < F_x0:
        i = 1
        while F(x0 + h) < F(x0):
            x0 = x0 + i*h
            i+=1
        return x0, x0 + i*h
def newtons_method(F, F_prime, F_double_prime, x0, epsilon):
    x_values = [x0]
    iterations = 0
    while True:
        x_new = x0 - F_prime(x0) / F_double_prime(x0)
        x_values.append(x_new)
        if abs(x_new - x0) < epsilon:
            break
        x0 = x_new
        iterations += 1
    return x_values

# Вхідні дані
x0 = 3
epsilon = 0.01
h = 2
a, b = dsk_method(F, x0, h)
# Знаходження мінімуму методом дотичних
x_values = newtons_method(F, F_prime, F_double_prime, a+b/2, epsilon)
optimal_x = x_values[-1]
optimal_F = F(optimal_x)
print("Мінімум функції:", optimal_F, "в точці", optimal_x,"за ",len(x_values)-1," ітерацій")
# Побудова графіка
x_plot = np.linspace(-5, 3.5, 400)
f_plot = F(x_plot)

plt.figure(figsize=(10, 6))
plt.plot(x_plot, f_plot, label='F(x)')
plt.scatter(optimal_x, optimal_F, color='red', label='Minimum', zorder=5)

# Візуалізація ітерацій
for i in range(len(x_values) - 1):
    x = x_values[i]
    tangent_x = np.linspace(x - 1, x + 1, 100)
    tangent_y = F(x) + F_prime(x) * (tangent_x - x)
    plt.scatter(x, F(x), color='blue', zorder=5)
    plt.plot([x, x], [0, F(x)], linestyle='--', color='gray')
    plt.plot(tangent_x, tangent_y, linestyle='--', color='orange', label=f'Tangent at x{i}' if i == 0 else "")

plt.title('Графік функції та метод дотичних')
plt.xlabel('x')
plt.ylabel('F(x)')
plt.legend()
plt.grid(True)
plt.show()
