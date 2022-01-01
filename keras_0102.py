from keras import models
from keras import layers

model = model.Sequential()
model.add(layers.Dense(32, activation='relu', input_shapte=(784,)))
model.add(layers.Dense(10, activation='softmax'))

