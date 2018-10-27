
import socket

def remote_host_name():
    rhost = input("Enter host name: ")
    rip = socket.gethostbyname(rhost)

    try:
        print("IP address of remote host is ", rip)
    except:
        print("Error")



if __name__ == '__main__':
    remote_host_name()   #www.google.com
