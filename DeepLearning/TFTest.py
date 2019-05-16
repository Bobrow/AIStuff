import tensorflow as tf
import numpy as np
const = tf.constant(2.0, name="const")
y=tf.Variable(2.0, name="y")
z=tf.Variable(1.0, name="z")
p=tf.add(y,z,name="p")
q=tf.add(z, const, name="q")
x=tf.multiply(p,q,name="x")
init_op=tf.global_variables_initalizer()
with tf.Session() as ses:
	ses.run(init_op)
	x_out = ses.run(x)
	print("Variable x has a value of {}".format(x_out))
y=tf.placeholder(tf.float32, [None,1], name="y")
x_out=ses.run(x, feed_dict={y: np.arrange(0,10)[:, np.newaxis]}) 
