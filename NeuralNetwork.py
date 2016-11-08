from Neuron import Neuron
from random import random

class NeuralNetwork:
	'Neural Network class.'
	def __init__(self, structure):
		'Initialization.'
		self.layers = []
		#input
		self.input = structure[0]
		#layers
		for x in range(1, len(structure)):
			self.layers.append(self.constructLayer(structure[x], structure[x-1]))

	def constructLayer(self, num, prev):
		'Construct layer.'
		#constructing array of neurons
		layer = []
		for x in range(num):
			#array of neuron weights
			weights = []
			for x in range(prev):
				weights.append(random())

			layer.append(Neuron(weights))

		return layer

	def __call__(self, input):
		'Calculate.'
		if len(input) != self.input:
			print('Wrong input vector size.')

		for layer in self.layers[1:]:
			result = []
			for neuron in layer:
				result.append(neuron.sigma(neuron.net(input)))
			input = result
		print(result)#result