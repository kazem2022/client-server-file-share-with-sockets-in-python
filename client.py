"""Importing libraries"""
import socket
import os
from tqdm import tqdm
from tkinter import *
from tkinter import filedialog
import tkinter.ttk as pb_tk
from tkinter import messagebox
import time

ip = "localhost"
port = 8092
buffer_size = 512 #Bytes => KB

lbx_answer = []
def select_from_list(files_list):
    """This function select file from list to download."""
    Download_win = Tk()
    Download_win.geometry("400x400+40+40")
    Download_win.title("Download")
    Download_win.configure(bg="#dad7cd")

    lb3 = Label(master=Download_win, anchor=N, text="Select your file to download:",
                font=("Arial",18), bg="#3a5a40", fg="#dad7cd").pack(padx=10, pady=40)

    server_txt = Listbox(master=Download_win,selectmode=SINGLE)
    server_txt.pack()

    for file in files_list:
        server_txt.insert(END, file)

    def request():
        """This function earn user selected file name."""
        fileName = server_txt.get(ACTIVE)
        Download_win.destroy()
        lbx_answer.append(fileName)
    submit = Button(master=Download_win, text="submit", command=request).pack()

    Download_win.mainloop()

files_list = []
def receive_file():
    """This function receive data from the server."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((ip, port))
        client.send("down".encode())
        # Receive files list and print
        server_files = client.recv(buffer_size).decode()
        print(server_files)
        files = server_files.split("\n")
        for file in files:
            files_list.append(file)
        
        # ISERT FLIES TO LIST BOX
        # THEN USER SELECT ONE FILE
        select_from_list(files_list)
        file_name = lbx_answer[0]
            
        print(files_list)
        input_message = client.recv(buffer_size).decode()
        print(input_message)
        time.sleep(1)
        client.sendall(file_name.encode())
        file_size = int(client.recv(buffer_size).decode())
        requested_file = client.recv(buffer_size)
        
        # Making a progress to drawing progress-bar
        progress = tqdm(range(file_size), f"receiving {file_name}",
                        unit="B", unit_scale=False, unit_divisor=buffer_size)
        
        if requested_file == b"File not found!":
            print(requested_file.decode()) 
        else:
            # File receiving cycle
            with open(f"../client-files/{file_name}", "wb") as file:
                load = "download"
                def downloading():
                    """This function download data from the server."""
                    download = 0
                    buffer_size = 8192
                    
                    while (download<file_size):
                        data = client.recv(buffer_size)
                        file.write(data)
                        progress.update(len(data))
                        
                        bar['value']+=(buffer_size/file_size)*100
                        download+=buffer_size
                        percent.set(str(int((download/file_size)*100))+"%")
                        text.set(str(download)+"/"+str(file_size)+f"{file_name} {load} completed")
                        window.update_idletasks()
                        
                    time.sleep(1)     
                    window.destroy()
                    client.send(b"File sent!")
                window = Tk()
                window.geometry("300x130+200+200")
                window.title("Download from sever")

                percent = StringVar()
                text = StringVar()

                bar = pb_tk.Progressbar(window,orient=HORIZONTAL,length=300)
                bar.pack(pady=10)

                percentLabel = Label(window,textvariable=percent).pack()
                taskLabel = Label(window,textvariable=text).pack()
                button = Button(window,text=f"{load}",command=downloading).pack()

                window.mainloop()
                    
            print("file downloaded from server.")

def send_file(file_name):
    """This function send data to server."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((ip, port))
        print("connected to the server.")
        client.send("up".encode())
        time.sleep(1)
        # Error handling
        try:
            path = f"../client-files/{file_name}"
            file_size = os.stat(path).st_size

            client.send(str(file_size).encode())
            client.send(file_name.encode())
            
            # Make a progress to drawing progress-bar
            progress = tqdm(range(file_size), f"sendig {file_name}", unit="B",
                            unit_scale=False, unit_divisor=buffer_size)
            
            # Sending process to sending file to the server
            with open(path, "rb") as file:
                steps = int(file_size/buffer_size + 1)
                print(steps)
                # Progress bar
                load = "upload"
                def uploading():
                    """This function upload data to the server."""
                    download = 0
                    buffer_size = 8192
                    
                    while(download<file_size):
                        data = file.read(buffer_size)
                        client.send(data)
                        progress.update(len(data))
                        bar['value']+=(buffer_size/file_size)*100
                        download+=buffer_size
                        percent.set(str(int((download/file_size)*100))+"%")
                        text.set(str(download)+"/"+str(file_size)+f" {file_name} {load} completed")
                        window.update_idletasks()
                    time.sleep(1)    
                    
                    window.destroy()
                    client.send(b"File sent!")
                    print("\nFile sent!!!")
                window = Tk()
                window.title("Upload to sever")

                percent = StringVar()
                text = StringVar()

                bar = pb_tk.Progressbar(window,orient=HORIZONTAL,length=300)
                bar.pack(pady=10)

                percentLabel = Label(window,textvariable=percent).pack()
                taskLabel = Label(window,textvariable=text).pack()
                button = Button(window,text=f"{load}",command=uploading).pack()

                window.mainloop()
                
        except FileNotFoundError:
            print("File not found!")
    

