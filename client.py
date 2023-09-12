import socket
import os

ip = "localhost"
port = 8082
buffer_size = 8192 #Bytes = KB
def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((ip, port))
        message = client.recv(buffer_size).decode()
        print(message)
        message2 = client.recv(buffer_size).decode()
        print(message2)
        file_name = input()
        request = client.sendall(file_name.encode())
        requested_file = client.recv(buffer_size)
        if requested_file == b"File not found!":
            print(requested_file.decode()) 
        else:
            with open(f"../client-files/{file_name}", "wb") as file:
                file.write(requested_file)
            print("file downloaded from server.")
        
if __name__ == "__main__":
    main()
    
   


    