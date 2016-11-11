from socket import *
serversocket = socket()
address = ("",12345)
serversocket.bind(address)
serversocket.listen(5)
(client,clientaddress)=serversocket.accept()
print clientaddress
client.send("Hello World")
print client.recv(1000)
serversocket.close()
