'''
Created on 2021. 6. 7.

@author: User
'''


import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

a = tf.constant(100)
b = tf.constant(50)
add_op = a+b

v = tf.Variable(0)
let_op = tf.assign(v, add_op)

sess = tf.Session()

sess.run(tf.global_variables_initializer())
sess.run(let_op)

print(sess.run(v))
