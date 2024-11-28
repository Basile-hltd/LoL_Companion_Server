import socket

ADRESSE_SERVER = '127.0.0.1'
PORT = 50005

if __name__ == "__main__":
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((ADRESSE_SERVER, PORT))

    message = "Shutdown"
    client_socket.sendall(message.encode('utf-8'))

    client_socket.close()
