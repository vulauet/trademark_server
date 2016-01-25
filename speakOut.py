import SocketServer
import json
import mysql.connector as mariadb
from datetime import datetime

# def get_shop_data(shopname):
    # connection = mariadb.connect(user='root', password='PP@@ssw0rd', database='shameal')
    # cursor = connection.cursor()
    # query = "SELECT * FROM shops_tbl WHERE name LIKE %s;"
    # cursor.execute(query, ('%' + shopname + '%',))
    # return cursor.fetchall()
    # for resp in cursor.fetchall():
        # cursor.close()
        # return resp

class MyTCPServer(SocketServer.ThreadingTCPServer):
    allow_reuse_address = True

class MyTCPServerHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        print "-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-"
        print "[+] " + str(datetime.now())
        try:
            # data = json.loads(self.request.recv(1024).strip())
            # process the data, i.e. print it:
            shopname = self.request.recv(1024).strip()
            # shopdata = get_shop_data(shopname)
            print "[+] Request: " + shopname
            # print "[+] Respone: " + str(shopdata)
            f = open("output.dat", "a")
            f.write("[+] Request: " + shopname + "\n\n\n")
            f.close()
			
            # send some 'ok' back
            self.request.sendall(
                json.dumps([{'speech_id':1, 'speech_title': '001', 'speech_description': 'Test 1', 'speech_script': 'Test 1', 'speech_link': 'facebook.com', 'user_id': 1, 'topic': 'Toefl', 'created_at': '', 'updated_at': ''},
				{'speech_id':002, 'speech_title': '002', 'speech_description': 'Test 2', 'speech_script': 'Test 2', 'speech_link': 'facebook.com', 'user_id': 1, 'topic': 'IELTS', 'created_at': '', 'updated_at': ''},
				{'speech_id':003, 'speech_title': '003', 'speech_description': 'Test 3', 'speech_script': 'Test 3', 'speech_link': 'facebook.com', 'user_id': 3, 'topic': 'TOEIC', 'created_at': '', 'updated_at': ''},
				{'speech_id':004, 'speech_title': '004', 'speech_description': 'Test 4', 'speech_script': 'Test 4', 'speech_link': 'facebook.com', 'user_id': 2, 'topic': 'TOEFL', 'created_at': '', 'updated_at': ''},
				{'speech_id':005, 'speech_title': '005', 'speech_description': 'Test 5', 'speech_script': 'Test 5', 'speech_link': 'facebook.com', 'user_id': 2, 'topic': 'TOEFL', 'created_at': '', 'updated_at': ''}])
                )
        except Exception, e:
            print "[e] Exception while receiving message: ", e
        print "-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-\n"

server = MyTCPServer(('0.0.0.0', 12055), MyTCPServerHandler)
server.serve_forever()
