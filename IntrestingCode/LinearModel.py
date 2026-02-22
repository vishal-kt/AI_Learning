import tensorflow as tf

# Data
x = tf.constant([[1.0], [2.0], [3.0], [4.0]])
y = tf.constant([[2.0], [4.0], [6.0], [8.0]])

# Model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(units=1, input_shape=[1])
])

# Compile
model.compile(optimizer='sgd', loss='mean_squared_error')

# Train
model.fit(x, y, epochs=100)

# Predict
print("Prediction for 5:", model.predict([[5.0]]))