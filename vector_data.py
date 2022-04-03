# Вектор длины 1024 - какое первое и последнее число?
    # Решил взять вектора длины 16 для начала.
# Взять взять все простые числа этого диапазона
# Представить их в виде векторов, сохранить в файл
# Считать их с файла, закинуть в list

import random
from random import randint

def isPrime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n


f = '1'
l = '1'

for i in range(1, 32):
    f = f + '0'
    l = l + '1'
print('Вектор - ' + f)
print('Длина - ' + str(len(f)))
print('Десятичное - ' + str(int(f, 2)))

print('Вектор - ' + l)
print('Длина - ' + str(len(l)))
print('Десятичное - ' + str(int(l, 2)))

f10 = int(f, 2)
l10 = int(l, 2)

print('Между ними чисел: '+ str(l10 - f10))

f = open('./datasets/non_prime_numbers.txt', 'w')
p = open('./datasets/prime_numbers.txt', 'w')

# for i in range(f10, l10):
#     if isPrime(i):
#         p.write(str(i) + '\n')
#     else:
#         f.write(str(i) + '\n')

randNumList = []
for i in range(0, 100000):
    randNumList.append(random.randint(f10, l10))

# print(randNumList)
for number in randNumList:
    if isPrime(number):
        p.write(str(number) + '\n')
    else:
        f.write(str(number) + '\n')
    
f.close()
p.close()






