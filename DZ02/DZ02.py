# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# 2 2
# 4
def summa(a,b):
    if b >= 0:
        if b == 0:
            return a
        else:
            return summa(a, b-1)+1
    if b < 0:
        if b == 0:
            return a
        else:
            return summa(a, b+1)-1
print(summa(a=int(input("Введите число a: ")), b=int(input("Введите число b "))))