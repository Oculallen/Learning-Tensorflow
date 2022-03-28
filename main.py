import tensorflow as tf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#extra imports
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
#Doccy stuff
import tensorflow_docs as tfdocs
import tensorflow_docs.plots
import tensorflow_docs.modeling

layers = [6, 32, 16, 1]

def normalizer(x, ts):
    return (x-ts['mean'])/ts['std']

column_names = ['bedrooms', 'bathrooms', 'ensuit', 'distanceToCity', 'area', 'garden', 'price']
df = pd.read_csv("TrainingData.csv",
sep=",",
comment="\t",
names=column_names,
na_values="?",
skipinitialspace=True)

train = df.sample(frac=0.8, random_state=0)
train_x = train.drop('price', axis=1)
train_y = train['price']

test = df.drop(train.index)
test_x = test.drop('price', axis=1)
test_y = test['price']

train_stats = train_x.describe().transpose()
print(train_stats)
train_x_scaled = normalizer(train_x, train_stats)
test_x_scaled = normalizer(test_x, train_stats)

#Lets build a model booiiiiiis
model = Sequential()
model.add(Dense(6, activation=tf.nn.relu, input_shape=[train_x.shape[1]]))
model.add(Dense(16, activation=tf.nn.relu))
model.add(Dense(32, activation=tf.nn.relu))
model.add(Dense(layers[-1]))
print("Model Built!")

#Config
model.compile(optimizer='adam',
loss='mse',
metrics=['mse','mae'])

#Early Stop
early_stop = tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=50)

history = model.fit(
    x=train_x_scaled,y=train_y,
    epochs=1000,
    validation_split=0.2,
    verbose=0,
    callbacks=[early_stop, tfdocs.modeling.EpochDots()]
)

#Evaluation
# plot_obj=tfdocs.plots.HistoryPlotter(smoothing_std=2)
# plot_obj.plot({'Auto MPG': history}, metric="mae")
# plt.ylim([100000, 7000000])
# plt.ylabel('MAE [Price]')

test_preds = model.predict(test_x_scaled).flatten()

evaluation_plot = plt.axes(aspect='equal')
plt.scatter(test_y, test_preds)
plt.ylabel('Price Predicted')
plt.xlabel('Actual Price')
plt.xlim([5000, 400000000])
plt.ylim([5000, 400000000])
plt.plot([5000, 400000000], [5000, 400000000])
plt.show()

new_house = pd.DataFrame([[
    4,
    6,
    2,
    5000,
    6,
    4
]], columns=column_names[0:-1])
print(new_house)

new_house_price = model.predict(new_house).flatten()
print(f'New price is: {new_house_price}')