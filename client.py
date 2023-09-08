import socket
import os

# files_path = "./"
# data = os.listdir(files_path)



# print(data)
ip = "localhost"
port = 8005
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((ip, port))
    # client.send(b"quit")
    message = client.recv(1024).decode()
    print(message)
    message2 = client.recv(1024).decode()
    print(message2)
    file_name = input()
    request = client.sendall(file_name.encode())
    requested_file = client.recv(1024)
    # print(requested_file)
    if requested_file == b"dadash in file inja nistesh!!!":
        print(requested_file.decode()) 
    else:
        with open(f"./client-files/{file_name}", "wb") as file:
            file.write(requested_file)
        print("file downloaded from server.")
        
    # file_name = input("enter your desire file name to download")
    # with open("./client-files/new2.txt", "wb") as file:
    #     file.write(message)
    
   


    