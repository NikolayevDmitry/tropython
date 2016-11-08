from Neuron import Neuron
from random import random

class NeuralNetwork:
	'Neural Network class.'
	def __init__(self, structure, type):
		'Initialization.'
		self.type = type
		self.layers = []
		self.input = structure[0]#input vector size
		#layers
		#for x in range(1, len(structure)):
		for x, y in zip(structure[1:], structure):
			self.layers.append(self.constructLayer(x, y))

	def constructLayer(self, num, prev):
		'Construct layer.'
		#constructing array of neurons
		layer = []
		for x in range(num):
			#array of neuron weights
			weights = []
			for x in range(prev):
				weights.append(random())

			layer.append(Neuron(self.type, weights))

		return layer

	def __call__(self, input):
		'Calculate.'
		if len(input) != self.input:
			print('Wrong input vector size.')
		#errors for wrong input type

		for layer in self.layers[1:]:
			result = []
			for neuron in layer:
				result.append(neuron.sigma(neuron.net(input)))
			input = result
		print(result)

	def __str__(self):
		#kwargs
		''
		counter = 1		

		for layer in self.layers:
			print('Layer ' + str(counter))
			ncounter = 1
			for neuron in layer:
				print('\tNeuron ' + str(ncounter), end=': ')
				print(neuron.weights)
				ncounter += 1
			counter += 1
		return str(self.type)