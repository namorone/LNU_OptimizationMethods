import numpy as np
import copy
# A will contain the coefficients of the constraints
A = np.array([[2, -1, 3], [1, 0, 2], [-1, -2, 0]])
# b will contain the amount of resources
b = np.array([5, 8, 1])
# c will contain coefficients of objective function Z
c = np.array([1, -1, 3])

# Створення двоїстої матриці A_T
A_T = A.transpose()

# Створення двоїстого вектора c_T
c_T = b.transpose()

# Створення двоїстого вектора b_T
b_T = c.transpose()

m, n = 3, 3

# A will contain the coefficients of the constraints
A = A_T.tolist()
A[0].append(1)
A[0].append(0)
A[0].append(0)
A[1].append(0)
A[1].append(1)
A[1].append(0)
A[2].append(0)
A[2].append(0)
A[2].append(1)
# b will contain the amount of resources
b = b_T.tolist()
# c will contain coefficients of objective function Z
c =c_T.tolist()
c.append(0)
c.append(0)
c.append(0)
# Вивід двоїстої матриці A_T, двоїстого вектора c_T та двоїстого вектора b_T
print("Двоїста матриця A_T: ")
print(A)
print("\nДвоїстий вектор c_T: ")
print(c)
print("\nДвоїстий вектор b_T: ")
print(b)

bazis = []
k1=0
temp=0
print("Початкова симплекс таблиця: ", A)
for i in range(m):
    do = True
    for j in range(n):
        do1 = True
        if A[i][j]==1 and do:
            for k in range(m):
                if A[k][j]!=0 and i!=k:
                    do1=False
        else:
            do1=False
        if (do1):
            do = False
            bazis.append(j+1)
if len(bazis)!=m:
    bazis.clear()
    n+=m
    for i in range(m):
        for j in range(m):
            if i==j:
                A[i].append(1.0)
            else:
                A[i].append(0.0)
        bazis.append(n+i-1)
        c.append(0)
for i in range(m):
    A[i].append(b[i])
    A[i].append(bazis[i])
stop = 0
while (stop<=5):
    print("Індекси базисних змінних: ", bazis)
    print("Заключна симплекс таблиця: ", A)
    #вектор b
    b=0.0
    for i in range(m):
        b+=A[i][n]*c[int(A[i][n+1]-1)]
    print("Обчислене начення функції",b)
    Aj=list()
    temp=0.0
    for i in range(n):
        for j in range(m):
            temp+= A[j][i] * c[int(A[j][n + 1] - 1)]
        Aj.append(temp-c[i])
        temp=0
    print("Δ: ", Aj)
    if any([element > 0 for element in Aj])==False:
        break
    else:
        res=-1
        for i in range(n):
            if max(Aj)==Aj[i] and res==-1:
                res=i

        min= 2147483647
        min_i=0
        for i in range(m):
            if A[i][res]>0:
                if min>A[i][n]/A[i][res]:
                    min=A[i][n]/A[i][res]
                    min_i=i
        bazis[min_i]=res+1
        new_A=[]

        for i in range(m):
            row=list()
            for j in range(n+1):
                if i != min_i:
                    row.append(A[i][j] - (A[i][res] * A[min_i][j]) / A[min_i][res])
                else:
                    row.append(A[min_i][j] / A[min_i][res])
            row.append(bazis[i])
            new_A.append(row)

        A=copy.deepcopy(new_A)
        stop = stop + 1