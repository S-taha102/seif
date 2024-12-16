import socket
import threading

def receive_messages(sock):
    """
    Function to continuously receive messages from the server.
    """
    while True:
        message = sock.recv(1024)
        if not message:
            print("Disconnected from server.")
            break
        print(f"\nMessage: {message.decode()}")

def send_messages(sock):
    """
    Function to send messages to the server.
    """
    while True:
        message = input("Enter message: ")
        sock.sendall(message.encode())

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    print(f"Connect {HOST}:{PORT}")

    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    print("Connected to the chat server.\n")

    
    receive_thread = threading.Thread(target=receive_messages, args=(sock,))
    send_thread = threading.Thread(target=send_messages, args=(sock,))
    
    receive_thread.start()
    send_thread.start()

    
    receive_thread.join()
    send_thread.join()
