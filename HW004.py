# 1. Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
# import math
# n = int(input("Введите количество цифр после запятой -> "))
# temp = '{:.' + str(n) + 'f}'
# print(temp.format(math.pi))

# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# N = int(input("Введите натуральное число -> "))
# i = 2
# while N >= i:
#     while N % i == 0:
#         print(i, end=' ')
#         N //= i
#     i += 1

# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# num_list = [23, 56, 89, 23, 55, 89, 56, 9]

# num_dict = {}
# for i in num_list:
#     num_dict[i] = num_dict.get(i, 0) + 1

# new_list = [key for key, value in num_dict.items() if value == 1]
# print(f'Список неповторяющихся элементов: {new_list}')

# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.

# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# 5. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
