import tensorflow as tf
import matplotlib.pyplot as plt
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' 

x_set = [i for i in range(40)]
y_set = [5*i-20 for i in x_set]

x = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)

a = tf.Variable(1, dtype=tf.float32)
b = tf.Variable(1, dtype=tf.float32)

linear_model = tf.add(tf.multiply(a, x), b)  # a * x + b
loss = tf.reduce_sum(tf.square(linear_model - y))
optimizer = tf.train.GradientDescentOptimizer(0.00001)
train = optimizer.minimize(loss)

sess = tf.Session()
init = tf.global_variables_initializer()
sess.run(init)

for i in range(10000):
    sess.run(train, {x: x_set, y: y_set})

print("y = %+.2f * x %+.2f" % (sess.run(a), sess.run(b)))


plt.plot(x_set, y_set, 'go')
plt.plot(x_set, sess.run(linear_model, {x: x_set}))
plt.grid()
plt.show()