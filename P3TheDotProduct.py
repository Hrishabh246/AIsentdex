
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

