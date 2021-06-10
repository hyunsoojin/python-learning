'''
Created on 2021. 6. 8.

@author: User
'''

import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

a = tf.constant(20, name="a")
b = tf.constant(30, name="b")
mul_op = a * b

sess = tf.Session()

tw = tf.summary.FileWriter("log_dir", graph=sess.graph)

print(sess.run(mul_op))

