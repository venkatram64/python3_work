import socket

def my_server():
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    my_socket.bind(("localhost", 4546))
    while True:

        client, addr = my_socket.recvfrom(2048)
        print(client)
        print("address of the client " + str(addr))
        msg = "Knock Knock Knock, I'm server"
        my_socket.sendto(msg, addr)

    my_socket.close()


if __name__ == '__main__':
    my_server()

