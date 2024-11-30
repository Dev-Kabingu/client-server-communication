import socket

# Function to send a message to the server and receive a response
def send_message_to_server(server_ip='127.0.0.1', server_port=9999):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to the server
        client.connect((server_ip, server_port))

        # Prompt the user to enter a message
        message = input("Enter a message to send to the server: ")

        # Send the message to the server
        client.send(message.encode('utf-8'))

        # Receive the server's response
        response = client.recv(1024).decode('utf-8')
        print(f"Received from server: {response}")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the connection to the server
        client.close()

if __name__ == "__main__":
    send_message_to_server()
