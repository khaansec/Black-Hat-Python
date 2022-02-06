import socket

# init variables
target_port = 9998
target_host = "127.0.0.1"
#print("Enter the target host: ")
#target_host = input()
#print("Enter the target port: ")
#target_port = input()

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
client.connect((target_host,target_port))

# send some data
#client.send(b"GET / HTTP/1.1\r\n" + target_host + "\r\n\r\n")
client.send(b"GET / HTTP/1.1\r\nHost: ensign.edu\r\n\r\n")
#client.send(b"GET / HTTP/1.1\r\nHost: " + target_host + "\r\n\r\n")

# receive the data
response = client.recv(4096)

print(response.decode())
client.close()