import socket
import threading
import time

def handle_client_connections(client_socket, client_address, storage):
    client_socket.settimeout(180)  # 180 second timeout to detect stalled clients
    try:
        # run in a loop to continuously receive messages from a client until it disconnects
        while True:
            try:
                message = client_socket.recv(1024).decode('utf-8').strip()
            except socket.timeout:
                print(f"Timeout: No data from {client_address} for 180 seconds")
                break
            # if message is empty, the client has disconnected. handle broken client connection gracefully
            if not message:
                break
            print(f"Received: {message} from {client_address}")
            # parse PUT/GET commands
            if message.startswith("PUT"):
                # handle PUT command
                # split the message into the 3 expected pieces and inserting the key and value into the storage dictionary
                try:
                    _, key, value = message.split()
                except ValueError:
                    response = "Error: PUT command requires both a non-empty key and value. Try again.\n"
                    client_socket.sendall(response.encode('utf-8'))
                    continue
                storage[key] = value
                # return 'OK' for successful PUT commands
                response = "OK\n".encode('utf-8')

            elif message.startswith("GET"):
                # handle GET command
                # split the message into the 2 expected pieces and retrieving the value for the key from the storage dictionary
                try:
                    _, key = message.split()
                except ValueError:
                    response = "Error: GET command requires a non-empty key. Try again.\n"
                    client_socket.sendall(response.encode('utf-8'))
                    continue
                # return 'NOT FOUND' if the user requests a key that does not exist
                value = storage.get(key, "NOT FOUND")
                response = f"{value}\n".encode('utf-8')

            else:
                response = "Error: Invalid command. Either `PUT key value` or `GET key` are accepted.\n".encode('utf-8')

            client_socket.sendall(response)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('127.0.0.1', 12345) 
    threads = []
    storage = {}  # in-memory key-value store for PUT/GET client commands

    try:
        try:
            server_socket.bind(server_address)
        except Exception as e:
            if "Address already in use" in str(e):
                print("Error: Port 12345 is already in use. Please free the port and try again.")
                return
            
        server_socket.listen(5) 
        print("Server listening on port 12345...")

        while True:
            # accept client connections and create threads to run client logic concurrently
            client_socket, client_address = server_socket.accept()
            print(f"Connection from {client_address}")
            # create daemon threads to handle each client connection concurrently
            # use daemon threads so they will automatically be cleaned up when the server shuts down
            thread = threading.Thread(target=handle_client_connections, args=(client_socket, client_address, storage), daemon=True)
            thread.start()
            threads.append(thread)


    except Exception as e:
        print(f"Server error: {e}")
    finally:
        server_socket.close()

if __name__ == "__main__":
    main()
