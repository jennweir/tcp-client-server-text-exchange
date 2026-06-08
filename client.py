import socket

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('127.0.0.1', 12345) 

    try:
        client_socket.connect(server_address)

        # run in a loop to continuously prompt the user for input to send to the server until they choose to exit
        while True:
            message = input("Enter command (`PUT key value` or `GET key`): ").strip()
            # close the connection if the user types "EXIT" signifying they want to disconnect
            if message == "EXIT":
                break
            client_socket.sendall((message + "\n").encode('utf-8'))

            response = client_socket.recv(1024).decode('utf-8').strip()
            print(f"Server response: {response}")

    except Exception as e:
        print(f"Client error: {e}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    main()