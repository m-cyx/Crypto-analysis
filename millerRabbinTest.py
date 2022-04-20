# Рабочий тест Миллера-Рабина + стандартная проверка на простоту

import time
from random import randint
from datetime import datetime

def isPrime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n

# производится k раундов проверки числа n на простоту
def MillerRabinTest(n, k):
    # если n == 2 или n == 3 - эти числа простые, возвращаем True
    if (n == 2 or n == 3):
        print('выход 1')
        return True

    # если n < 2 или n четное - возвращаем False
    if (n < 2 or n % 2 == 0):
        print('выход 2')
        return False
        
    # представим n − 1 в виде(2 ^ s)·t, где t нечётно, это можно сделать последовательным делением n - 1 на 2
    t = n - 1
    s = 0

    while (t % 2 == 0):
        t /= 2
        t = int(t)
        s += 1

    # повторить k раз
    for i in range(1, k + 1):
        # выберем случайное целое число a в отрезке[2, n − 2]
        a = randint(2, n - 2)

        # x ← a ^ t mod n, вычислим с помощью возведения в степень по модулю
        x = pow(a, t, n)
        
        # если x == 1 или x == n − 1, то перейти на следующую итерацию цикла
        if (x == 1 or x == n - 1):
            continue

        # повторить s − 1 раз
        for i in range(1, s):
            # x ← x ^ 2 mod n
            x = pow(x, 2, n)

            # если x == 1, то вернуть "составное"
            if (x == 1):
                print('выход 3')
                return False

            # если x == n − 1, то перейти на следующую итерацию внешнего цикла
            if (x == n - 1):
                break

        if (x != n - 1):
            print('выход 4')
            return False

    # вернуть "вероятно простое"
    print('выход 5')
    return True


number = 2708829427
number2 = '10100001011101010111010011110011'


# Засекаю начальное время
start_time = datetime.now()

print(str(isPrime(number)))

# Вывожу конечное время
print('Время затраченное на точную проверку: ')
print(datetime.now() - start_time)

# Засекаю начальное время
start_time = datetime.now()

print(str(MillerRabinTest(number,50)))

# Вывожу конечное время
print('Время затраченное на тест Миллера Рабина: ')
print(datetime.now() - start_time)

# (int(number2, 2)) - перевод двоичной строки в десятичное 

