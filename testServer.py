import SocketServer
import os
from datetime import datetime


class MyTCPServer(SocketServer.ThreadingTCPServer):
	allow_reuse_address = True

class MyTCPServerHandler(SocketServer.BaseRequestHandler):
	def handle(self):
		try:
			# inp = self.request.recv(1024).strip()
			
			timeStamp = str(datetime.now().microsecond)
			annotation = timeStamp + ".txt"
			fname =  timeStamp + ".jpg"
			fp = open(fname, 'w')
			while True:
				strng = self.request.recv(512)
				fp.write(strng)
				if len(strng)<512:
					break
				
			fp.close()
			annotate = open(annotation, 'w')
			annotate.write(fname)
			annotate.close()
			os.system("extract " + annotation + " 6 . .")
			self.request.sendall("Received\n")
		except Exception, e:
			print "[e] Excetion while receiving message: ", e

server = MyTCPServer(('0.0.0.0', 12055), MyTCPServerHandler)
server.serve_forever()