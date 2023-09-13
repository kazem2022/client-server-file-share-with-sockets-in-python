import socket
import os
import threading
from tqdm import tqdm

ip = "127.0.0.1"
port = 8086
buffer_size = 512 #Bytes => KB

def send_file(client):
    
    files = os.listdir("../server-files")
    files_path = "\n".join(files)
    client.send(files_path.encode())
    client.send("\nPlease input the desired file name:\n ".encode())
    
    requested_file = client.recv(buffer_size).decode()
    try:
        file_path = f"../server-files/{requested_file}"
        file_size = os.stat(file_path).st_size
        client.send(str(file_size).encode())
        progress = tqdm(range(file_size), f"sendig {requested_file}", unit="B", unit_scale=True, unit_divisor=buffer_size)
        
        with open(file_path, "rb") as file:
            steps = int(file_size/buffer_size + 1)
            for step in range(steps):
                data = file.read(buffer_size)
                client.send(data)
                progress.update(len(data))
            client.send(b"file sent!")
            print("file sent!!!")
            
    except FileNotFoundError:
        client.send(b"File not found!")


def receive_file(client):
   
    file_size = int(client.recv(buffer_size).decode())
    print("file_size:", file_size)
    file_name = client.recv(buffer_size).decode()
    
    progress = tqdm(range(file_size), f"receiving {file_name}", unit="B", unit_scale=True, unit_divisor=buffer_size)
    
    with open(f"../server-files/{file_name}", "wb") as file:
        while True:
            data = client.recv(buffer_size)
            if data == b"file sent!":
                print("***************")
                break
            file.write(data)
            progress.update(len(data))
                                    
    print("file downloaded from server.") 



while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((ip, port))
        server.listen(5)
        print(f"server is listening on address:{ip,port}...")
        
        client, address = server.accept() 
        print(f"client with address: {address} connected")
        
        answer = client.recv(buffer_size).decode()
        if answer == "up":
            client_thread = threading.Thread(target=receive_file, args=(client,))
            client_thread.start()
        if answer == "down":
            client_thread = threading.Thread(target=send_file, args=(client,))
            client_thread.start()
    