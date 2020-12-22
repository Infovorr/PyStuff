# This class models the Vernam cipher
# -- Val

import Automaton
import math
import random
import sys

class VernamAutomaton:

	def __init__(self):
		"""
		An empty constructor, for possible future use.
		"""
		pass
	
	def crypt(self, text, key):
		"""
		This function takes a string as input, along with a key in the form of a 1-D array of bits. The key and string must have
		equal numbers of bits. The function either encrypts the string by XORing it with the key, or decrypts it the same way.
		Output is the encrypted or decrypted string.
		"""
		binaryText = ''
		# This block converts the provided string from ASCII to binary
		for i in text:
			temp = bin(ord(i))
			if len(temp) < 10 :
				temp = ('0' * (10 - len(temp))) + temp[2:]
			else:
				temp = temp[2:]
			binaryText += temp
		# Format the binary string properly for further use
		binaryListF = '0b' + binaryText
		keyListF = '0b'
		# Combine the bit array into a bit string
		for i in key:
			keyListF += str(i)
		# XOR the text with the key
		encryption = bin(int(binaryListF, 2) ^ int(keyListF, 2))
		# Format the modified string in order to restore leading 0s that may have been lost
		if len(encryption) < len(binaryListF):
			encryption = '0b' + ((len(binaryListF) - len(encryption)) * '0') + encryption[2:]
		encryption = encryption[2:]
		encryptionList = []
		# Break the bit string into an array of byte-length chunks; first condition is for bit strings that aren't divisible by 8
		if (len(encryption) % 8 != 0):
			length = int(math.floor(len(encryption) / 8))
			ack = 0
			for i in range(length):
				encryptionList.append(encryption[i*8:(i*8)+8])
				ack = i*8+8
			encryptionList.append(encryption[ack:-1])
		# Second condition is for those that are
		else:
			length = int(len(encryption) / 8)
			for i in range(length):
				encryptionList.append(encryption[i*8:(i*8)+8])
		output = ''
		# Convert the individual byte-length chunks of the list into ASCII characters
		for i in encryptionList:
			output += chr(int(i, 2))
		return output
		
if __name__ == '__main__':
	"""
	This block here is for demo purposes. It prompts the user to enter a string, which it will then encrypt and subsequently 
	decrypt, displaying the string after both stages. This is not intended to be a full and complete end-user program; it 
	only serves to demonstrate the capabilities of the actual class, which is to be incorporated in other programs and scripts 
	as need be.
	"""
	crypto = VernamAutomaton()
	text = input("Please enter a string to be encrypted: ")
	test = ''
	# The following block attempts to convert the provided string into bits and then calculate the length of said bit string.
	for i in text:
		temp = bin(ord(i))
		if len(temp) < 10 :
			temp = ('0' * (10 - len(temp))) + temp[2:]
		else:
			temp = temp[2:]
		test += temp
	test = '0b' + test
	robot = Automaton.Automaton('x', 30, len(test) - 2)
	for i in range(10):
		robot.evolve()
	output = crypto.crypt(text, robot.extractRowBits(9))
	print("Encrypted:")
	print(output)
	print("Decrypted:")
	output = crypto.crypt(output, robot.extractRowBits(9))
	print(output)