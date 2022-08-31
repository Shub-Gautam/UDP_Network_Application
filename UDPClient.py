from socket import * 
serverName = "120.0.0.1"
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input('Input your data: ')
clientSocket.sendto(message.encode(),(serverName,serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())
clientSocket.close() 
