import socket

ADRESSE_SERVER = "0.0.0.0"
PORT = 5010

if __name__ == "__main__":
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((ADRESSE_SERVER, PORT))

    print("===== Server Starting =====")

    server_socket.listen(5)

    index_file = open("index.html", 'rb')
    index_file = index_file.read()

    while True:
        print()
        print("Attente de client...")
        client_socket, client_addr = server_socket.accept()
        client_socket.settimeout(5)
        print("Client Accepté :", client_addr[0])

        data = client_socket.recv(1024).decode("utf-8")

        response = (
                       "HTTP/1.1 200 OK\r\n"
                       "Content-Type: text/html\r\n"
                       "Connection: close\r\n"
                       "\r\n"
                   ).encode() + index_file

        # Send the response
        client_socket.sendall(response)

        client_socket.close()


    print('')
    print("===== Server Closing =====")
    server_socket.close()
