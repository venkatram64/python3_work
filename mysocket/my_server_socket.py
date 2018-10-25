import socket

def my_server():
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    my_socket.bind((host, 4545))
    my_socket.listen(5)
    while True:
        client,addr = my_socket.accept()
        print("Got a connection form %s" % str(addr))
        msg = "Knock Knock Knock, I'm server"
        client.send(msg.encode('ascii'))

    my_socket.close()


if __name__ == '__main__':
    my_server()

