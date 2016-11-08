from types import MethodType
from math import exp
from Matrix import Matrix

def default_net(self, input):
	'Dot product.'
	result = 0
	for x in range(len(input)):
		result += self.weights[x] * input[x]
	return result

def default_sigma(self, input):
	'Logistic function.'
	return 1.0 / (1 + exp(-input))

class Neuron:
	'Single neuron class.'

	def __init__(self, type, weights, net=0, sigma=0):
		'Initialization.'
		self.weights = weights
		self.type = type

		if callable(net) == 1:
			self.net = MethodType(net, self)
		else:
			self.net = MethodType(default_net, self)

		if callable(sigma) == 1:
			self.sigma = MethodType(sigma, self)
		else:
			self.sigma = MethodType(default_sigma, self)

	def __str__(self):
		'To string.'
		return str(self.type) + '\t' + str(self.weights)
	def __repr__(self):
		'Representation.'
		return 'Neuron'
	#set_net and set_sigma methods