import socket

# Host can be IP or web domain (URL)
target_host = "www.google.com"

# Target port 
target_port = 80

# Create socket object 
# AF_INET indicates hostname or IPv4
# SOCK_STREAM indicates TCP 
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to Client
client.connect((target_host, target_port))

# send data
# b indicates send as bytes 
client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

# receice data
response = client.recv(4096)

# print / decode 
print(response.decode())

# Close connection 
client.close()