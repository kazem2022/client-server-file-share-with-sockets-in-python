import socket
import os
import threading

ip = "127.0.0.1"
port = 8082
buffer_size = 8192 #Bytes = 8KB

def client_function(client):
    
    files = os.listdir("../server-files")
    files_path = "\n".join(files)
    
    client.send(files_path.encode())
    
    # with open("../server-files/a.txt", "rb") as file:
    #     data2 = file.read(4072)
    client.send("\nPlease input the desired file name:\n ".encode())
    
    requested_file = client.recv(buffer_size).decode()
    try:
        with open(f"../server-files/{requested_file}", "rb") as file:
            request_answer = client.send(file.read(buffer_size))
        print(request_answer)
    except FileNotFoundError:
        client.send(b"File not found!")
# clients = []
while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((ip, port))
        server.listen(5)
        print(f"server is listening on address:{ip,port}...")
        
        client, address = server.accept() 
        print(f"client with address: {address} connected")
        # print("client:", client)
        # clients.append(client)
        client_thread = threading.Thread(target=client_function, args=(client,))
        client_thread.start()
    