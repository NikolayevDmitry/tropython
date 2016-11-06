from Qpmin import Qpmin
import math

class Matrix:
	'Matrix class.'
	
	def __init__(self, rows = 0, cols = 0, semifield=Qpmin, matrix = None):
		'Initialization.'
		self.rows = rows
		self.cols = cols
		self.semifield = Qpmin
		self.position = 0

		self.matrix = []

		if matrix is not None:
			self.matrix = matrix
		else:
			for i in range(self.rows):
				row = []
				for j in range(self.cols):
					row.append(Qpmin.zero)
				self.matrix.append(row)

	def __str__(self):
		'To string.'
		string = ''

		for i in range(self.rows):
			for j in range(self.cols):
				string += str(self.matrix[i][j]).ljust(8) + ' '
			if i < self.rows - 1: string += '\n'

		return string

	def __repr__(self):
		'Representation.'
		return str(self.matrix)

	def __getitem__(self, x):
		'[] operator.'
		return self.matrix[x]

	def __add__(self, other):
		'+ operator.'
		rows = min(self.rows, other.rows)
		cols = min(self.cols, other.cols)

		result = []

		for i in range(rows):
			row = []
			for j in range(cols):
				row.append(self.matrix[i][j] + other.matrix[i][j])
			result.append(row)

		return  Matrix(rows, cols, result)

	def __mul__(self, other):
		'* operator.'
		#scalar
		if isinstance(other, int):
			result = self
			for i in range(self.rows):
				for j in range(self.cols):
					self[i][j] *= other
			return result
		#matrix
		if self.cols != other.rows:
			print('Matrix multiplication error.')
			return Matrix()

		result = []

		for i in range(self.rows):
			row = []
			for j in range(other.cols):
				element = 0
				for r in range(self.cols):
					element += self.matrix[i][r] * other.matrix[r][j]

				row.append(element)
			result.append(row)

		return Matrix(self.rows, other.cols, result)

	def __lshift__(self, other):
		'<< operator.'
		self[(self.position % (self.rows * self.cols)) // self.rows][(self.position % (self.rows * self.cols)) % self.rows] = other
		self.position += 1

	def __eq__(self, other):
		'== operator'
		if (self.rows != other.rows) or (self.cols != other.cols):
			return False

		for i in range(self.rows):
			for j in range(self.cols):
				if self.matrix[i][j] != other.matrix[i][j]:return False

		return True

	def fromFile(self, name):
		'Load from file.'#бесконечность не реализована
		matrix = [line.rstrip('\n') for line in open(name)]

		matrix = [[int(s) for s in line.split()] for line in matrix]
		
		self.matrix = matrix
		self.rows = len(self.matrix)
		self.cols = len(self.matrix[0])

	def toFile(self, name):
		open(name, 'w').write(self.__str__())

def zero(matrix):
	'Fill matrix with Qpmin.zero objects.'
	for i in range(matrix.rows):
			for j in range(matrix.cols):
				matrix[i][j] = Zmin.zero

def unit(matrix):
	'Fill matrix with Qpmin.unit objects.'
	for i in range(matrix.rows):
			for j in range(matrix.cols):
				matrix[i][j] = Qpmin.unit

def eye(matrix):
	'Unit matrix.'
	for i in range(matrix.rows):
			for j in range(matrix.cols):
				if i == j: matrix[i][j] = Qpmin.unit
				else: matrix[i][j] = Qpmin.zero
