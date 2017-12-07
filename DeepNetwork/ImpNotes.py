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
### Now by changing W and b we can actually reduce the loss.
## Now if W = -1 and b =1 then our our linear_model becomes y i.e. output of our model becomes the actual output
## -1 x 1 + 1 = 0
## -1 x 2 + 1 = -1
## -1 x 3 + 1 = -2
## -1 x 4 + 1 = -3
## if we change W = tf.Variable([-1.0],tf.float32)
## b = tf.Variable([1.0], tf.float32) , we will get loss as 0.0
## If we want machine to learn W and b , we need optimizer
## Optimizer modifies each variable according to the magnitude of the derivative of loss w.r.t that variable. here we will use
## Gradient Descent optimizer i.e The optimizer will check the magnitude of the derivative of loss i.e the optimizer will check
## the change in the loss w.r t the change in the variable and if the loss is decreasing then it will keep on changing the variable 
## in that particular direction
