# У меня есть список чисел. нужно взять каждую строчку.
# Проверить число на простоту
# Перевести число в вектор
# Создать строку в которой вектор через запятую и + 1 или 0
# Запасать строку в файл




import random
f1 = open('./datasets/prime_numbers.txt', 'r')
f2 = open('./datasets/non_prime_numbers.txt', 'r')
f = open('./datasets/dataset5050.txt', 'w')
primeLines = f1.readlines()
nonPrimwLines = f2.readlines()

primeNumberList = [] # это список чисел 1 0 1 1 0
nonPrimeNumberList = []

for line in primeLines:
    line = line.strip()
    primeNumberList.append(int(line))

for line in nonPrimwLines:
    line = line.strip()
    nonPrimeNumberList.append(int(line))
    
for number in primeNumberList:
    vector = str(bin(number))[2:]
    vector2 = ''
    for el in vector:
        vector2 = vector2 + el + ', '
    f.write(vector2 + '1' + '\n')

for number in nonPrimeNumberList:
    vector = str(bin(number))[2:]
    vector2 = ''
    for el in vector:
        vector2 = vector2 + el + ', '
    f.write(vector2 + '0' + '\n')

f.close()
f1.close()
f2.close()

# 4585 - последнее простое в файле 5050

# перемешать все строки в файле

f = open('./datasets/dataset5050.txt', 'r')
lines = f.readlines()
buf = lines[:9170]

random.shuffle(buf)

f.close()
f = open('./datasets/dataset5050.txt', 'w')
for el in buf:
    f.write(el)

f.close()

