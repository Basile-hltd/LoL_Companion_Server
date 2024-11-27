import socket

if __name__ == "__main__":
    print("===== Server Starting =====")

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.bind(("0.0.0.0", 50005))

    server_socket.listen(5)

    while True:
        client_socket, client_addr = server_socket.accept()

        data = client_socket.recv(1024).decode("ascii")
        print(data)
