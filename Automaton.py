# This class models an elementary cellular automaton
# -- Val

import random
import sys

class Automaton:
	startingCondition = []
	rule = []
	cells = []
	age = 0
	size = 0

	def __init__(self, startingCondition, rule, size):
		"""
		Initializes an elementary cellular automaton; user must provide a starting condition (either a letter or a number), 
		a rule (integer with a value from 0-255), and a size (integer representing the length of each generation for those 
		cases in which the user specified l, r, c, or x as the starting condition.
		l, r, and c create starting conditions in which the entire string is filled with zeros save the leftmost, rightmost, 
		or central bit. x creates starting conditions in which a random number of the appropriate number of bits is the 
		starting condition.
		"""
		# Convert the rule into a binary string, then pad it with leading 0s as necessary.
		ruleM = '{0:0b}'.format(rule)
		ruleM = ('0' * (8 - len(ruleM))) + ruleM
		self.rule = [int(i) for i in list(ruleM)]
		self.size = size
		# Array of 0s with the leftmost bit as a 1
		if startingCondition == 'l':
			self.startingCondition = [0] * size
			self.startingCondition[0] = 1
		# Array of 0s with the rightmost bit as a 1
		elif startingCondition == 'r':
			self.startingCondition = [0] * size
			self.startingCondition[-1] = 1
		# Array of 1s with the central bit as a 1
		elif startingCondition == 'c':
			self.startingCondition = [0] * size
			self.startingCondition[int(round(size / 2, 0))] = 1
		elif startingCondition == 'x':
			random.seed()
			val = random.getrandbits(size)
			valB = '{0:0b}'.format(val)
			valB = ('0' * (size - len(valB))) + valB
			self.startingCondition = [int(i) for i in list(valB)]
		else:
			startM = '{0:0b}'.format(int(startingCondition))
			self.startingCondition = [int(i) for i in list(startM)]
		self.cells.append(self.startingCondition[:])
			
	def evolve(self):
		"""
		This function takes the array representing the latest generation, and then creates an array representing a new generation 
		by applying the automaton's rule to the latest generation. This new array is then appended to the total list of generations.
		"""
		newCells = []
		for bit in range(len(self.cells[self.age])):
			# This condition handles the rightmost cell in the array
			if bit == len(self.cells[self.age]) - 1:
				if (self.cells[self.age][bit] == 1 and self.cells[self.age][bit - 1] == 1 and self.cells[self.age][0] == 1):		#111
					newCells.append(self.rule[0])
				elif (self.cells[self.age][bit] == 1 and self.cells[self.age][bit - 1] == 1 and self.cells[self.age][0] == 0):		#110
					newCells.append(self.rule[1])
				elif (self.cells[self.age][bit] == 0 and self.cells[self.age][bit - 1] == 1 and self.cells[self.age][0] == 1):		#101
					newCells.append(self.rule[2])
				elif (self.cells[self.age][bit] == 0 and self.cells[self.age][bit - 1] == 1 and self.cells[self.age][0] == 0):		#100
					newCells.append(self.rule[3])
				elif (self.cells[self.age][bit] == 1 and self.cells[self.age][bit - 1] == 0 and self.cells[self.age][0] == 1):		#011
					newCells.append(self.rule[4])
				elif (self.cells[self.age][bit] == 1 and self.cells[self.age][bit - 1] == 0 and self.cells[self.age][0] == 0):		#010
					newCells.append(self.rule[5])
				elif (self.cells[self.age][bit] == 0 and self.cells[self.age][bit - 1] == 0 and self.cells[self.age][0] == 1):		#001
					newCells.append(self.rule[6])
				else:		#000
					newCells.append(self.rule[7])
			# This condition handles all other cells in the array
			else:
				if (self.cells[self.age][bit] == 1 and self.cells[self.age][bit - 1] == 1 and self.cells[self.age][bit + 1] == 1):		#111
					newCells.append(self.rule[0])
				elif (self.cells[self.age][bit] == 1 and self.cells[self.age][bit - 1] == 1 and self.cells[self.age][bit + 1] == 0):		#110
					newCells.append(self.rule[1])
				elif (self.cells[self.age][bit] == 0 and self.cells[self.age][bit - 1] == 1 and self.cells[self.age][bit + 1] == 1):		#101
					newCells.append(self.rule[2])
				elif (self.cells[self.age][bit] == 0 and self.cells[self.age][bit - 1] == 1 and self.cells[self.age][bit + 1] == 0):		#100
					newCells.append(self.rule[3])
				elif (self.cells[self.age][bit] == 1 and self.cells[self.age][bit - 1] == 0 and self.cells[self.age][bit + 1] == 1):		#011
					newCells.append(self.rule[4])
				elif (self.cells[self.age][bit] == 1 and self.cells[self.age][bit - 1] == 0 and self.cells[self.age][bit + 1] == 0):		#010
					newCells.append(self.rule[5])
				elif (self.cells[self.age][bit] == 0 and self.cells[self.age][bit - 1] == 0 and self.cells[self.age][bit + 1] == 1):		#001
					newCells.append(self.rule[6])
				else:		#000
					newCells.append(self.rule[7])
		self.cells.append(newCells)
		self.age += 1
		
	def extractColumn(self, index):
		"""
		This function takes a user-specified index and then extracts the bit at said index from every generation. The bits are converted 
		into an array of integers that is then returned.
		"""
		bitArray = []
		numbers = []
		for i in range(len(self.cells)):
			bitArray.append(self.cells[i][index])
			number = 0
			for bit in bitArray:
				number = (number << 1) | bit
			numbers.append(number)
		return numbers
		
	def extractColumnBits(self, index):
		"""
		This function takes a user-specified index and then extracts the bit at said index from every generation. The bits are placed in 
		an array and the raw bit array is returned.
		"""
		bitArray = []
		for i in range(len(self.cells)):
			bitArray.append(self.cells[i][index])
		return bitArray
		
	def extractRow(self, row):
		"""
		This function takes the row representing the user-specified generation and then returns the row as a series of integers placed 
		in an array.
		"""
		number = []
		for i in range(len(self.cells[row])):
			number = 0
			for bit in row:
				number = (number << 1) | bit
			numbers.append(number)
		return numbers
		
	def extractRowBits(self, row):
		"""
		This function takes the row representing the user-specified generation and then returns the raw bit array that represents said
		generation.
		"""
		return self.cells[row]
		
	def draw(self):
		"""
		This function prints each generation to the console.
		"""
		for generation in self.cells:
			printLine = ''
			for bit in generation:
				if bit == 0:
					printLine = printLine + ' '
				else:
					printLine = printLine + '*'
			print(printLine)
			
