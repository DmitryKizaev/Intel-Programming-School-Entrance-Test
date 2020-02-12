"""Отборочное задание на школу Intel N1"""

# Есть 2 массива, A и B, вывести третий массив C как сумму таким образом:
# Элемент 1: сумма наименьшего из A c наибольшим из B
# Элемент 2: сумма 2-го наименьшего из A cо 2-м наибольшим из B
# и так далее

# Python 3.8
# В Python в роли "массивов" вполне могут выступить списки, реализуем через них


def list_inp(N):
    """Allows to enter a list and prints the result"""
    lin = list()
    for i in range(1, N+1):
        print("Enter element", i)
        lin.append(int(input()))
    return lin


print("Enter N")
N = int(input())
print("Enter massive ""A"":")
A = list_inp(N)
print("Enter massive ""B"":")
B = list_inp(N)

A.sort()
B.sort(reverse=True)

result = []
for i in range(N):
    result.append(int(A[i] + B[i]))
print(result)
