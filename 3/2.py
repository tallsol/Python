# Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai. Последняя строка
# содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5

n = int(input("Введите количество элементов массива: "))
import random
array = [random.randint(1,10) for i in range(n)]
print (array)

x = int(input("Введите число, к которому будем искать ближайший элемент в массиве: "))
for i in array:
    if i == x:
        break
    else:
        m = min(array, key=lambda i: abs(i - x))
print(f"Ближайший элемент - {m} ")