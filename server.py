import socket
import threading

# Function to handle client communication
def handle_client(client_socket, client_address):
    print(f"New connection from {client_address}")

    try:
        # Receive message from the client
        message = client_socket.recv(1024).decode('utf-8')
        print(f"Received from {client_address}: {message}")

        # Send a confirmation response back to the client
        response = f"Message received from {client_address}: {message}"
        client_socket.send(response.encode('utf-8'))

    except Exception as e:
        print(f"Error with client {client_address}: {e}")
    finally:
        # Close the connection to the client
        client_socket.close()
        print(f"Connection closed for {client_address}")

# Function to start the server and accept client connections
def start_server(host='0.0.0.0', port=9999):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print(f"Server listening on {host}:{port}...")

    while True:
        # Accept a new client connection
        client_socket, client_address = server.accept()

        # Handle the client in a new thread
        client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_handler.start()

if __name__ == "__main__":
    start_server()
