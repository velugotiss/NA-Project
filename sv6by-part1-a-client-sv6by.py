import socket
// Python Code
def client_socket():
    host = socket.gethostbyname('192.168.1.161')  # as both code is running on same pc
    port = 6000  # socket server port number

    s = socket.socket()  # instantiate
    s.connect((host, port))  # connect to the server

    msg = input("Enter input -> \n")  # take input
    while True:  
            if msg == "Bye from Client Srinivas":
                s.send(msg.encode())
                data = s.recv(1024).decode()
                print(data)
                if(data == "Bye from Server Srinivas"):
                    break
                else:
                    message=input("Take another input \n")
            elif msg == "Hello from Client Srinivas":
                s.send(msg.encode())
                data= s.recv(1024).decode()
                print(data)
                msg = input("Take another input")
            else:
                s.send(msg.encode())
                data = s.recv(1024).decode()
                print(data)
                msg = input("Enter message: \n")

    s.close()  # close the connection

if __name__ == '__main__':
    client_socket()
