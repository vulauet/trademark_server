#!/usr/bin/python
from SocketServer import ThreadingMixIn
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import threading
from os import curdir
from os.path import join as pjoin
from os import makedirs
from os import system
from datetime import datetime
import cgi
import MySQLdb
# import mysql.connector as mariadb
import json
import decimal

PORT_NUMBER = 12055

#This class will handles any incoming request from
#the browser 
class myHandler(BaseHTTPRequestHandler):

	def do_POST(self):
		if self.path == '/image_upload':
			form = cgi.FieldStorage(
				fp=self.rfile,
				headers=self.headers,
				environ={'REQUEST_METHOD':'POST', 'CONTENT_TYPE':self.headers['Content-Type'],})
			filename = form['media'].filename
			content_length = int(self.headers['Content-Length'])
			data = form['media'].file.read(content_length)
			savename = str(datetime.now().microsecond) + ".jpg"
			open('./index/' + savename, "wb").write(data)
			brand = self.getBrand(savename)
			info = self.getBrandInfo(brand)
			self.reply(json.dumps(info))

	def do_GET(self):
		if self.path == '/update':
			# db = MySQLdb.connect("localhost", "root", "toor", "banknote")
			db = MySQLdb.connect("localhost", "vula", "pass", "vula")
			cursor = db.cursor()
			cursor.execute('SELECT base_banknote_code, rate_banknote_code, rate FROM update_exchange_rate')
			rows = cursor.fetchall()
			columns = [desc[0] for desc in cursor.description]
			rate = []
			if hasattr(rows, '__iter__'):
				for row in rows:
					row = dict(zip(columns, row))
					rate.append(row)

			cursor.execute('SELECT last_update FROM update_exchange_rate LIMIT 1')
			last_update = cursor.fetchone()
			db.close()
			result = {'rate': rate, 'last_update': last_update[0]}
			self.reply(json.dumps(result, default=object_serial))
		return

	def reply(self, response, status=200):
		self.send_response(status)
		self.send_header('Content-type','text/html')
		self.send_header('Content-length', len(response))
		self.end_headers()
		self.wfile.write(response)

	def getBrand(self, savename):
		retrieve_list = open('./log/retrieve_list.txt', 'r').read().split()
		retrieve_list[0] = savename
		open('./log/retrieve_list.txt', 'w').write(' '.join(retrieve_list))
		open('./log/extract_image.txt', "w").write(savename)
		system("extract extract_image.txt 6 ./index ./log >> ./log/extract_log.txt")
		system('retrieve brand.idx retrieve_list.txt 6 ./index ./log -t ./log/retrieve_result.txt')
		retrieve_result = open('./log/retrieve_result.txt', 'r').read().split()
		return retrieve_result[1][:6]

	def getBrandInfo(self, bsin):
		# db = MySQLdb.connect("localhost", "root", "toor", "trademark")
		db = MySQLdb.connect("localhost", "vula", "pass", "vula")
		cursor = db.cursor()
		cursor.execute("""SELECT brand_nm, brand_type_cd, brand_link FROM brand WHERE bsin = %s""", (bsin,))
		rows = cursor.fetchone()
		columns = [desc[0] for desc in cursor.description]
		cursor.execute("SELECT owner_cd FROM brand_owner_bsin WHERE bsin = %s", (bsin,))
		owner_cd = cursor.fetchone()
		if owner_cd is not None:
			cursor.execute("SELECT owner_nm, owner_link, owner_wiki_en FROM brand_owner WHERE owner_cd = %s", (owner_cd,))
			rows += cursor.fetchone()
			columns += [desc[0] for desc in cursor.description]
		db.close()
		return dict(zip(columns, rows))

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
	"""Handle requests in a separate thread."""

def object_serial(obj):
	if isinstance(obj, datetime):
		serial = obj.isoformat()
		return serial
	elif isinstance(obj, decimal.Decimal):
		return float(obj)
	raise TypeError("Type not serializable")

if __name__ == '__main__':
	try:
		#Create a web server and define the handler to manage the
		#incoming request
		# server = HTTPServer(('', PORT_NUMBER), myHandler)
		server = ThreadedHTTPServer(('', PORT_NUMBER), myHandler)
		print 'Started httpserver on port ' , PORT_NUMBER
		
		#Wait forever for incoming htto requests
		server.serve_forever()

	except KeyboardInterrupt:
		print '^C received, shutting down the web server'
		server.socket.close()
