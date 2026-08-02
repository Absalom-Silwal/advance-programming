import socket
import threading

# Define connection parameters
HOST = '127.0.0.1'  # Localhost
PORT = 65432  # Arbitrary non-privileged port

client_locks = threading.Lock()
active_client= []


def handle_client(client_socket, client_address):
    """Handles communication with a single connected client."""
    print(f"[NEW CONNECTION] {client_address} connected.")

    try:
        while True:
            # Receive data from the client (1024 bytes buffer)
            data = client_socket.recv(1024)
            if not data:
                # If data is empty, the client disconnected
                break

            message = data.decode('utf-8')
            print(f"[{client_address}] {message}")

            # Send a response back to the client
            response = f"Server received: {message}"
            #client_socket.sendall(response.encode('utf-8'))
            for conn,addr in active_client:
                if addr != client_address:
                    conn.sendall(response.encode('utf-8'))
    except ConnectionResetError:
        print(f"[WARNING] Connection forcibly closed by {client_address}")
    finally:
        # Clean up the socket connection
        client_socket.close()
        print(f"[DISCONNECTED] {client_address} disconnected.")


def start_server():
    """Initializes and runs the server."""
    # Create an IPv4 TCP socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Avoid "Address already in use" errors on restart
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server.bind((HOST, PORT))
    server.listen()  # Start listening for connections
    print(f"[LISTENING] Server is listening on {HOST}:{PORT}")

    while True:
        # Accept a new incoming connection (blocks until a client connects)
        client_socket, client_address = server.accept()

        # Spin up a new thread to handle this specific client
        client_thread = threading.Thread(
            target=handle_client,
            args=(client_socket, client_address)
        )
        client_thread.start()

        with client_locks:
            active_client.append((client_socket,client_address))

        print(active_client)
        # Display how many clients are currently active
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")


#need to work on file transfer and also need to work on the client side to send the file to the server and also need to work on the server side to receive the file from the client and also need to work on the server side to send the file to the client and also need to work on the client side to receive the file from the server and also need to work on the server side to send the file to the client and also need to work on the client side to receive the file from the server and also need to work on the server side to send the file to the client and also need to work on the client side to receive the file from the server and also need to work on the server side to send the file to the client and also need to work on the client side to receive the file from the server and also need to work on the server side to send the file to the client and also need to work on the client side to receive the file from the server and also need to work on the server side to send the file to the client and also need to work on the client side to receive


if __name__ == "__main__":
    start_server()