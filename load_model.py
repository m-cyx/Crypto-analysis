from sklearn.metrics import accuracy_score
import numpy as np
from tensorflow import keras
# Загружаю модель
model = keras.models.load_model('my_model')

# Опции для вывода NP, влияют только на консоль.
np.set_printoptions(precision=2)
np.set_printoptions(formatter={'float': '{: 0.1f}'.format})



# Данные для проверки и точный ответ
A = [[1,0,1,0,0,0,0,1,0,1,1,1,0,1,0,1,0,1,1,1,0,1,0,0,1,1,1,1,0,0,1,1]]
B = [[1]]

# Предсказываем
prediction = model.predict(A)
print('Как предсказывает Для A:' + prediction)
