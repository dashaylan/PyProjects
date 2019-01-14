import sys

#Solution to http://rosalind.info/problems/gc/

def parser(f):

	fasta = []
	segments = []
	index = 0

	#Open file, use bit to ignore first entry increment
	#Create an entry tuple that will hold name segment and nucleotides on >
	#Add nucleotides to current tuple if no > first
	with open(f, "r") as file:

		bit = 0

		for line in file:
			line = line.rstrip('\n')
			if line[0] == ">":

				if bit == 1:
					index += 1
				else:
					bit = 1

				entry = []
				entry.append(line)
				fasta.append(entry)


			else:
				fasta[index].append(line)

	#Concatenate the nucleotides in each entry and calculate GC content
	#Easier to make a new list since nucleotide entries is unknown per fasta entry

		for item in fasta:
			concat = ''.join(item[1:])
			A, T = concat.count('A'), concat.count('T')
			G, C = concat.count('G'), concat.count('C')
			GC = (float(G+C) / float(A+T+G+C))*100
			entry = []
			entry.append(item.pop(0))
			entry.append(concat)
			entry.append(GC)
			segments.append(entry)

			#print(A, T, G, C, G+C, A+T+G+C, GC)

		
	#Use GC content to calculate max instead of fasta label
	print(segments)
	print(max(segments, key = lambda segment: segment[2]))


			

parser("rosalind_gc.txt")
