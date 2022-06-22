import socket

client_socket = socket.socket()
client_socket.connect(("127.0.0.1", 9191))


while True:
    message = input("Enter Message: ")
    if message == "quit":
        break
    client_socket.send(message.encode())
    data = client_socket.recv(1024)
    print("Received: ", repr(data.decode()))

client_socket.close()
