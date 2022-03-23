import math
 
#%% inputs
x1 = 0.5
x2 = 1
b_layer_1 =[1,1,1]
b_layer_2 =[1,1]

def f1(v):
    e = math.e
    return (e**v - e**(-v))/(e**v + e**(-v))

def f2(v):
    e = math.e
    return 1/(1 - e**(-v))

#%% functions
def Perceptron(inputs, function_id, bias):
    v = sum(inputs)
    if function_id == 1:
        return f1(v) * bias
    elif function_id == 2:
        return f2(v) * bias
    return print("percepton function_id not recognised")

def Layer(perceptronBiases, function_id, startInputs, maxPerceptronInputs):
   inputCount = 0
   perceptonCount = 0 
   for i in range(0, len(startInputs)):
       anInput = startInputs[i]
       while inputCount < maxPerceptronInputs:
           if inputCount == 0:
               inputs = [anInput]
           else:    
               inputs = inputs + [anInput]
           inputCount = inputCount + 1   
       if perceptonCount == len(perceptronBiases):
           print("invlaid number of inputs per perceptrons")
       inputs = inputs + [anInput]
       bias = perceptronBiases[perceptonCount] 
       perceptronOutput = Perceptron(inputs, function_id, bias)
       inputs = [anInput]
       inputCount = 1
       if perceptonCount == 0:
           outputs = [perceptronOutput]
       else:    
           outputs = outputs + [perceptronOutput]
       perceptonCount = perceptonCount + 1
   return outputs

#%% complete multilayer perpceptron task
start_inputs_Layer_1 = [x1, x2]
outputs_layer_1 = Layer(b_layer_1, 1, start_inputs_Layer_1, 2)
outputs_layer_2 = Layer(b_layer_2, 2, outputs_layer_1, 2)
print("y1 = ", outputs_layer_2[0])
print("y2 = ", outputs_layer_2[1])