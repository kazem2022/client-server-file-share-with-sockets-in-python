import socket
import os
import threading

ip = "127.0.0.1"
port = 8086

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
        file_path = f"../server-files/{requested_file}"
        with open(file_path, "rb") as file:
            file_size = os.stat(file_path).st_size
            steps = int(file_size/buffer_size + 1)
            # print(steps)
            for step in range(steps):
                data = file.read(buffer_size)
                # while data:    
                client.send(data)
                # data = file.read(buffer_size)
                # print(step)
            client.send(b"file sent!")
            print("file sent!!!")
            
            
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
    