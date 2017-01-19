import math
import random
from linear_algebra import dot

def step_function(x):
    return 1 if x >= 0 else 0

def perceptron_output(weights, bias, x):
    """
    Returns 1 if the perceptron 'fires', 0 otherwise
    """
    calculation = dot(weights, x) + bias
    return step_function(calculation)

def sigmoid(t):
    return 1 / (1 + math.exp(-t))

def neuron_output(weights, inputs):
    """
    print weights
    print "----------------------------"
    print inputs
    """
    return sigmoid(dot(weights, inputs))

def feed_forward(neural_network, input_vector):
    """
    Takes in a neural network (represented as list of list of lists of weights)
    and returns the output from forward-propogating the input
    """
    outputs = []

    # Process one layer at a time
    for layer in neural_network:
        input_with_bias = input_vector + [1]                # add a bias input
        output = [neuron_output(neuron, input_with_bias)    # compute output
                  for neuron in layer]                      # for each neuron
        outputs.append(output)                              # adn remember it

        # The input to the next layer is the output of this one
        input_vector = output

    return outputs

"""
xor_network = [ # Hidden layer
                [[20, 20, -30],     # 'and' neuron
                 [20, 20, -10]],    # 'or' neuron
                # Output layer
               [[-60, 60, -30]]]

for x in [0,1]:
    for y in [0,1]:
        # feed_forward produces outputs of every neuron
        # feed_forward[-1] is the outputs of the output-layer neurons
        print x, y, feed_forward(xor_network, [x,y])[-1]
"""

def backpropogate(network, input_vector, target):

    hidden_outputs, outputs = feed_forward(network, input_vector)
    
    # the output * (1 - output) is from the derivative of sigmoid
    output_deltas = [output * (1 - output) * (output - target[i])
                     for i, output in enumerate(outputs)]

    # Adjust weights for output layer, one neuron at a time
    for i, output_neuron in enumerate(network[-1]):
        # Focus on the ith output layer neuron
        for j, hidden_output in enumerate(hidden_outputs + [1]):
            # Adjust the jth weight based on both this
            # neuron's delta and its jth iinput
            output_neuron[j] -= output_deltas[i] * hidden_output

    # Backpropogate errors to hidden layer
    hidden_deltas = [hidden_output * (1 - hidden_output) * 
                      dot(output_deltas, [n[i] for n in network[-1]])
                     for i, hidden_output in enumerate(hidden_outputs)]

    # Adjust weights for hidden layer, one neuron at a time
    for i, hidden_neuron in enumerate(network[0]):
        for j, input in enumerate(input_vector + [1]):
            hidden_neuron[j] -= hidden_deltas[i] * input

zero_digit = [1,1,1,1,1,
              1,0,0,0,1,
              1,0,0,0,1,
              1,0,0,0,1,
              1,1,1,1,1]

raw_digits = [
          """11111
             1...1
             1...1
             1...1
             11111""",
             
          """..1..
             ..1..
             ..1..
             ..1..
             ..1..""",
             
          """11111
             ....1
             11111
             1....
             11111""",
             
          """11111
             ....1
             11111
             ....1
             11111""",     
             
          """1...1
             1...1
             11111
             ....1
             ....1""",             
             
          """11111
             1....
             11111
             ....1
             11111""",   
             
          """11111
             1....
             11111
             1...1
             11111""",             

          """11111
             ....1
             ....1
             ....1
             ....1""",
             
          """11111
             1...1
             11111
             1...1
             11111""",    
             
          """11111
             1...1
             11111
             ....1
             11111"""]     

def make_digit(raw_digit):
    return [1 if c == '1' else 0
            for row in raw_digit.split("\n")
            for c in row.strip()]

inputs = map(make_digit, raw_digits)

targets = [[1 if i == j else 0 for i in range(10)]
           for j in range(10)]

random.seed(0)
input_size = 25 
num_hidden = 5
output_size = 10

# Each hidden neuron has one weight per input, plus a bias weight
hidden_layer = [[random.random() for __ in range(input_size + 1)]
                for __ in range(num_hidden)]

# Each output neuron has one weight per hidden neuron, plus a bias weight
output_layer = [[random.random() for __ in range(num_hidden + 1)]
                for __ in range(output_size)]

# The network starts out with random weights
network = [hidden_layer, output_layer]

for __ in range(10000):
    for input_vector, target_vector in zip(inputs, targets):
        backpropogate(network, input_vector, target_vector)

def predict(input):
    return feed_forward(network, input)[-1]

predict(inputs)
