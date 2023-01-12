# Code
inputs = [1,2,3,2.5]
# weights = [0.2,0.8,-0.5,1.0]
# bias = 2

# # One Neuron with 4 inputs
# output = inputs[0]*weights[0] + inputs[1]*weights[1] + inputs[2]*weights[2] + inputs[3]*weights[3] + bias
# print(output)



# 3 output Neuron with 4 inputs Ie 3 different neurons with 4 inputs each
# inputs we need 4 so it wil be same but we need  3 weights sets with 3 biases
weights1 = [0.2,0.8,-0.5,1.0]
bias1 = 2
weights2 = [0.5,-0.91,0.26,-0.5]
bias2 = 3
weights3 = [-0.26,-0.27,0.17,0.87]
bias3 = 0.5

output = [  inputs[0]*weights1[0] + inputs[1]*weights1[1] + inputs[2]*weights1[2] + inputs[3]*weights1[3] + bias1,
            inputs[0]*weights2[0] + inputs[1]*weights2[1] + inputs[2]*weights2[2] + inputs[3]*weights2[3] + bias2,
            inputs[0]*weights3[0] + inputs[1]*weights3[1] + inputs[2]*weights3[2] + inputs[3]*weights3[3] + bias3
            ]

print(output)


# cleaner way to do P2 Coding a Layer
inputs = [1,2,3,2.5]
weights = [[0.2,0.8,-0.5,1.0], [0.5,-0.91,0.26,-0.5], [-0.26,-0.27,0.17,0.87]]
biases = [2,3,0.5]

#to Understand about ZIP
# print(list(zip(weights, biases))) 

#code for output Cleaner way to do single Layer
layer_outputs = [] # Output of current Layer
for neuron_weights, neuron_bias in zip(weights, biases):
    neuron_output = 0 #Output of given neuron
    for n_input, w_weight in zip(inputs, neuron_weights):
        neuron_output += n_input * w_weight
    neuron_output += neuron_bias
    layer_outputs.append(neuron_output)



print(layer_outputs)