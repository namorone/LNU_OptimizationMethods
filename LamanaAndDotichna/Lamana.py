import numpy as np
import matplotlib.pyplot as plt


def F(x):
    return x ** 2 - x + 2


def cutting_plane_method(F, a, b, epsilon):
    intervals = []
    while (b - a) > epsilon:
        mid = (a + b) / 2
        intervals.append((a, b, mid))
        if F(mid - epsilon / 2) < F(mid + epsilon / 2):
            b = mid
        else:
            a = mid
    intervals.append((a, b, (a + b) / 2))
    return (a + b) / 2, intervals


# Визначення початкового інтервалу методом ДСК
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


# Вхідні дані
x0 = 3
h = 3
epsilon = 0.01

# Визначення інтервалу [a, b]
a, b = dsk_method(F, x0, h)

# Знаходження мінімуму методом ламаних
optimal_x, intervals = cutting_plane_method(F, a, b, epsilon)
optimal_F = F(optimal_x)
print(f"Початковий проміжок [{a, b}] для методу ламаних")
print(f"Кількість ітерацій: {len(intervals) - 1}")
print("Мінімум функції:", optimal_F, "в точці", optimal_x)
# Побудова графіка
x_values = np.linspace(a - h, b + h, 400)
f_values = F(x_values)

plt.figure(figsize=(10, 6))
plt.plot(x_values, f_values, label='F(x)')
plt.scatter(optimal_x, optimal_F, color='red', label='Minimum', zorder=5)

# Візуалізація ламаних
for (a_i, b_i, mid_i) in intervals:
    plt.plot([a_i, b_i], [F(a_i), F(b_i)], linestyle='--', color='gray')
    plt.scatter([a_i, b_i], [F(a_i), F(b_i)], color='blue', zorder=5)

plt.title('Графік функції та методу ламаних')
plt.xlabel('x')
plt.ylabel('F(x)')
plt.legend()
plt.grid(True)
plt.show()
