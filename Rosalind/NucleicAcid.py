import sys

#Class to solve http://rosalind.info/problems/rna/, http://rosalind.info/problems/revc/

class RosalindProblems:

	def __init__(self, s):
		self.A = 0
		self.C = 0
		self.G = 0
		self.T = 0
		self.nucleotides = s
		self.RNA = self.RNA = self.nucleotides.replace("T", "U")
		self.complement = ""
		self.complementary()
		self.compreverse = self.complement[::-1]

	def counter(self):
		self.A = self.nucleotides.count('A')
		self.C = self.nucleotides.count('C')
		self.G = self.nucleotides.count('G')
		self.T = self.nucleotides.count('T')
		
		print(self.A, self.C, self.G, self.T)

	def complementary(self):
		self.complement = [self.switch(x) for x in self.nucleotides]
		self.complement = ''.join(self.complement)
		#print(self.complement)
		


	def switch(self, n): 
		if n == "A":
			n = "T"
		elif n == "T":
			n = "A"
		elif n == "C":
			n = "G"
		elif n == "G":
			n = "C"
		return n

		










#nucleotide = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"

nucleotide = sys.argv[1]
test = RosalindProblems(nucleotide)
test.counter()
test.complementary()
print(test.compreverse)
#print(test.nucleotides)
#print(test.RNA)
#print()




