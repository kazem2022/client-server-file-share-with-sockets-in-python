import socket
import os
import threading

ip = "localhost"
port = 8000

def client_function(client):
    
    files = os.listdir("server-files")
    files_path = "\n".join(files)
    # print(files_path)
    
    client.send(files_path.encode())
    
    with open("./server-files/a.txt", "rb") as file:
        data2 = file.read(1024)
        # client.send(data2)
        client.send("input desire file name please:\n ".encode())
        
        requested_file = client.recv(1024).decode()
        if requested_file in files:
            # print(requested_file)
            with open(f"./server-files/{requested_file}", "rb") as file:
                request_answer = client.send(file.read(1024))
        else:
            client.send(b"dadash in file inja nistesh!!!")
    # if message == "quit":
clients = []
while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((ip, port))
        server.listen(5)
        print("server is listening ...")
        client, address = server.accept() 
        print(f"client : {client} with address: {address} connected")
        clients.append(client)
        break
for client in clients:
    threading.Thread(target=client_function, args=(client,)).start()
        
    

    
# server.close()
