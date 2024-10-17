import socket
import hashlib

def extract_and_md5_hash(received_string):
    # Find the substring between the quotes
    start_index = received_string.find("'")
    end_index = received_string.rfind("'")

    if start_index == -1 or end_index == -1:
        return "Error: Could not find text between quotes"

    # Extract the text between quotes
    text_to_hash = received_string[start_index + 1:end_index]
    print(f"Extracted text: {text_to_hash}")

    # Compute the MD5 hash of the extracted text
    md5_hash = hashlib.md5(text_to_hash.encode()).hexdigest()
    return md5_hash

def connect_to_nc_server_and_process(host, port):
    try:
        # Create a socket object
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect to the Netcat server
        client_socket.connect((host, port))

        # Receive data from the server
        received_data = client_socket.recv(1024).decode()  # Receiving and decoding the data

        # Process the received data to extract and hash the text
        md5_hash_result = extract_and_md5_hash(received_data)
        client_socket.send(md5_hash_result).encode()
        client_socket.send("\n").encode

        client_socket.recv(1024).decode()
        client_socket.recv(1024).decode()
        client_socket.recv(1024).decode()
        client_socket.recv(1024).decode()



        # Close the connection
        client_socket.close()
        print("Connection closed.")

    except Exception as e:
        print(f"Error: {e}")

# Example usage
host = "saturn.picoctf.net"  # Replace with the actual host
port = 49515                 # Replace with the actual port

# Connect to the Netcat server and process the received data
connect_to_nc_server_and_process(host, port)
