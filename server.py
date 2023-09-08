import socket
import os
import threading

ip = "localhost"
port = 8092

def client_function(client):
    
    files = os.listdir("server-files")
    files_path = "\n".join(files)
    
    client.send(files_path.encode())
    
    with open("./server-files/a.txt", "rb") as file:
        data2 = file.read(1024)
        client.send("\nPlease input the desired file name:\n ".encode())
        
        requested_file = client.recv(1024).decode()
        if requested_file in files:
            with open(f"./server-files/{requested_file}", "rb") as file:
                request_answer = client.send(file.read(1024))
        else:
            client.send(b"File not found!")
clients = []
while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((ip, port))
        server.listen(5)
        print(f"server is listening on address:{ip,port}...")
        client, address = server.accept() 
        print(f"client with address: {address} connected")
        clients.append(client)
        threading.Thread(target=client_function, args=(client,)).start()
       