from keras.preprocessing import image
import numpy as np
from keras.models import load_model
import os
from keras.applications.resnet50 import preprocess_input
from shutil import copyfile
from keras.preprocessing.image import ImageDataGenerator
from image_matrix import image2matrix

model = load_model('classify.model')
model.summary()

_, X_test, _, y_test = image2matrix("./test/MC/data_beta_0.15")
y = model.predict(X_test)
print(y_test)
print(y)
k = 0
i = 0
for t in range(y_test.shape[0]):
    k = k + 1
    if( abs(y[t,0]-y_test[t,0]) < 0.5 and abs(y[t,1]-y_test[t,1]) < 0.5):
        i = i + 1

print("k = " + str(k))
print("i = " + str(i))
np.savetxt('y.txt', y, fmt="%f") #保存为整数
np.savetxt('y_test.txt', y_test, fmt="%d") #保存为整数
