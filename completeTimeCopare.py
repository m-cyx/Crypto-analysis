from datetime import datetime
from random import randint
from sklearn.metrics import accuracy_score
import numpy as np
from tensorflow import keras

# Загружаю модель
model = keras.models.load_model('my_model')

# Опции для вывода NP, влияют только на консоль.
np.set_printoptions(precision=2)
np.set_printoptions(formatter={'float': '{: 0.1f}'.format})

def isPrime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n

def MillerRabinTest(n, k):
    # производится k раундов проверки числа n на простоту
    if (n == 2 or n == 3):
        return True
    if (n < 2 or n % 2 == 0):
        return False
    t = n - 1
    s = 0
    while (t % 2 == 0):
        t /= 2
        t = int(t)
        s += 1
    for i in range(1, k + 1):
        a = randint(2, n - 2)
        x = pow(a, t, n)
        if (x == 1 or x == n - 1):
            continue
        for i in range(1, s):
            x = pow(x, 2, n)
            if (x == 1):
                return False
            if (x == n - 1):
                break
        if (x != n - 1):
            return False
    return True


# Данные для проверки и точный ответ
A = [[1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1,
      0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1]]
B = [[1]]
number = 2708829427


# Предсказываем
startTime1 = datetime.now()
resultPrediction = model.predict(A)
endTime1 = datetime.now() - startTime1

startTime2 = datetime.now()
resultMiller = MillerRabinTest(number, 50)
endTime2 = datetime.now() - startTime2

startTime3 = datetime.now()
resultPrime = isPrime(number)
endTime3 = datetime.now() - startTime3

print('Проверка Нейросетью: ' + str(resultPrediction))
print('Проверка Миллер-Рабин: ' + str(resultMiller))
print('Проверка Стандантрая: ' + str(resultPrime))

print('Время каждого: ')
print(str(endTime1) + '  Нейро')
print(str(endTime2) + '  Миллер')
print(str(endTime3) + '  Стандарт')
