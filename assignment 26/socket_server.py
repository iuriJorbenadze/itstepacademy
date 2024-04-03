
import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', 12345))  # Bind to localhost on port 12345, '' allows connection from any host
    server_socket.listen()

    print("Server is listening for connections...")

    while True:
        client_socket, address = server_socket.accept()
        print(f"Connection from {address} has been established.")

        client_socket.send(bytes("You are connected to the server.", "utf-8"))
        client_socket.close()
        break  # For this example, we'll close after one connection to keep it simple.

if __name__ == "__main__":
    start_server()
