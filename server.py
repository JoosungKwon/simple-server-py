import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

server_socket.bind(("127.0.0.1", 9191))

server_socket.listen(5)

client_socket, addr = server_socket.accept()
print("Connected: ", addr)

while True :
    data = client_socket.recv(1024)
    
    if not data :
        break
    
    print("Received from", addr, data.decode())
    
    client_socket.sendall(data)
    
client_socket.close()
server_socket.close()
    
    