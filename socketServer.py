from socket import *
from threading import *
def clientHandler(client):
    while True:
        print client.recv(1000)
server = socket()
server.bind(("",5432))
server.listen(5)
while True:
    client,address = server.accept()
    Thread(target=clientHandler,args=(client,)).start()
