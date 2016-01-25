#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import json

PORT_NUMBER = 12055

#This class will handles any incoming request from
#the browser 
class myHandler(BaseHTTPRequestHandler):
	
	#Handler for the GET requests
	def do_GET(self):
		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()
		# Send the html message
		self.wfile.write(json.dumps([{'speech_id':1, 'speech_title': '001', 'speech_description': 'Test 1', 'speech_script': 'Test 1', 'speech_link': 'facebook.com', 'user_id': 1, 'topic': 'Toefl', 'created_at': '', 'updated_at': ''},
				{'speech_id':002, 'speech_title': '002', 'speech_description': 'Test 2', 'speech_script': 'Test 2', 'speech_link': 'facebook.com', 'user_id': 1, 'topic': 'IELTS', 'created_at': '', 'updated_at': ''},
				{'speech_id':003, 'speech_title': '003', 'speech_description': 'Test 3', 'speech_script': 'Test 3', 'speech_link': 'facebook.com', 'user_id': 3, 'topic': 'TOEIC', 'created_at': '', 'updated_at': ''},
				{'speech_id':004, 'speech_title': '004', 'speech_description': 'Test 4', 'speech_script': 'Test 4', 'speech_link': 'facebook.com', 'user_id': 2, 'topic': 'TOEFL', 'created_at': '', 'updated_at': ''},
				{'speech_id':005, 'speech_title': '005', 'speech_description': 'Test 5', 'speech_script': 'Test 5', 'speech_link': 'facebook.com', 'user_id': 2, 'topic': 'TOEFL', 'created_at': '', 'updated_at': ''}]))
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