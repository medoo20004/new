import socket
host= '192.168.8.152'
port= 9999
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))