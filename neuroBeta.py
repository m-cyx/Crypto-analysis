# У меня есть все вектора заданного диапазона + в конце строки ответ простое или нет
# Разбить данные на обучающие и тестовые
# Посмотреть как работает прога на видосе
# Получить результат для вектора длины 16
# Посмотреть как сохранять модель
# Увеличить размер вектора через вектор_дата -> препер_датасет
# ПОсмотреть TensorBoard для визуализации графа

from tensorflow.python.keras.callbacks import TensorBoard
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from tensorflow.keras.utils import plot_model
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential
import matplotlib.pyplot as plt


# Загружаю датасет
dataset = np.genfromtxt('./datasets/dataset5050.txt', delimiter=",")

# Опции для вывода NP, влияют только на консоль.
np.set_printoptions(precision=2) 
np.set_printoptions(formatter={'float': '{: 0.1f}'.format})


print('\n Датасет: (Строки , Колонки) ' + str(dataset.shape) + '\n')


X = dataset[:9170, :-1]  # Все строки до 4585 без последнего символа        обучение
Y = dataset[:9170, -1]   # Все строки до 4585, только последний символ
Z = dataset[4585:, :-1]  # Все строки после 4585 без последнего символа     тест
M = dataset[4585:, -1]   # Все строки после 4585, только последний символ

print('\nРазмеры массивов (Строки , Колонки):')
print(X.shape, Y.shape, Z.shape, M.shape)
print('Размер входного слоя: ' + str(len(X[0, :])))
# Собираю нейронную сеть
model = Sequential()
model.add(Dense(32, input_dim=len(X[0, :]), activation='relu')) # Длина вектора входа определяется автоматически
model.add(Dense(16, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# Выводит параметры модели
# model.summary() 

# Рисую модель
plot_model(model, show_layer_names=True, show_shapes=True, show_layer_activations=True)

# Компилирую модель
model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])  # Конфиг модели
# Обучение модели verbose: 0 = silent, 1 = progress bar
history = model.fit(X, Y, epochs=2048, verbose=1)


# Сохраняю модель
model.save('my_model')

print('Изначальные значения Y:')
print(Y[:10])
prediction = model.predict(X)
print('Как предсказывает для Y:')
print(prediction[0:10].T)

print('Изначальные значения M:')
print(M[:10])
prediction2 = model.predict(Z)
print('Как предсказывает Для M:')
print(prediction2[0:10].T)

# Вывожу точность в процентах
accuracy = accuracy_score(Y, prediction.round())
print("Точность: %.2f%%" % (accuracy * 100.0)) # точность

accuracyZ = accuracy_score(M, prediction2.round())
print("Точность на тестовых данных: %.2f%%" % (accuracyZ * 100.0))  # точность
print(history.history.keys())
plt.plot(history.history['accuracy'], label='Аккуратность на обучающем наборе')
plt.xlabel('Эпоха обучения')
plt.ylabel('Аккуратность')
plt.legend()
plt.show()

plt.plot(history.history['loss'], label='Ошибка на обучающем наборе')
plt.xlabel('Эпоха обучения')
plt.ylabel('Ошибка')
plt.legend()
plt.show()
a = input('продолжить: ')

# Сейчас скорее всего предсказывает 90%, что число не простое. Плохо. Надо пробовать учить на дата сете 50\50
# На датасете 50\50 работает норм
# Почистить проект
# Посмотреть как разделить данные на обучающие и тестовые. Кстати разделение данных вроде есть на видосе

# Вывод: при задаче бинарной классификации данные для обучения лучше брать 50\50 + перемешанные
# При использовании стандартного распределения простых чисел - показана высокая аккуратность распознавания
# Но есть предположение, что это вероятность предсказания того, что число - не простое. 


# Из одного бы датасета срезать первую  на обучение, а оставшиеся на проверку точности
