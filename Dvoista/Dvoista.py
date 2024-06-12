import numpy as np
import pandas as pd

def simplex_method_case1(c, table, Vb):
    table_privious=table.copy()
    table_next=table.copy()
    Vb_privious=Vb.copy()
    Vb_next=Vb.copy()
    vb_b=True

    basis =[]

    i = 0

    while True:
        print(f"Ітерація: {i+1}")

        if i == 0:
            basis = first_basis(table_privious)
        #     print(table_privious, Vb_privious, basis)
        #print(table_privious, Vb_privious, basis)
        if basis == False:
            return False


        delta = find_delta(table_privious, basis, c)
        # print(delta)
        simplex_table=create_simplex_table(c, table_privious, Vb_privious, delta, basis)
        print(simplex_table)
        if np.all(delta >= 0):
            print('Функція оптимальна')
            new_arr = np.zeros_like(c)
            new_arr[basis] = Vb_privious
            print(f'x*={new_arr}')
            new_arr[basis]=new_arr[basis]*c[basis]
            print(f'F(x*)={sum(new_arr)}')
            return False
        if i == 0:
            max_delta_index = np.argmax(delta[np.nonzero(delta)])
        else:
            max_delta_index = np.where(delta == np.min(delta[np.nonzero(delta)]))[0][0]


        Vb_min,Vb_min_index,Vb_b = find_min_Vb(Vb_privious,table_privious,max_delta_index)
        if not (Vb_min or Vb_min_index or Vb_b):
            vb_b = False

        if vb_b == False:
            return False

        Vb_next ,table_next = update_table(np.hstack((table_privious, np.array(Vb_privious)[:, np.newaxis])), Vb_min_index, max_delta_index)
        basis[Vb_min_index]=max_delta_index
        table_privious = table_next
        Vb_privious =Vb_next

        i = i + 1

def first_basis(table):
    basis = [];

    for i in range(len(table)):
        for j in range(len(table[0])):
            if table[i][j] == 1:
                c = 0
                for k in range(len(table)):
                    if table[k][j] == 0:
                        c = c + 1
                if c == len(table) - 1:
                    basis.append(j)

    if len(basis)==0 or len(basis)==1:
        print("початковий базис помилка")
        return False
    return basis

def find_delta(table,basis,cj):
    fd = []
    for i in range(len(table)):
        if i == 0:
            fd.append(table[i]*cj[basis[i]])
        elif i>0:
            fd=fd + (table[i] * cj[basis[i]])
    #fd=(table[0]*cj[basis[0]]+table[1]*cj[basis[1]])-cj
    fd = fd - cj

    return fd[0]

def find_min_Vb(Vb,table,max_delta_index):
    result=[];
    index=[];
    for i in range(len(Vb)):
        if (Vb[i]/table[i][max_delta_index])>=0:
            if table[i][max_delta_index] == 0:
                continue
            else:
                result.append(Vb[i]/table[i][max_delta_index])
                index.append(i)

    if len(result)==0 or result[0] == -0.0:
        print('Усі Vb менші нуля. Функція не обмежена. Оптимальне рішення відсутнє.')
        return False,False,False
    print(max_delta_index,result)
    min_Vb = min(result)
    min_Vb_in = np.argmin(result)
    index_Vb = index[min_Vb_in]
    print(min_Vb,index_Vb)
    return min_Vb,index_Vb,True

def update_table(table, pivot_row, pivot_col):
    num_rows, num_cols = table.shape
    pivot_element = table[pivot_row, pivot_col]
    table=table.astype(float)

    # Ділимо ведучий рядок на ведучий елемент, щоб зробити його 1
    table[pivot_row, :] /= pivot_element

    # Обчислення нових значень для інших рядків
    for i in range(num_rows):
        if i == pivot_row:
            continue
        ratio = -table[i, pivot_col] / table[pivot_row, pivot_col]
        table[i, :] += ratio * table[pivot_row, :]

    return  table[:, -1],np.delete(table, -1, axis=1)

def create_simplex_table(c, table, b, delta,basis):
    df_A = pd.DataFrame(table, columns=[f'x{i}' for i in range(1, table.shape[1] + 1)])
    df_b = pd.DataFrame(b, columns=['Vb'])
    df = pd.concat([df_A, df_b], axis=1)
    df.index = ['x' + str(i+1) for i in basis]
    # Створюємо DataFrame для значень дельта
    delta = np.array(delta, dtype=object)
    delta=np.append(delta, " ")
    df.loc['Δ']=delta
    c=np.array(c, dtype=object)
    c=np.append(c, " ")
    custom_df = pd.DataFrame([c], columns=df.columns, index=['Cj'])

    # Об'єднуємо з поточним DataFrame
    df = pd.concat([custom_df, df])
    return df

M=10000;
c1 = np.array([4, 3, 5, -20, M, M])
A1 = np.array([[1, 8, 7, -15, 1, 0], [-1, 5, 6, -11, 0, 1]])
b1 = np.array([17, 9])
basis1 = [4, 5]

# simplex_method_case1(c1, A1, b1)

c2 = np.array([-6, -8, 1, 3, 0, M])
A2 = np.array([[2, 5, 1, 2, 0, 1], [12, 6, 2, 1, 1, 0]])
b2 = np.array([20, 72])
# simplex_method_case1(c2, A2, b2)

# print(first_basis1(A2))
#
# a3=[[2, 5, 1, 2, 0, 1, 0],[1, 7, 1, 2, 0, 0, 1], [12, 6, 2, 1, 1, 0, 0]]
# print(first_basis1(a3))

c3 = np.array([5,8,1,0,0,0])
A3 = np.array([[2,1,-1,1,0,0], [-1,0,-2,0,1,0], [3,2,0,0,0,1]])
b3 = np.array([1,-1,3])
simplex_method_case1(c3, A3, b3)