#Simple Neural Network Model

import numpy as np

class NeuralNetwork():
    def __init__(self):
        np.random.seed(1) 
        self.synaptic_weight = 2 * np.random.random((3,1))-1

    def sigmoid(self,x):
        return 1/(1+np.exp(-x))

    def sigmoidDerivative(self,x):
        return x*(1-x)

    def training_Model(self, training_input, training_output, training_iteration):
        for iteration in range(training_iteration):
            output = self.think(training_input)
            error = training_output - output
            adjust = np.dot(training_input.T, error*self.sigmoidDerivative(output))

            self.synaptic_weight += adjust

    def think(self, input):
        input = input.astype(float)
        output = self.sigmoid(np.dot(input, self.synaptic_weight))
        return output

if __name__ == "_main_":
    neuralNetwork = NeuralNetwork()
    print("Start Randon Weight : ")
    print(neuralNetwork.synaptic_weight)

    triningInput = np.array([[0,0,1] ,[1,1,1] ,[1,0,1] ,0,1,1])
    triningOutput = np.array([[0,1,1,0]]).T

    neuralNetwork.training_Model(triningInput ,triningOutput, 15000)

    print("Ending weight : ")
    print(neuralNetwork.synaptic_weight)

    UserInput_1 = str(input("User Input 1 : "))
    UserInput_2 = str(input("User Input 2 : "))
    UserInput_3 = str(input("User Input 3 : "))

    print("Analyze new situation : ",UserInput_1 ,UserInput_2 ,UserInput_3)
    print("New output data : ")
    print(neuralNetwork.think(np.array([UserInput_1,UserInput_2,UserInput_3])))
    



