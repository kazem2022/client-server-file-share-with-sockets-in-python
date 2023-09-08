import socket
import os

ip = "localhost"
port = 8005



with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((ip, port))
    server.listen()
    print("server is listening ...")
    
   
    message = []
    while not message:
        client, address = server.accept() 
        print(f"client : {client} with address: {address} connected")
        
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
        break
# server.close()
