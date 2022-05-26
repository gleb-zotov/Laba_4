import random
import time

def print_matrix(M, matr_name, tt):
    print("матрица " + matr_name + " промежуточное время = " + str(format(tt, '0.2f')) + " seconds.")
    for i in M:  # делаем перебор всех строк матрицы
        for j in i:  # перебираем все элементы в строке
            print("%5d" % j, end=' ')
        print()

print("\n-----Результат работы программы-------")
try:
    row_q = int(input("Введите количество строк (столбцов) квадратной матрицы в интервале от 6 до 100:"))
    while row_q < 6 or row_q > 100:
        row_q = int(input(
            "Вы ввели неверное число\nВведите количество строк (столбцов) квадратной матрицы в интервале от 6 до 100:"))
    K = int(input("Введите число К="))
    start = time.time()
    A, F, FA, AT = [], [], [], []  # задаем матрицы
    for i in range(row_q):
        A.append([0] * row_q)
        F.append([0] * row_q)
        FA.append([0] * row_q)
        AT.append([0] * row_q)
    time_next = time.time()
    print_matrix(F, "F", time_next - start)

    for i in range(row_q):                                   # заполняем матрицу А
        for j in range(row_q):
            A[i][j] = random.randint(-10, 10)
    time_prev = time_next
    time_next = time.time()
    print_matrix(A, "A", time_next - time_prev)

    for i in range(row_q):  # F
        for j in range(row_q):
            F[i][j] = A[i][j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(F, "F", time_next - time_prev)

    size= row_q // 2
    flag = 0
    for i in range(row_q):                                        # обработка матрицы A
        for j in range(row_q):
            if i<j and A[i][j]==A[j][i]:
                flag+=1

    if flag==(row_q*row_q-row_q)/2:
        print("A симметрична относительно главной диагонали")
    else:
        print("A несимметрична относительно главной диагонали")

    if flag==(row_q*row_q-row_q)/2:                                                         # формируем F по условию
        print("меняем в В симметрично области 1 и 3 местами")
        for i in range(size + row_q % 2 + 1):
            for j in range(size + row_q % 2 + 1, row_q, 1):
                if i - size - row_q % 2 < j and i - size - row_q % 2 < size - j - 1:
                    buffer = F[i][j]
                    F[i][j] = F[size+i-1][j]
                    F[size+i-1][j] = buffer
    else:
        print("меняем С и Е местами")
        for j in range(size):
            for i in range(size):
                F[i][j], F[size + row_q % 2 + i][size + row_q % 2 + j] = F[size + row_q % 2 + i][size + row_q % 2 + j], F[i][j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(F, "Измененная F", time_next - time_prev)

                                                                           #К * (F+A) * A^T – A^T + F
    print_matrix(A, "A", 0)

    for i in range(row_q):  # F+A
        for j in range(row_q):
            s=0
            for m in range(row_q):
                s = s + F[i][m] + A[m][j]
            FA[i][j] = s
    time_prev = time_next
    time_next = time.time()
    print_matrix(FA, "F+A", time_next - time_prev)

    for i in range(row_q):                 # K * (F+A)
        for j in range(row_q):
            FA[i][j] = K * FA[i][j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(AT, "K * (F+A)", time_next - time_prev)

    for i in range(row_q):  # A^T
        for j in range(i, row_q, 1):
            AT[i][j], AT[j][i] = A[j][i], A[i][j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(AT, "A^T", time_next - time_prev)

    for i in range(row_q):                  # К * (F+A) * A^T
        for j in range(row_q):
            FA[i][j] = AT[i][j] * FA[i][j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(A, "К * (F+A) * A^T", time_next - time_prev)

    for i in range(row_q):                     # К * (F+A) * A^T – A^T
        for j in range(row_q):
                FA[i][j]=FA[i][j]-AT[i][j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(FA, "К * (F+A) * A^T – A^T", time_next - time_prev)


    for i in range(row_q):                     # К * (F+A) * A^T – A^T + F
        for j in range(row_q):
            FA[i][j] = FA[i][j] + F[i][j]
    time_prev = time_next
    time_next = time.time()
    print_matrix(FA, "К * (F+A) * A^T – A^T + F", time_next - time_prev)

    finish = time.time()
    result = finish - start
    print("Program time: " + str(result) + " seconds.")


except ValueError:
    print("\nэто не число")