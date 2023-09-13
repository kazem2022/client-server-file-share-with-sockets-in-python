import socket
import os
from tqdm import tqdm

ip = "localhost"
port = 8086
buffer_size = 512 #Bytes => KB





def receive_file():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((ip, port))
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
    pass
        
def loader():
    answer = input("do you wanna upload a file or download from server?        up/down :  ")
    if answer.lower() == "up":
        send_file()
    if answer.lower() == "down":
        receive_file()

if __name__ == "__main__":
    loader()
    
   


    