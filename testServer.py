import SocketServer
import os

class MyTCPServer(SocketServer.ThreadingTCPServer):
	allow_reuse_address = True

class MyTCPServerHandler(SocketServer.BaseRequestHandler):
	def handle(self):
		try:
			# inp = self.request.recv(1024).strip()
			
			fname = "logo.jpg"
			fp = open(fname, 'w')
			while True:
				strng = self.request.recv(512)
				if not strng:
					break
				fp.write(strng)
			fp.close()
			# im = Image.open(fname)
			# im.save("logo", "JPEG")
			self.request.sendall("Received")
		except Exception, e:
			print "[e] Excetion while receiving message: ", e

server = MyTCPServer(('0.0.0.0', 12055), MyTCPServerHandler)
server.serve_forever()