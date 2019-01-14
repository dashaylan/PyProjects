import sys

#Solution to http://rosalind.info/problems/hamm/

def hamm(s, t):
	count = 0

	for i, n in enumerate(s):
		if t[i] != n:
			count += 1

	print(count)

s1 = "GAGCCTACTAACGGGAT"
t1 = "CATCGTAATGACGGCCT"
hamm(s1, t1)
