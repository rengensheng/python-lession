import numpy as np

def sigmoid(x):
  return 1/(1 + np.exp(-x))

class Neuron:
  def __init__(self,widgets, bias):
    self.widgets = widgets
    self.bias = bias
  def feedforward(self, inputs):
    total = np.dot(self.widgets, inputs) + self.bias
    return sigmoid(total)
class OurNeuralNetwork:
  def __init__(self):
    widgets = np.array([0, 1])
    bias = 0.0
    self.h1 = Neuron(widgets=widgets, bias=bias)
    self.h2 = Neuron(widgets=widgets, bias=bias)
    self.o1 = Neuron(widgets=widgets, bias=bias)
  def feedforward(self, x):
    out_h1 = self.h1.feedforward(x)
    out_h2 = self.h2.feedforward(x)
    out_o1 = self.o1.feedforward(np.array([out_h1, out_h2]))
    return out_o1
network = OurNeuralNetwork()
x = np.array([2,3])
print(network.feedforward(x))