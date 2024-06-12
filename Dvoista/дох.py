import numpy as np

# Припустимо, що delta - це ваш масив з числами
delta = np.array([0, 3, 7, 0, 9, 0, 2])

# Знаходимо індекс максимального ненульового елемента
max_nonzero_index = np.where(delta == np.min(delta[np.nonzero(delta)]))[0][0]

print("Індекс максимального ненульового елемента:", max_nonzero_index)