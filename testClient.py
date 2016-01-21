import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('112.137.130.32', 12055))
# s.send('test')
data = 'BT.jpg'
imp = open(data, 'r')
while True:
	strng = imp.readline(512)
	if not strng:
		break
	s.send(strng)
imp.close()
result = s.recv(1024)
print result
s.close()
exit()