# This class is a partial model of ARC4, including just the portions
# necessary for pseudorandom number generation.
# -- Val

import random

class PA4:
	seedValue = []
	
	def __init__(self, input):
		"""
		This constructor takes either the letter "x" or a number as input. Passing it the letter "x" 
		will cause it to generate a random bit string of length 2048 to serve as the key; passing it 
		a number, on the other hand, will cause it to format it as a bit string.
		"""
		# Generate a random bit string if passed "x"
		if input == "x":
			random.seed()
			initialVal = random.getrandbits(2048)
			medialVal = '{0:0b}'.format(initialVal)
			if len(medialVal) < 2048:
				medialVal = ('0' * (2048 - len(medialVal))) + medialVal
			finalVal = [int(i) for i in list(medialVal)]
			self.seedValue = finalVal[:]
		# Otherwise, format the input as a bit string of the appropriate length
		else:
			thing = '{0:0b}'.format(int(input))
			if len(thing) < 2048:
				thing = ('0' * (2048 - len(thing))) + thing
				self.seedValue = [int(thing) for i in list(thing)]
			if len(thing) > 2048:
				thing = thing[:2048]
				self.seedValue = [int(thing) for i in list(thing)]
			else:
				self.seedValue = [int(thing) for i in list(thing)]

	def scheduleKey(self, initializer):
		"""
		This function is the key scheduler. It initializes an array that is used to generate the 
		pseudorandom numbers used later. It takes the seed value and then mixes it with the 
		identity permutation that makes up "key," for 256 iterations.
		"""
		key = []
		for i in range(256):
			key.append(i)
		j = 0
		for i in range(256):
			j = (j + key[i] + initializer[i % 256]) % 256 # [i % x], where x is the number of bytes taken up by the seed value (so 2048 bits == 256 bytes)
			key[i], key[j] = key[j], key[i]
		return key
	
	def generateBits(self, key):
		"""
		This function creates a generator that, when used, will iterate for as long as needed and 
		combined elements from the key array with other elements from it, in a pseudorandom fashion.
		These elements are then parsed to create the pseudorandom integers that are reutrned by the 
		generator.
		"""
		generating = True
		i = 0
		j = 0
		thisKey = key[:]
		while(generating):
			i = (i + 1) % 256
			j = (j + thisKey[i]) % 256
			output = thisKey[(thisKey[i] + thisKey[j]) % 256]
			yield output	