# Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания
# все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.

# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.

n = int(input('Введите количество элементов первого множества: '))
m = int(input('Введите количество элементов второго множества: '))

a = list(map(int, input('Введите элементы первого множества: ').split()))
b = list(map(int, input('Введите элементы второго множества: ').split()))

result = list(set(a) & set(b))
result.sort()
print(result)