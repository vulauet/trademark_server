import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('128.199.160.37', 12055))
print "Sending..."
s.send('test')
# data = 'BT.jpg'
# imp = open(data, 'r')
# while True:
	# strng = imp.read(512)
	# if not strng:
		# break
	# #print strng
	# s.send(strng)
# imp.close()
print s.recv(1024)
print 1
s.close()
exit()