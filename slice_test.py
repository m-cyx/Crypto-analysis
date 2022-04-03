import numpy as np

dataset = np.genfromtxt('./datasets/dataset_test.txt', delimiter=",")

print(dataset)
X = dataset[:, :-1]  # Все строки без последнего символа
Y = dataset[:, -1]   # Все строки, только последняя колонка

print(X)
print(Y)
