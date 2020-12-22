import random

class rsaProg:
	def factor(self, n):
		f = {0:0}
		i = 2
		if n == 1 or n == 2:
			f[n] = 1
			del f[0]
			return f
		while i <= n:
			if n % i == 0:
				if i in f:
					f[i] = f[i] + 1
				else:
					f[i] = 1
				n = n/i
			else:
				i += 1
		del f[0]
		return f
	
	
	def phi(self, n):
		f = self.factor(n)
		values = list(f.keys())
		output = 1
		for i in values:
			output = output * ((i**(f[i] - 1)) * (i - 1))
		return output
	
	
	def rsaE(self, p, q, e, m):
		n = p * q
		d = self.inverse(e, (p-1)*(q-1))
		c = (m**e) % n
		o = (c**d) % n
		print("Encryption keys: " + str(n) + ", " + str(e))
		print("Decryption keys: " + str(n) + ", " + str(d))
		print("Ciphertext: " + str(c))
		print("Deciphered text: " + str(o))

	def extended(self, n, d):
		sOld, sNew = 1, 0
		tOld, tNew = 0, 1
		while d != 0:
			q = n // d
			r = n % d
			n = d
			d = r
			sOld, sNew = sNew, sOld - (q * sNew)
			tOld, tNew = tNew, tOld - (q * tNew)
		return n, sOld, tOld
	
	def inverse(self, n, d):
		n, s, t = self.extended(n, d)
		if s < 0:
			s = s + d
		return s % d
		
if __name__ == "__main__":
	running = 1
	
	worker = rsaProg()
	
	while running:
		alsoRunning = 1
		option = int(input("Press 1 to calculate Euler's totient, or 2 for RSA:"))
		if option == 1:
			userVal = int(input("Please enter a value for the input:"))
			output = worker.phi(userVal)
			print("The totient is " + str(output))
			alsoRunning = 0
			running = 0
		if option == 2:
			p = int(input("Please enter a value for p: "))
			q = int(input("Please enter a value for q: "))
			e = int(input("Please enter a value for e: "))
			m = random.randint(1,9999)
			worker.rsaE(p, q, e, m)
			alsoRunning = 0
			running = 0