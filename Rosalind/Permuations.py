import sys
from itertools import permutations
import itertools

#Function to solve http://rosalind.info/problems/sign/

#Most of the work in this page is just to create
#an output suitable for Rosalind

def perm(n):

	q = list(range(1,n+1))
	
	answer = permutations(q)
	

	#print(len(list(cp)))

	permlist = []
	permlist.append(list(answer))
	permlist = permlist.pop()

	signed = []

	for thing in permlist:
		signed.insert(0,table(thing))
	
	flat = [item for sublist in signed for item in sublist]

	flat = stripping(flat)

	#print (flat)


	for ans in flat:
		print(ans)



def table(p):

	n = len(p)
	tab = list(itertools.product(['-', ''], repeat=n))


	f = []

	for index in tab:
		s = []
		for i, entry in enumerate(index):
			s.append(int(entry+str(p[i])))
		f.append(s)

	

	return f
	#print("-2")


def stripping(l):
	real = []
	cp = 0

	for i in l:
		
		perm = ""
		for entry in i:
			perm += str(entry)+' '
		perm = perm.strip()
		cp += 1
		
		real.append(perm)
		perm = ""
	real.insert(0, cp)

	return real


perm(3)
#table([1,2,3])
