import sys

#LinkedList implementation

class LinkList:
	def __init__(self, data):
		self.data = data
		self.next = None

	def increment(self, data):
		node = LinkList(data)
		end = self
		while end.next != None:
			#print end.data
			end = end.next
		end.next = node

	def printData(self):
		end = self
		while end.next != None:
			print end.data
			end = end.next
		print end.data



def testLinked():

	ll = LinkList("hi")
	ll.increment("you")
	ll.increment("gr8")
	ll.increment("stuff")

	ll.printData()


testLinked()

