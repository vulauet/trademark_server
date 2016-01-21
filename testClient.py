import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('112.137.130.32', 12055))
s.send('test')
result = s.recv(1024)
print result
s.close()