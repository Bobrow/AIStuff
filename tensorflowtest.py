import tensorflow as tf
h = tf.constant('Hello, this is TensorFlow!')
s = tf.Session()
print(s.run(h))
