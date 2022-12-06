# DZ_4
# # 4_1. Вычислить число Пи c заданной точностью d
# import math

# d = int(input("задайте точность числа π : "))

# if d < 1 or d > 10:
#     print("точность выходит за границы диапазона")
# else:
#     pi = str(math.pi)
#     print(pi[0 : (d + 2)])
#
# 4_2. Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа
# n = int(input("задайте натуральное число N : "))
# mass = []
# i = 2
# while n != 1 or i < n:
#     if n % i == 0:
#         mass.append(i)
#         n = n / i
#         i = 2
#     else:
#         i = i + 1
# print(mass)
# 4_3. Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.
# from random import randint

# N = int(input("Введите число N: "))
# mass = []

# for i in range(N):
#     mass.append(randint(0, N))
# print(mass)
# mass2 = []
# for i in mass:
#     if mass.count(i) == 1:
#         mass2.append(i)
# print(mass2)
# 4_4. Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.
# from random import randint
# import itertools

# k = int(input("задайте натуральную степень k : "))


# def get_ratios(k):
#     ratios = [randint(0, 10) for i in range(k + 1)]
#     while ratios[0] == 0:
#         ratios[0] = randint(1, 10)
#     return ratios


# def get_polynomial(k, ratios):
#     var = ["*x^"] * (k - 1) + ["*x"]
#     polynomial = [
#         [a, b, c]
#         for a, b, c in itertools.zip_longest(ratios, var, range(k, 1, -1), fillvalue="")
#         if a != 0
#     ]
#     for x in polynomial:
#         x.append(" + ")
#     polynomial = list(itertools.chain(*polynomial))
#     polynomial[-1] = " = 0"
#     return "".join(map(str, polynomial)).replace(" 1*x", " x")


# ratios = get_ratios(k)
# polynom1 = get_polynomial(k, ratios)
# print(polynom1)

# with open("polinom.txt", "w") as data:
#     data.write(polynom1)
# 4_5. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму
# import random


# def write_file(name, st):
#     with open(name, "w") as data:
#         data.write(st)


# def rnd():
#     return random.randint(0, 101)


# def create_mn(k):
#     lst = [rnd() for i in range(k + 1)]
#     return lst


# def create_str(sp):
#     lst = sp[::-1]
#     wr = ""
#     if len(lst) < 1:
#         wr = "x = 0"
#     else:
#         for i in range(len(lst)):
#             if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
#                 wr += f"{lst[i]}x^{len(lst)-i-1}"
#                 if lst[i + 1] != 0 or lst[i + 2] != 0:
#                     wr += " + "
#             elif i == len(lst) - 2 and lst[i] != 0:
#                 wr += f"{lst[i]}x"
#                 if lst[i + 1] != 0 or lst[i + 2] != 0:
#                     wr += " + "
#             elif i == len(lst) - 1 and lst[i] != 0:
#                 wr += f"{lst[i]} = 0"
#             elif i == len(lst) - 1 and lst[i] == 0:
#                 wr += " = 0"
#     return wr


# def sq_mn(k):
#     if "x^" in k:
#         i = k.find("^")
#         num = int(k[i + 1 :])
#     elif ("x" in k) and ("^" not in k):
#         num = 1
#     else:
#         num = -1
#     return num


# def k_mn(k):
#     if "x" in k:
#         i = k.find("x")
#         num = int(k[:i])
#     return num


# def calc_mn(st):
#     st = st[0].replace(" ", "").split("=")
#     st = st[0].split("+")
#     lst = []
#     l = len(st)
#     k = 0
#     if sq_mn(st[-1]) == -1:
#         lst.append(int(st[-1]))
#         l -= 1
#         k = 1
#     i = 1
#     ii = l - 1
#     while ii >= 0:
#         if sq_mn(st[ii]) != -1 and sq_mn(st[ii]) == i:
#             lst.append(k_mn(st[ii]))
#             ii -= 1
#             i += 1
#         else:
#             lst.append(0)
#             i += 1

#     return lst


# k1 = int(input("Введите натуральную степень для первого файла k = "))
# k2 = int(input("Введите натуральную степень для второго файла k = "))
# koef1 = create_mn(k1)
# koef2 = create_mn(k2)
# write_file("file34_1.txt", create_str(koef1))
# write_file("file34_2.txt", create_str(koef2))


# with open("file34_1.txt", "r") as data:
#     st1 = data.readlines()
# with open("file34_2.txt", "r") as data:
#     st2 = data.readlines()
# print(f"Первый многочлен {st1}")
# print(f"Второй многочлен {st2}")
# lst1 = calc_mn(st1)
# lst2 = calc_mn(st2)
# ll = len(lst1)
# if len(lst1) > len(lst2):
#     ll = len(lst2)
# lst_new = [lst1[i] + lst2[i] for i in range(ll)]
# if len(lst1) > len(lst2):
#     mm = len(lst1)
#     for i in range(ll, mm):
#         lst_new.append(lst1[i])
# else:
#     mm = len(lst2)
#     for i in range(ll, mm):
#         lst_new.append(lst2[i])
# write_file("file34_res.txt", create_str(lst_new))
# with open("file34_res.txt", "r") as data:
#     st3 = data.readlines()
# print(f"Результирующий многочлен {st3}")
# 5_1 вариант человек против человека:
# from random import randint


# def input_dat(name):
#     x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
#     while x < 1 or x > 28:
#         x = int(input(f"{name}, введите корректное количество конфет: "))
#     return x


# def p_print(name, k, counter, value):
#     print(
#         f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет."
#     )


# player1 = input("Введите имя первого игрока: ")
# player2 = input("Введите имя второго игрока: ")
# value = int(input("Введите количество конфет на столе: "))
# flag = randint(0, 2)  # флаг очередности
# if flag:
#     print(f"Первый ходит {player1}")
# else:
#     print(f"Первый ходит {player2}")

# counter1 = 0
# counter2 = 0

# while value > 28:
#     if flag:
#         k = input_dat(player1)
#         counter1 += k
#         value -= k
#         flag = False
#         p_print(player1, k, counter1, value)
#     else:
#         k = input_dat(player2)
#         counter2 += k
#         value -= k
#         flag = True
#         p_print(player2, k, counter2, value)

# if flag:
#     print(f"Выиграл {player1}")
# else:
#     print(f"Выиграл {player2}")

# 5_1
# # вариант человек против бота:
# from random import randint


# def input_dat(name):
#     x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
#     while x < 1 or x > 28:
#         x = int(input(f"{name}, введите корректное количество конфет: "))
#     return x


# def p_print(name, k, counter, value):
#     print(
#         f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет."
#     )


# player1 = input("Введите имя первого игрока: ")
# player2 = "Bot"
# value = int(input("Введите количество конфет на столе: "))
# flag = randint(0, 2)  # флаг очередности
# if flag:
#     print(f"Первый ходит {player1}")
# else:
#     print(f"Первый ходит {player2}")

# counter1 = 0
# counter2 = 0

# while value > 28:
#     if flag:
#         k = input_dat(player1)
#         counter1 += k
#         value -= k
#         flag = False
#         p_print(player1, k, counter1, value)
#     else:
#         k = randint(1, 29)
#         counter2 += k
#         value -= k
#         flag = True
#         p_print(player2, k, counter2, value)

# if flag:
#     print(f"Выиграл {player1}")
# else:
#     print(f"Выиграл {player2}")
