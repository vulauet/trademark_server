import SocketServer

class MyTCPServer(SocketServer.ThreadingTCPServer):
	allow_reuse_address = True

class MyTCPServerHandler(SocketServer.BaseRequestHandler):
	def handle(self):
		try:
			inp = self.request.recv(1024).strip()
			print inp
			self.request.sendall("Received")
		except Exception, e:
			print "[e] Excetion while receiving message: ", e

server = MyTCPServer(('0.0.0.0', 12055), MyTCPServerHandler)
server.serve_forever()