import socket
import sys
from threading import Thread
import traceback


class MyServer:

    def start_server(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = socket.gethostname()
        try:
            server_socket.bind(("127.0.0.1", 4545))
        except socket.error as msg:
            print("Bind failed. Error: " + str(sys.exc_info()))
            sys.exit()

        #Start listening on socket
        server_socket.listen(10)
        print("Socket now listening.")

        #
        while True:
            conn, addr = server_socket.accept()
            ip, port = str(addr[0]), str(addr[1])
            print("Accepting connection from " + ip + ": " + port)
            try:
                Thread(target=self.client_thread, args=(conn, ip, port)).start()
            except:
                print("Terrible error.")
                traceback.print_exc()

        server_socket.close()

    def client_thread(self, conn, ip, port, MAX_BUFFER_SIZE=4096):

        while True:
            msg = conn.recv(MAX_BUFFER_SIZE)
            size = sys.getsizeof(msg)
            if size >= MAX_BUFFER_SIZE:
                print("The length of input is long: {}".format(size))
            msg_decode = msg.decode("utf8").rstrip()
            print("Message received from client is {}".format(msg_decode))
            msg_to_send_to_client = self.reverse_msg(msg_decode)

            if msg_decode != "quit":
                msg_to_send_to_client_encode = msg_to_send_to_client.encode("utf8")
                conn.sendall(msg_to_send_to_client_encode)
            else:
                conn.close()
                print("Connection " + ip + ": " + port + " ended")

    def reverse_msg(self, msg):
        return msg[::-1]


if __name__ == "__main__":
    myserver = MyServer()
    myserver.start_server()