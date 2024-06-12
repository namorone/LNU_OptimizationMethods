def f(x):
    return x ** 2 - x + 2

print (f(0.62) ,f(0.63))
def dichotomy_search(a, b, h):
    if b < a or h <= 0:
        return None

    n = int((b - a) / h) + 1

    interval = [a, b]

    for i in range(n):
        x1 = (interval[0] + interval[1] - h) / 2
        x2 = (interval[0] + interval[1] + h) / 2

        f1 = f(x1)
        f2 = f(x2)

        if f1 < f2:
            interval[1] = x2
        else:
            interval[0] = x1
        #print(interval[0], interval[1])
    return (interval[0] + interval[1]) / 2


a = -10
b = 10
h = 0.01

start_interval = dichotomy_search(a, b, h)

print("Початковий проміжок [a, b] для методу ламаних:", start_interval)


def f(x):
    return x ** 2 - x + 2


def golden_section_search(a, b, e):
    k = (3 - 5 ** 0.5) / 2

    x1 = a + k * (b - a)
    x2 = b - k * (b - a)
    f1 = f(x1)
    f2 = f(x2)
    iterations = 0

    while abs(b - a) > e:
        iterations += 1
        if f1 < f2:
            b = x2
            x2 = x1
            f2 = f1
            x1 = a + k * (b - a)
            f1 = f(x1)
        else:
            a = x1
            x1 = x2
            f1 = f2
            x2 = b - k * (b - a)
            f2 = f(x2)

    return (a + b) / 2, iterations


e = 0.01

minimum, iterations = golden_section_search(start_interval - h, start_interval + h, e)

print("Мінімум функції f(x) =", minimum)
print("Кількість ітерацій методу ламаних =", iterations)