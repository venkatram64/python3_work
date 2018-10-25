import socket

def my_client():
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    my_socket.connect((host, 4545))
    data = my_socket.recv(2048)
    my_socket.close()
    print(data.decode('ascii'))



if __name__ == '__main__':
    my_client()