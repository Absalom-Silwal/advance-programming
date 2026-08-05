"""
Task 3 Using Functional programming and network programming concepts
"""

import socket

HOST = "127.0.0.1"
PORT = 65432


def process_logs(logs):
    """
    filters the log that startswith word "Error".
    """

    # Error log filter
    error_logs = list(
        filter(
            lambda log: log.startswith("ERROR"),
            logs
        )
    )


    # formats the log

    formatted_logs = list(
        map(
            lambda log: f">>> {log}",
            error_logs
        )
    )

    #sorts the log alphabetically
    sorted_logs = sorted(formatted_logs)
    return sorted_logs


def tcp_server():
    """ TCP Server for logs monitoring"""
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((HOST, PORT))
        server.listen()
        print("Server is listening...")
        print()
        connection, address = server.accept()
        print(f"Connected by {address}")
        while True:
            data = connection.recv(4096).decode()
            if len(data) < 1:
                break
            logs = data.split("\n")
            processed_logs = process_logs(logs)
            print("\n===== Processed Error Logs =====")
            if len(processed_logs):
                for log in processed_logs:
                    print(log)
            else:
                print("Errors not found")

            connection.sendall(
                "Logs processed successfully.".encode()
            )

        connection.close()
        server.close()
    except Exception as error:
        print(f"An error has occured: {error}")




def main():
    tcp_server()




if __name__ == "__main__":
    main()