ans = []
def client_answer():
    """This function receive client request, Downloading or Uploading a file."""
    window = Tk()
    window.geometry("400x400+40+40")
    window.title("Client")
    window.configure(bg="#dad7cd")

    lbl = Label(master=window, anchor=N, text="welcome",
                font=("Arial",18), bg="#3a5a40", fg="#dad7cd").pack(padx=10, pady=40)
    lb2 = Label(master=window, anchor=N,
                text="Choose Download a file from server or upload to it?",
                font=("Arial",12), bg="#3a5a40", fg="#dad7cd").pack(padx=10, pady=20)
    var = IntVar()
    def select():
        if var.get() == 1:#download selected
            ans.append(1)
        elif var.get() == 2:#upload selected
            ans.append(2)
        window.destroy()
        
    # Buttons
    submit_btn = Button(master=window, text="submit", bd =2, bg="green",
                font=("Arial Black", 12),width=10,command=select)
    submit_btn.place(x=140, y=260)

    download_btn = Radiobutton(master=window, text="download", bd =2, bg="#129490",
                font=("Arial Black", 12),variable=var, value=1)
    download_btn.pack(padx=2, pady=2)
    upload_btn = Radiobutton(master=window, text="upload", bd =2, bg="#129490",
                font=("Arial Black", 12),variable=var, value=2)
    upload_btn.pack(padx=2, pady=2)
    window.mainloop()

selected_file = []
def select_file_to_upload():
    upload_win = Tk()
    upload_win.geometry("400x400+40+40")
    upload_win.title("Upload")
    upload_win.configure(bg="#dad7cd")
    # Labels
    lb3 = Label(master=upload_win, anchor=N, text="Select your file to uplaod:",
                font=("Arial",18), bg="#3a5a40", fg="#dad7cd")
    lb3.pack(padx=10, pady=40)
    def open():
        """This function opens a directory for choosing a file from the client."""
        try:
            file_path = filedialog.askopenfile(initialdir="../client_files", title ="open")
            selected_file.append(file_path.name)
        except Exception:
            print("Select a file!")
    choose_btn = Button(master=upload_win, text="choose a file", command=open)
    choose_btn.pack()

    def send():
        print("File sent!")
        upload_win.destroy()
    send_btn = Button(master=upload_win, text="send to server", command=send)
    send_btn.pack(pady=5)

    upload_win.mainloop() 
        
def task_switcher():
    """This function is handling client request."""
    client_answer()
    if ans[0] == 1:
        receive_file()
        messagebox.showinfo("info", "File downloaded")
    elif ans[0] == 2:
        select_file_to_upload()
        path1 = selected_file[0]
        print(path1.split("/")[-1])
        fileName = path1.split("/")[-1]
        send_file(fileName)
        messagebox.showinfo("info", "File uploaded")
    
if __name__ == "__main__":
    task_switcher()
    