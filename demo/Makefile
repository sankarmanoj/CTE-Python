CC=gcc

all: server.out client.out

server.out: server.c
	$(CC) -lpthread -pthread server.c -o server.out

client.out: client.c
	$(CC) client.c -o client.out

clean:
	rm *.out
