import socket

ADRESSE_SERVER = "195.15.222.34"
PORT = 5010

if __name__ == "__main__":
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((ADRESSE_SERVER, PORT))

    print("===== Server Starting =====")

    server_socket.listen(5)

    while True:
        print()
        print("Attente de client...")
        client_socket, client_addr = server_socket.accept()
        print("Client Accepté :", client_addr[0])

        data = client_socket.recv(1024).decode("utf-8")
        print("Message du client :", data)

        client_socket.close()

        if data == 'Shutdown':
            break

    print()
    print("===== Server Closing =====")
    server_socket.close()
