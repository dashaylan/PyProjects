import sys

#Solution for http://rosalind.info/problems/dna/
#Utilizes the built in count function

class NucleotideCounter:

	def __init__(self, nucleotides):
		self.A = 0
		self.C = 0
		self.G = 0
		self.T = 0
		self.nucleotides = nucleotides

	def counter(self):
		self.A = self.nucleotides.count('A')
		self.C = self.nucleotides.count('C')
		self.G = self.nucleotides.count('G')
		self.T = self.nucleotides.count('T')
		
		return self.A, self.C, self.G, self.T







nucleotide = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"

#nucleotide = sys.argv[1]
test = NucleotideCounter(nucleotide)

print(test.counter())




