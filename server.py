import socket
#from PIL import Image
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("", 5005))
server_socket.listen(5)
import os


client_socket, address = server_socket.accept()
print "Conencted to - ",address,"\n"
while (1):
    choice = client_socket.recv(1024)
    choice = int(choice)
    if(choice == 1):
        data = client_socket.recv(1024)
        print "The following data was received - ",data
        print "Opening file - ",data
        fp = open(data,'r')
 #       strng = fp.read()
        strng = "ok"
        size = os.path.getsize(data)
        size = str(size)
        client_socket.send(size)
        client_socket.send (strng)
        #client_socket.close()

    if (choice == 2 or choice == 3):
        data = client_socket.recv(1024)
        print "The following data was received - ",data
        print "Opening file - ",data
        img = open(data,'r')
        while True:
            strng = img.readline(512)
            if not strng:
                break
            print strng
            client_socket.send(strng)
        img.close()
        # im = Image.open(data)
        # im.save("logo", "JPEG")
        print "Data sent successfully"
        exit()
        #data = 'viewnior '+data
        #os.system(data)