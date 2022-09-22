import socket
import logging

logging.basicConfig(filename="server.log", format='%(asctime)s %(clientip)-15s %(user)-8s %(message)s', level=logging.INFO)
port = 9090

while True:
    sock = socket.socket() 
    sock.bind(('', port)) 
    sock.listen(1)
    print(f"Server has started, listens port {port}")
    logging.info(f"Server has started, listens port {port}")
    conn, addr = sock.accept()
    print(addr)
    

    while True:
        data = conn.recv(1024).decode()
        if not data or data == "exit":
            break
        print(data)
    print("Connection closed")                                                 
    logging.info("Connection closed") 
    conn.close()
