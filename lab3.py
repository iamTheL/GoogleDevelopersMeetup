# Tensor Flow

# Tensor -> data
# Operations -> addition/subtraction/ all math funcs
# Graph -> combination of tensor + operations
# Nodes -> operations
import tensorflow as tf

a = tf.constant(3.0, name="input1")
b = tf.constant(2.0, name="input2")
print(tf.add(a, b, name="sum"))

print(tf.multiply(a, b))

sess = tf.Session()
ans1 = sess.run(tf.add(a, b, name="sum"))
ans2 = sess.run(tf.multiply(a, b, name="sum"))

print(ans1)
print(ans2)
