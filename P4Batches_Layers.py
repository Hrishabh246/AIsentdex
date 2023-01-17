import numpy as np

inputs = [[1,2,3,2.5], [2.0, 5.0, -1.0, 2.0], [-1.5, 2.7, 3.3, -0.8]]
weights = [[0.2,0.8,-0.5,1.0], [0.5,-0.91,0.26,-0.5], 
[-0.26,-0.27,0.17,0.87]]
biases = [2,3,0.5]

#Second Layer
# Inputs of Layer 2 are Output of Layer 1

weights2 = [[0.1, -0.14, 0.5], [-0.5, 0.12, -0.33], [-0.44, 0.73, -0.13]]
biases2 = [-1, 2, -0.5]


#Layer 1

# print(weights,"\n\n")
print("\n\n Weights for Layer 1\n",np.array(weights),"\n")
print("\ninputs for Layer 1 \n",np.array(inputs),"\n")
print("\nTranspose weights for layer 1\n",np.array(weights).T,"\n")

print("\n ***####### Neuron Working Over Time ***########## \n")

layer1_output = np.dot(inputs, np.array(weights).T) + biases#This wil become for Inputs for Layer 2 
print("\nLayer 1 Output\n",layer1_output,"\n")

#Wrong Output
WrongOutput = np.dot(weights, np.array(inputs).T) + biases
print("\nWrongOutput\n",WrongOutput,"\n \n********NEVER TRANSPOSE INPUT*******\n")

#layer2

print("\n\n Weights for Layer 2 \n",np.array(weights2),"\n")
print("\ninputs for Layer 2 ie. Output of Layer 1\n",np.array(layer1_output),"\n")
# print("\nTranspose weights\n",np.array(weights).T,"\n")

print("\n ***####### Neuron Working Over Time ***########## \n")

layer2_output = np.dot(layer1_output, np.array(weights2).T) + biases2

print("\nLayer 2 Output\n",layer2_output,"\n")
