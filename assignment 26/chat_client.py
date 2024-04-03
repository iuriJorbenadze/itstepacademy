
import socket

def start_chat_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12346))  # Connect to the chat server on localhost port 12346
    print("Connected to chat server. You can start sending messages.")

    try:
        while True:
            message = input("You: ")
            client_socket.sendall(message.encode("utf-8"))
            data = client_socket.recv(1024)
            print(f"Echoed back: {data.decode('utf-8')}")
    except KeyboardInterrupt:
        print("\nDisconnected from chat server.")

    client_socket.close()

if __name__ == "__main__":
    start_chat_client()
