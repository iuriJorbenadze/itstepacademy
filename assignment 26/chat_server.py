
import socket

def start_chat_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12346))  # Bind to localhost on port 12346
    server_socket.listen(1)
    print("Chat server is listening for connections on localhost:12346")

    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")

    with open('chat_history.txt', 'w') as file:
        while True:
            data = conn.recv(1024)
            if not data:
                break  # Exit the loop if no data is sent
            message = data.decode("utf-8")
            print(f"Received: {message}")
            file.write(f"{addr}: {message}
")
            conn.sendall(data)  # Echo back the received message

    conn.close()

if __name__ == "__main__":
    start_chat_server()
