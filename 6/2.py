# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

a = list(map(int, input('Введите массив: ').split()))

mini = int(input('Введите начало диапазона: '))
maxi = int(input('Введите конец диапазона: '))
print(*[i for i in range(len(a)) if mini <= a[i] <= maxi])

N = int(input("Введите число элементов массива: "))
min = int(input("Введите минимальное значение заданного диапазона: "))
max = int(input("Введите максимальное значение заданного диапазона: "))

import random
array = []
for i in range(N):
    array.append(random.randint(-10, 11))
print(array)

index_list = []
for i in range(len(array)):
    if array[i] >= min and array[i] <= max:
        index_list.append(i)

print(index_list)