from collections import deque

class InboundPort:
	inboundQueue = deque()

	def receive(self, message):
		self.inboundQueue.append(message)

	def printAll(self):
		sb = ''

		for message in self.inboundQueue:
			sb+=message

		return sb
