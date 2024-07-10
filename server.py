import socket

s = socket.socket(socket.AF_INET , socket.SOCK_STREAM , socket.IPPROTO_TCP)

s.bind( ("127.0.0.1" , 4444) )

print("Listening for connections ...")
s.listen(1)

conn, addr = s.accept()

conn.send("Hey, I have recieved your connection".encode())

print("A connection recieved, and a message sent.")

data = conn.recv(512)

data = data.decode()

print(data)

conn.close()
s.close()

# Device 1