import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' 

a = tf.placeholder(dtype=tf.float32)
b = tf.placeholder(dtype=tf.float32)
c = tf.placeholder(dtype=tf.float32)

d = tf.add(tf.multiply(a, b), c)  # a * b + c

init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

print("d =",sess.run(d, feed_dict={a:1, b:2, c:3}))

e = tf.divide(d, b)

print(sess.run(e, feed_dict={a:[2, 6], b:[4,6], c:[4,10]}))