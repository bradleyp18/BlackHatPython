import socket 

# Target URL or IPv4 
target_host = "127.0.0.1"

# Target port
target_port = 9997

# Create socket connection
# SOCK_DGRAM indicates UDP
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Sent data, must use "sendto" for UDP 
client.sendto(b"Type Something to send here", (target_host, target_port))

# Receive some data
data, addr = client.recvfrom(4096)

# Print
print(data.decode())

# Close Connection 
client.close()