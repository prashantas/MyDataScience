import tensorflow as tf

a = tf.constant(5.0)
b = tf.constant(6.0)

c = a*b
sess = tf.Session()

File_Writer = tf.summary.FileWriter('C:\\Users\\prassha\\Desktop\\MachineLearning\\EquiSkill\\TF_Sonar\\graph',sess.graph)

## (C:\Users\prassha\AppData\Local\Continuum\Anaconda3) C:\Users\prassha\Desktop\MachineLearning\EquiSkill\TF_Sonar\graph>tensorboard --logdir="C:\Users\prassha\Desktop\MachineLearning\EquiSkill\TF_Sonar\graph"
## Starting TensorBoard b'54' at http://prassha-WX-1:6006
## (Press CTRL+C to quit)

print(sess.run(c))

sess.close()
