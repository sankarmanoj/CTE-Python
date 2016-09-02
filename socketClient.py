from socket import *
client = socket()
client.connect(("localhost",5432))
while True:
    client.send(raw_input("Enter Input"))
