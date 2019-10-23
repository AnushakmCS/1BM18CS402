from socket import *
servername="10.124.6.97"
serverPort=12000
clientSocket=socket(AF_INET,SOCK_STREAM)
clientSocket.connect((servername,serverPort))
sentence=input("enter file name")

clientSocket.send(sentence.encode())
filecontent=clientSocket.recv(1024).decode()
print('Freom Server:',filecontent)
clientSocket.close()
