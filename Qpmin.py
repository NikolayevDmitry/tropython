"""
Tropical (min,+) p-adic semiring

AUTHORS:

- Dmitry Kashirin (2016-10-15) - Initial version
- Dmitry Nikolayev (2016-10-15) - Improved version
"""

import math

def int2list(x, p):
	"""Converts nonnegative integer or infinity to a list 
	in a given numeric base"""
	digits = []
	if x == 0: return [0]
	elif x == math.inf:
		return [math.inf]
	while x:
		digits.append(x % p)
		x = x//p
		digits.reverse()
	return digits

def list2int(x, p):
	"""
		Дописать
	"""
	pass


class Qpmin:
	def __init__(self, value = 0, p = 10):
		"""
        Initialization.

        INPUT:

            - value -- Base ring.
            - p -- base of the p-adic semifield (natural number).

        EXAMPLES::

            sage: R = Zp(17,3) #creates new object with value=17 over Q_3.
        """
		self.value = value
		self.p = p
		self.coefs = int2list(value, p)
	
	def __repr__(self):
		'Representation.'
		out = ''
		n = len(self.coefs)
		for i in range(n):
			out += str(self.coefs[i]) + '*' + str(self.p) + '^' + str(i)
			if i != n-1:
				out += ' + '
		return out

	def __add__(self, other):
		'+ operator.'
		return Qpmin(max(self.value, other.value), self.p)

	def __mul__(self, other):
		'* operator.'
		return Qpmin(self.value + other.value, self.p)

	def __truediv__(self, other):
		'/ operator.'
		return Qpmin(self.value - other.value, self.p)

	def __eq__(self, other):
		'== operator.'
		if isinstance(other, Qpmin):
			return self.value == other.value
		else:
			return self.value == other


Qpmin.zero = Qpmin(math.inf)
Qpmin.unit = Qpmin(0)

