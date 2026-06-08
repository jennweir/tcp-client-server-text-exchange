# tcp-client-server-text-exchange

Demonstrates fundamental Inter-Process Communication (IPC) by upgrading a basic TCP echo server into a concurrent, stateful distributed key-value node.

## TCP client-server text exchange

### Prerequisites

- Client code must be updated and saved in `client.py`
- Server code must be updated and saved in `server.py`

### Run the TCP echo server

- Navigate to the directory that contains `server.py`
- Run the server with `python3 server.py`
- At this point, the server should be listening

### Run the client

- In a separate terminal, navigate to the directory that contains `client.py`
- Run the client with `python3 client.py`
- At this point, the client will connect to the server

### Test Commands

When prompted by the client, test a key-value store by typing commands (and then pressing Enter) such as:

- PUT name Alice
- GET name

### Test Concurrency

When one client is still running, open another terminal and run another client. Verify both clients can send commands to the server without blocking or crashing.

Type EXIT in the clients to verify they close cleanly.
