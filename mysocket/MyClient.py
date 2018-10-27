
import socket

class MyClient:

    def start_client(self):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(("127.0.0.1", 4545))
        while True:
            client_msg = input("Enter a message to send server:\n ")
            if client_msg == "bye":
                client_socket.close()
                break
            client_socket.send(client_msg.encode("utf8"))
            msg_from_server = client_socket.recv(4096)
            print("Received msg from server is {} ".format(msg_from_server.decode("utf8")))



if __name__ == "__main__":
    myclient = MyClient()
    myclient.start_client()
