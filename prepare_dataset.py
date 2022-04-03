# У меня есть список чисел. нужно взять каждую строчку.
# Проверить число на простоту
# Перевести число в вектор
# Создать строку в которой вектор через запятую и + 1 или 0
# Запасать строку в файл

def isPrime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n

f = open('./datasets/numbers.txt', 'r')
f2 = open('./datasets/dataset.txt', 'w')
a = f.readlines()
numberList = [] # это список чисел готовых
for line in a:
    line = line.strip()
    numberList.append(int(line))
    
for number in numberList:
    vector = str(bin(number))[2:]
    vector2 = ''
    for el in vector:
        vector2 = vector2 + el + ', '
    f2.write(vector2 + str(int(isPrime(number))) + '\n')

f.close()
f2.close()