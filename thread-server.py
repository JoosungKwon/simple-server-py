from _thread import *
import socket


def threaded(client_socket, sock_addr):
    print('Connected: ', sock_addr[0], ":", sock_addr[1])

    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                print("Error")
                break
            print("Received: ", data.decode())

            client_socket.send(data)

        except ConnectionResetError as e:
            print("Disconnected: ", sock_addr[0], ':', sock_addr[1])
            break
    client_socket.close()


server_socket = socket.socket()
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind(("", 9191))
server_socket.listen(5)

print('Server Start')

while True:
    print("Wait")

    client_socket, sock_addr = server_socket.accept()
    start_new_thread(threaded, (client_socket, sock_addr))

server_socket.close()
