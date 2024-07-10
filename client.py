import socket

s = socket.socket(socket.AF_INET , socket.SOCK_STREAM , socket.IPPROTO_TCP)

s.connect( ("127.0.0.1" , 4444 ))

data = s.recv(512)

print(data.decode())

s.send("It is great to have network programming".encode())

# Device 2