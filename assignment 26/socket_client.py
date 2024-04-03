
import socket

def connect_to_server():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))  # Connect to the server on localhost port 12345

    message = client_socket.recv(1024)  # Receive the welcome message from the server
    print(message.decode("utf-8"))

    client_socket.close()

if __name__ == "__main__":
    connect_to_server()
