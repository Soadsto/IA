import tensorflow as tf
#Collect 2 numbers by input prompt
num1 = int(input("n1 = "))
num2 = int(input("n2 = "))

#Establish two tensors, one for each input number
num1 = tf.Variable(num1)
num2 = tf.Variable(num2)

#Establish graph
sum = tf.add(num1, num2)

#This show information about sum but doesnt evaluate anything yet
print("sum =" + str(sum))

#instantiate a global varible initializer 
globalVariableInitializer = tf.global_variables_initializer()

#Finally we run the graph (in a session)
with tf.Session() as session:
    globalVariableInitializer.run()
    result = sum.eval()
#Here ends the with block

#Show the result
print("Result = " + str(result))

