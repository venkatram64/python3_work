import socket

def my_client():
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    my_socket.connect(("127.0.0.1", 4546))
    my_socket.sendto("Hello from client".encode('ascii'), ("127.0.0.1", 4546))
    data = my_socket.recvfrom(2048)
    my_socket.close()
    print(data)


if __name__ == '__main__':
    my_client()