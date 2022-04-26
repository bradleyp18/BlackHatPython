from http import client
import socket
import threading

# IP Address
HOST = '0.0.0.0'
# IP Port
PORT = '42069'

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST,PORT))
    # Number of listening connections
    server.listen(5)
    print(f"Listening on {HOST}:{PORT}")

    while True:
        client, addr = server.accept()
        print(f"[*] Accepted connection from {addr[0]}:{addr[1]}")
        client_handler = threading.Thread(target=handle_client, args = (client,))
        client_handler.start()

def handle_client(client_socket):
    with client_socket as socket:
        request = socket.recv(1024)
        print(f" Received: {request.decode()}")
        socket.send(b'ACK')

if __name__ == "__main__":
    main()