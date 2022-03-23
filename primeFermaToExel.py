import pandas as pd
from datetime import datetime
import time

# Оптимизированная проверка на простоту
def isPrime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n

# Оптимизация теста Ферма - смотрю только на нечётные числа. 2х прирост скорости
def isPrimeFerma(a, n):  # а - основание для проверки, n - само число
    if n % 2 != 0:
        if a**(n-1) % n == 1:
            return True
        else:
            return False
    else:
        return False

# Засекаю начальное время
start_time = datetime.now()

probablePrime = []
# Тест Ферма по основанию 2 для чисел. Все что прошли тест - попадают в список.
for number in range(2,1000000):
    if isPrimeFerma(2, number):
        probablePrime.append(number)
        print('Число прошло проверку ' + str(number))


# Убираем из списка простые числа
sost = []
for number in probablePrime:
    if not isPrime(number):
        sost.append(number)
        print('Число составное ' + str(number))

# Работа со словарём и проверка найденых составных по всем основаниям
d = dict.fromkeys(sost)

for number in sost:
    buf = []
    print('Проверка числа ' + str(number))
    for a in range(2, 101):
        #print(a)
        buf.append(isPrimeFerma(a, number))
    d[number] = buf

df = pd.DataFrame(d)
df.to_excel('./data.xlsx')

# Вывожу конечное время
print(datetime.now() - start_time)