import socket

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('127.0.0.1', 12345) 

    try:
        client_socket.connect(server_address)

        # TODO: Upgrade this to a while loop that continuously takes user input until 'EXIT'
        message = input("Enter command (e.g., PUT key value): ") + "\n"
        client_socket.sendall(message.encode('utf-8'))

        response = client_socket.recv(1024).decode('utf-8').strip()
        print(f"Server response: {response}")

    except Exception as e:
        print(f"Client error: {e}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    main()