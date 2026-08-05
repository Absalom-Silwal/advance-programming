
import socket

HOST = "127.0.0.1"
PORT = 65432

def client_logs():
    return [
        "INFO: User login successful",
        "ERROR: Database connection failed",
        "WARNING: Low disk space",
        "INFO: Daily backup completed",
        "ERROR: Authentication failed",
        "ERROR: File not found"
    ]

def client_logs_test_case_1():
    return [
        "INFO: User login successful",
        "WARNING: Low disk space",
        "INFO: Daily backup completed",
    ]

def tcp_client():
    """ client Application """
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((HOST, PORT))
        logs = client_logs()
        message = "\n".join(logs)
        client.sendall(message.encode())
        response = client.recv(1024).decode()
        print(response)

        """ ----------------- test cases -----------------------"""
        logs = client_logs_test_case_1()
        message = "\n".join(logs)
        client.sendall(message.encode())
        response = client.recv(1024).decode()
        print(response)

        client.close()
    except Exception as e:
        print(f"An error has occured:{e}")

def main():
    tcp_client()


if __name__ == "__main__":
    main()