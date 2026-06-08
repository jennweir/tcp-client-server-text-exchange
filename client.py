import socket

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('127.0.0.1', 12345)
    client_socket.settimeout(15)  # timeout of 15 sec for socket operations

    try:
        # attempt to connect to the server; handle connection errors as needed
        try:
            client_socket.connect(server_address)
        except ConnectionRefusedError:
            print("Error: Connection refused due to server not running on port 12345")
            return
        except socket.timeout:
            print("Error: Connection timeout due to server not responding")
            return

        # run in a loop to continuously prompt the user for input to send to the server until they choose to exit
        while True:
            message = input("Enter command (`PUT key value` or `GET key`): ").strip()
            # close the connection if the user types "EXIT" signifying they want to disconnect
            if message == "EXIT":
                break
            
            try:
                # send input to the server
                client_socket.sendall((message + "\n").encode('utf-8'))
                # receive the response from the server; handle connection errors as needed
                response = client_socket.recv(1024).decode('utf-8').strip()
                if not response:
                    print("Error: Connection with server lost")
                    break
                print(f"Server response: {response}")
            except socket.timeout:
                print("Error: Server response timeout due to client not receiving data for 15 seconds")
                break
            except ConnectionResetError:
                print("Error: Connection reset by server")
                break
            except BrokenPipeError:
                print("Error: Connection with server lost")
                break

    except Exception as e:
        print(f"Client error: {e}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    main()