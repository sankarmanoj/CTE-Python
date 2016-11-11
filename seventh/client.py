from socket import *
client = socket()
client.connect(("127.0.0.1",12345))
print client.recv(1000)
client.send("Good Bye")
