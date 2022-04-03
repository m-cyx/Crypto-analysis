from sklearn.metrics import accuracy_score
import numpy as np
from tensorflow import keras
model = keras.models.load_model('my_model')

# Загружаю датасет
dataset = np.genfromtxt('./datasets/dataset5050.txt', delimiter=",")

# Опции для вывода NP, влияют только на консоль.
np.set_printoptions(precision=2)
np.set_printoptions(formatter={'float': '{: 0.1f}'.format})


print('\n Датасет: (Строки , Колонки) ' + str(dataset.shape) + '\n')


# Все строки до 3030 без последнего символа        обучение
X = dataset[:3030, :-1]
Y = dataset[:3030, -1]   # Все строки до 3030, только последний символ
# Все строки после 3030 без последнего символа     тест
Z = dataset[3030:, :-1]
M = dataset[3030:, -1]   # Все строки после 3030, только последний символ

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
print("Точность: %.2f%%" % (accuracy * 100.0))  # точность

accuracyZ = accuracy_score(M, prediction2.round())
print("Точность на тестовых данных: %.2f%%" % (accuracyZ * 100.0))  # точность
