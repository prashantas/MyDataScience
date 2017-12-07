####  https://www.youtube.com/watch?v=yX8KuPZCAMo           # Very Good Link from Edureka for tensorflow basics Really Good

# A placeholder is nothing but a promise to provide the value later

a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)

adder_node = a+b
sess = tf.Session()

print(sess.run(adder_node,{a:[1,3],b:[2,4]}))

###########################################################################################################
###########################################################################################################
#When we train a model, we use variable to hold an update parameter. Variables allow us to add trainable parameters to a graph
import tensorflow as tf
#Model parameters
W = tf.Variable([.3],tf.float32)
b = tf.Variable([-.3], tf.float32)

#Inputs and Outputs
x = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)  # Actual output which we already know

linear_model = W*x+b

#Loss ffunction
squared_delta = tf.square(linear_model - y)
loss = tf.reduce_sum(squared_delta)

init = tf.global_variables_initializer()

sess = tf.Session()
sess.run(init)
print(sess.run(loss,{x:[1,2,3,4],y:[0,-1,-2,-3]}))
### the output is 23.66
###########################################################################################################################################
