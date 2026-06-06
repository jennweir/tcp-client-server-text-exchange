import socket

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('127.0.0.1', 12345) 

    try:
        server_socket.bind(server_address)
        server_socket.listen(5) 
        print("Server listening on port 12345...")

        # TODO: Upgrade this to handle multiple clients concurrently using threads
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")

        try:
            # run in a loop to continuously receive messages from a client until it disconnects
            while True:
                message = client_socket.recv(1024).decode('utf-8').strip()
                print(f"Received: {message}")
                # parse PUT/GET commands

                response = "Message received\n".encode('utf-8')
                client_socket.sendall(response)

        except Exception as e:
            print(f"Error: {e}")
        finally:
            client_socket.close()

    except Exception as e:
        print(f"Server error: {e}")
    finally:
        server_socket.close()

if __name__ == "__main__":
    main()
