# Требуется вывести все целые степени двойки (т.е. числа
# вида 2^k), не превосходящие числа N.
# 10 -> 1 2 4 8

n = int(input("Введите число: "))
m = 1
while m < n:
    print(m, end=' ')
    m = m * 2