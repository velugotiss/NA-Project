import socket

def server():

    port = 6000  # initiate port no above 1024
    s = socket.socket()  # get instance
    s.bind(('', port))  # bind host address and port together
    s.listen(1)
    conn, addr = s.accept()  # accept new connection
    print("Connection from: " + str(addr))

    while True:
        data = conn.recv(1024).decode()
        if data == "Bye from Client Srinivas":
            print(data)
            conn.send(str.encode("Bye from Server Srinivas"))
            break
        elif data == "Hello from Client Srinivas":
            print(data)
            conn.send(str.encode("Hello from Server Srinivas"))
        else:
            print(data)
            conn.send(data.encode())  # send data to the client

    conn.close()  # close the connection

if __name__ == '__main__':
    server()
