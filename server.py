import socket
import threading

def handle_client_connections(client_socket, client_address):
    try:
        # run in a loop to continuously receive messages from a client until it disconnects
        while True:
            message = client_socket.recv(1024).decode('utf-8').strip()
            print(f"Received: {message} from {client_address}")
            # parse PUT/GET commands
            if message == "PUT":
                # handle PUT command
                pass
            
            if message == "GET":
                # handle GET command
                pass

            response = "Message received\n".encode('utf-8')
            client_socket.sendall(response)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('127.0.0.1', 12345) 
    threads = []

    try:
        server_socket.bind(server_address)
        server_socket.listen(5) 
        print("Server listening on port 12345...")

        while True:
            client_socket, client_address = server_socket.accept()
            print(f"Connection from {client_address}")
            # create daemon threads to handle each client connection concurrently
            # use daemon threads so they will automatically be cleaned up when the server shuts down
            thread = threading.Thread(target=handle_client_connections, args=(client_socket, client_address), daemon=True)
            thread.start()
            threads.append(thread)


    except Exception as e:
        print(f"Server error: {e}")
    finally:
        server_socket.close()

if __name__ == "__main__":
    main()
