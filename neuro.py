# У меня есть все вектора заданного диапазона + в конце строки ответ простое или нет
# Разбить данные на обучающие и тестовые
# Посмотреть как работает прога на видосе
# Получить результат для вектора длины 16
# Посмотреть как сохранять модель
# Увеличить размер вектора через вектор_дата -> препер_датасет
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from tensorflow.keras.utils import plot_model
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential

import numpy as np
import pandas as pd

data = pd.read_csv('./datasets/pima-diabetes.txt', delimiter=',')
print(data.head())
# Use np.loadtxt() instead when there are non-numeric values as well
dataset = np.genfromtxt('./datasets/pima-diabetes.txt',
                        delimiter=",", skip_header=True)
np.set_printoptions(precision=2)  # does not work for too wide array # Тут опции для вывода.
np.set_printoptions(formatter={'float': '{: 0.1f}'.format})

print('')
print(dataset.shape) # Возвращает (кол-во строк, кол-во колонок)
print('')
print(dataset[0:5])
X = dataset[:, :-1] # где-то тут срезает
Y = dataset[:, -1]
mean = X.mean(axis=0)
X -= mean
std = X.std(axis=0)
X /= std

print('шейпы')
print(X.shape, Y.shape)
# Design a neural network

model = Sequential()
model.add(Dense(8, input_dim=len(X[0, :]), activation='relu')) # тут указать длину вектора
model.add(Dense(4, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
# Draw the network architecture
# What is the total parameters? How?

model.summary()
# Рисую модель
plot_model(model, show_layer_names=True, show_shapes=True)
model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
model.fit(X, Y, epochs=1024, verbose=1) # тут кол-во эпох

print('True Validation Data:')
print(Y[:10])
prediction = model.predict(X)
print('Prediction:')
print(prediction[0:10].T)

# Evaluating binary predictions
accuracy = accuracy_score(Y, prediction.round())
precision = precision_score(Y, prediction.round())
recall = recall_score(Y, prediction.round())
f1score = f1_score(Y, prediction.round())
print("Accuracy: %.2f%%" % (accuracy * 100.0))
print("Precision: %.2f%%" % (precision * 100.0))
print("Recall: %.2f%%" % (recall * 100.0))
print("F1-score: %.2f" % (f1score))
