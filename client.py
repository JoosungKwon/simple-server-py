import socket

client_socket = socket.socket()

client_socket.connect(("127.0.0.1", 9191))

client_socket.sendall("Successful Connected".encode())

data = client_socket.recv(1024)
print("Received", repr(data.decode()))

client_socket.close()
