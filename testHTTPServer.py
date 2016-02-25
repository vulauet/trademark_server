#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from os import curdir
from os.path import join as pjoin
from datetime import datetime

PORT_NUMBER = 12055

#This class will handles any incoming request from
#the browser 
class myHandler(BaseHTTPRequestHandler):
	trademark_path = pjoin(curdir, str(datetime.now().microsecond) + ".jpg")

	#Handler for the GET requests
	def do_GET(self):
		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()
		# Send the html message
		self.wfile.write("Hello World !")
		return

	def do_POST(self):
		if self.path == '/trademark.jpg':
			length = self.end_headers['content-length']
			data = self.rfile.read(int(length))

			with open(self.trademark_path, 'w') as fh:
				fh.write(data.decode())
			self.send_response(200)
		return

try:
	#Create a web server and define the handler to manage the
	#incoming request
	server = HTTPServer(('', PORT_NUMBER), myHandler)
	print 'Started httpserver on port ' , PORT_NUMBER
	
	#Wait forever for incoming htto requests
	server.serve_forever()

except KeyboardInterrupt:
	print '^C received, shutting down the web server'
	server.socket.close()