import socket
from threading import Thread

class MyClient:

    def start_client2(self):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(("127.0.0.1", 4545))
        while True:
            client_msg = input("Enter a message to send server:\n ")
            client_socket.send(client_msg.encode("utf8"))
            msg_from_server = client_socket.recv(4096)
            print("Received msg from server is {} ".format(msg_from_server.decode("utf8")))
            if client_msg == "quit":
                break
        client_socket.close()

    def start_client(self):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(("127.0.0.1", 4545))
        receive_thread = Thread(target=self.receive, args=(client_socket,))
        receive_thread.start()
        send_thread = Thread(target=self.send, args=(client_socket,))
        send_thread.start()

    def receive(self, conn, MAX_BUFFER_SIZE=4096):
        while True:
            msg = conn.recv(MAX_BUFFER_SIZE).decode("utf8")
            if msg == "quit":
                conn.close()
                break
            if not msg:
                break
            print(msg)

    def send(self, conn):
        while True:
            msg = input("Enter: ")
            conn.send(bytes(msg, "utf8"))
            if msg == "quit":
                break


if __name__ == "__main__":
    myclient = MyClient()
    myclient.start_client()
