import socket
import getpass
def port_address_name():
    addr = input("Input addres: ")
    port = int(input("Input port : "))
    return (addr, port) 

def connect_to_server():
    sock = socket.socket()
    sock.connect(port_address_name())
    #msg = input()
    msg = ""
    while True:
        msg = input()
        if msg == "exit":
            break
        sock.send(msg.encode())
    
    sock.close()

if __name__ == "__main__":
    connect_to_server()
