from threading import *
from time import sleep
def printing():
    while True:
        print "Hello"
        sleep(2)

printingThread = Thread(target=printing)
printingThread.start()
while True:
    print raw_input("Enter a message:")
