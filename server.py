from twisted.internet import reactor
from twisted.internet.protocol import Factory, Protocol

class  IphoneChat(Protocol):
	"""docstring for  IphoneChat"Protocolf __init__(self, arg):
		super( IphoneChat,Protocol.__init__()
		self.arg = arg"""

	def connectionMade(self):
		self.factory.clients.append(self)
		print "clients are ", self.factory.clients
		
	def connectionLost(self, reason):
		self.factory.clients.remove(self)

	def dataReceived(self, data):
		a = data.split(':')
		print a
		if len(a) > 1:
			command = a[0]
			content = a[1]

			msg = ""
			if command == "iam":
				self.name = content
				msg = self.name + " has joined"

			elif command == "msg":
				msg = self.name + ": " + content
				print msg

			for c in self.factory.clients:
				c.message(msg)

	def message(self, message):
		self.transport.write(message + '\n')

factory = Factory()
factory.protocol = IphoneChat
factory.clients = []
reactor.listenTCP(8080, factory)
print "Iphone Chat server started"
reactor.run()