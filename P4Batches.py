import numpy as np

inputs = [[1,2,3,2.5], [2.0, 5.0, -1.0, 2.0], [-1.5, 2.7, 3.3, -0.8]]
weights = [[0.2,0.8,-0.5,1.0], [0.5,-0.91,0.26,-0.5], 
[-0.26,-0.27,0.17,0.87]]
biases = [2,3,0.5]

# print(weights,"\n\n")
print("\n\n Weights\n",np.array(weights),"\n")
print("\ninputs\n",np.array(inputs),"\n")
print("\nTranspose weights\n",np.array(weights).T,"\n")

print("\n ***####### Neuron Working Over Time ***########## \n")

output = np.dot(inputs, np.array(weights).T) + biases
print("\nOutput1\n",output,"\n")

WrongOutput = np.dot(weights, np.array(inputs).T) + biases
print("\nWrongOutput\n",WrongOutput,"\n \n********NEVER TRANSPOSE INPUT*******\n")