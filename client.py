"""Importing library"""
import socket
import os
from tqdm import tqdm

ip = "localhost"
port = 8092
buffer_size = 512 #Bytes => KB

def receive_file():
    """This function receive data from server"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((ip, port))
        client.send("down".encode())
        # Receive files list and print
        message = client.recv(buffer_size).decode()
        print(message)
        message2 = client.recv(buffer_size).decode()
        print(message2)
        file_name = input()
        client.sendall(file_name.encode())
        file_size = int(client.recv(buffer_size).decode())
        requested_file = client.recv(buffer_size)
        
        # Make a progress to drawing progress-bar
        progress = tqdm(range(file_size), f"receiving {file_name}",
                        unit="B", unit_scale=True, unit_divisor=buffer_size)
        
        if requested_file == b"File not found!":
            print(requested_file.decode()) 
        else:
            # File receiving cycle
            with open(f"../client-files/{file_name}", "wb") as file:
                while True:
                    data = client.recv(buffer_size)
                    if data == b"File sent!":
                        print("***************")
                        break
                    file.write(data)
                    progress.update(len(data))
                    
            print("file downloaded from server.")


def send_file():
    """This function send data to server"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((ip, port))
        print("connected to the server.")
        client.send("up".encode())
        # Showing client file list
        files = os.listdir("../client-files")
        files_path = "\n".join(files)
        print(files_path)
        file_name = input("select your desire file...\n")
        
        # Error handling
        try:
            path = f"../client-files/{file_name}"
            file_size = os.stat(path).st_size
            client.send(str(file_size).encode())
            client.send(file_name.encode())
            
            # Make a progress to drawing progress-bar
            progress = tqdm(range(file_size), f"sendig {file_name}", unit="B",
                            unit_scale=True, unit_divisor=buffer_size)
            
            # Sending process to sending file to the server
            with open(path, "rb") as file:
                steps = int(file_size/buffer_size + 1)
                for step in range(steps):
                    data = file.read(buffer_size)
                    client.send(data)
                    progress.update(len(data))
                client.send(b"File sent!")
                print("File sent!!!")
                
        except FileNotFoundError:
            print("File not found!")

        
def loader():
    """This function is handling client works"""
    answer = input("Do you want to upload a file or download it from the server?\n        up / down :  ")
    if answer.lower() == "up":
        send_file()
    elif answer.lower() == "down":
        receive_file()
    else:
        print("Type your response is incorrect!!")
if __name__ == "__main__":
    loader()



    