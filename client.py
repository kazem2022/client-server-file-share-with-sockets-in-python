import socket
import os
from tqdm import tqdm

ip = "localhost"
port = 8086
buffer_size = 512 #Bytes => KB

def receive_file():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((ip, port))
        
        client.send("down".encode())
        
        message = client.recv(buffer_size).decode()
        print(message)
        message2 = client.recv(buffer_size).decode()
        print(message2)
        file_name = input()
        request = client.sendall(file_name.encode())
        file_size = int(client.recv(buffer_size).decode())
        # print("file_size:", file_size)
        requested_file = client.recv(buffer_size)
        progress = tqdm(range(file_size), f"receiving {file_name}", unit="B", unit_scale=True, unit_divisor=buffer_size)
        if requested_file == b"File not found!":
            print(requested_file.decode()) 
        else:
            with open(f"../client-files/{file_name}", "wb") as file:
                while True:
                    data = client.recv(buffer_size)
                    if data == b"file sent!":
                        print("***************")
                        break
                    file.write(data)
                    progress.update(len(data))
                                         
            print("file downloaded from server.")

def send_file():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((ip, port))
        print("connected to the server.")
        client.send("up".encode())
        files = os.listdir("../client-files")
        files_path = "\n".join(files)
        print(files_path)
        file_name = input("select your desire file...\n")
                   
        try:
            path = f"../client-files/{file_name}"
            file_size = os.stat(path).st_size
            client.send(str(file_size).encode())
            client.send(file_name.encode())
            progress = tqdm(range(file_size), f"sendig {file_name}", unit="B", unit_scale=True, unit_divisor=buffer_size)
            
            with open(path, "rb") as file:
                steps = int(file_size/buffer_size + 1)
                for step in range(steps):
                    data = file.read(buffer_size)
                    client.send(data)
                    progress.update(len(data))
                client.send(b"file sent!")
                print("file sent!!!")
                
        except FileNotFoundError:
            print("File not found!")

        
        
        
        
        
        
        
        
        
        
def loader():
    answer = input("do you wanna upload a file or download from server?        up/down :  ")
    if answer.lower() == "up":
        send_file()
    elif answer.lower() == "down":
        receive_file()
    else:
        print("type your response is incorrect!!")
        

if __name__ == "__main__":
    loader()
    
   


    