if __name__ == '__main__':
	"""
	This block here is for demo purposes. It prompts the user to enter a series of values that are used to either print n generations 
	of the user-designed automaton to the console, or returns an array of integers derived from the central column of the array of 
	generations. This is not intended to be a full and complete end-user program; it only serves to demonstrate the capabilities of the 
	actual class, which is to be incorporated in other programs and scripts as need be.
	"""
	size = 0
	generations = 0
	drawOrGen = ''
	while (drawOrGen != 'd' and drawOrGen != 'g'):
		drawOrGen = input("Enter 'd' if you want to draw a cellular automaton, or 'g' if you want to generate a random number: ")
	startingCondition = input("Enter a starting condition (l, r, c, x, or a number): ")
	rule = int(input("Enter a rule (must be a number between 0 and 255): "))
	if (startingCondition == 'l' or startingCondition == 'r' or startingCondition == 'c' or startingCondition == 'x'):
		size = int(input("Please enter the size of the starting condition you would like in bits: "))
	else:
		size = len(bin(int(startingCondition))) - 2
	generations = int(input("Enter the number of generations you would like the automaton to live through: "))
	robot = Automaton(startingCondition, rule, size)
	for i in range(generations):
		robot.evolve()
	if drawOrGen == 'd':
		robot.draw()
	else:
		midpoint = round(size / 2)
		number = robot.extractColumn(midpoint)
		print(number)