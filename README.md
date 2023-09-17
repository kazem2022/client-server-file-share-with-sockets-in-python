# client-server-file-share-with-sockets-in-python
A client-server connection to file sharing with socket programming in python

code structure:
Some files are stored on the server-side, and when a client wants to download a file, the server sends a list of available files. The client then selects a file to download by typing its name.

![download](https://github.com/kazem2022/client-server-file-share-with-sockets-in-python/assets/118965194/cf1f5572-f67f-4594-855b-a3551c68566b)


In the first step, I wrote a simple socket connection between the server and client

![socket](https://github.com/kazem2022/client-server-file-share-with-sockets-in-python/assets/118965194/86daa318-bbad-4301-9636-c6dd8f65ab84)

Then I applied the concept of threading to the code.
And finally, a multi-client approach was applied, allowing each client to download the desired file
![images](https://github.com/kazem2022/client-server-file-share-with-sockets-in-python/assets/118965194/2ebf3c17-72e9-4349-9bec-9ceb3af67c36)

Not that, this approach was used for small-sized files.

![images](https://github.com/kazem2022/client-server-file-share-with-sockets-in-python/assets/118965194/3e9b7bf8-f7cd-43da-be38-8fe5391ccac8)

This code tested with localhost ip and a desired port:

![image](https://github.com/kazem2022/client-server-file-share-with-sockets-in-python/assets/118965194/55a9fec1-9b9e-4cfd-bae6-9e0ad0a022f3)

* Large file transfering approach added with buffer method

* 2-way socket file sharing added, you can transfer file from client to server and reverse.

* File source is local:


![image](https://github.com/kazem2022/client-server-file-share-with-sockets-in-python/assets/118965194/805ebdfd-a42a-4c13-9896-4c7e2373be10)

![image](https://github.com/kazem2022/client-server-file-share-with-sockets-in-python/assets/118965194/fd9bd9b3-da60-4cea-ba5a-604a266ea3d6)

In the last step, I applied a graphic user interface (GUI) using the Tkinter library in Python:
User selection page:

![welcome page](https://github.com/kazem2022/client-server-file-share-with-sockets-in-python/assets/118965194/ac94464d-6ca1-4d41-a990-04e6a8060305)

If download selected:

![download list2](https://github.com/kazem2022/client-server-file-share-with-sockets-in-python/assets/118965194/7d9cd08a-db17-4f2c-bab9-f0ec7fe314aa)


![loading bar-start](https://github.com/kazem2022/client-server-file-share-with-sockets-in-python/assets/118965194/c0d88f3b-4e08-49b6-b2a5-ceb09d420128)

By clicking download button:

![loading bar-start1](https://github.com/kazem2022/client-server-file-share-with-sockets-in-python/assets/118965194/f27096f5-9c67-4f4d-8967-bd2832b19487)

![messagebox-file-downloaded](https://github.com/kazem2022/client-server-file-share-with-sockets-in-python/assets/118965194/f021decf-dbbd-479e-84d9-13305d5d74fe)


File downloaded from the server.

** If user select upload:

![welcome upload](https://github.com/kazem2022/client-server-file-share-with-sockets-in-python/assets/118965194/f106f49b-b9f5-407b-a347-b180d51dd2e3)

![file to upload](https://github.com/kazem2022/client-server-file-share-with-sockets-in-python/assets/118965194/bf1c7ecb-7c5b-4ef1-a177-9a5f2824f89a)

![choose to upload](https://github.com/kazem2022/client-server-file-share-with-sockets-in-python/assets/118965194/20b64c4f-6223-4527-9ca6-6c18504f542b)


![uploading bar](https://github.com/kazem2022/client-server-file-share-with-sockets-in-python/assets/118965194/4a35c3dd-be99-4806-bd7b-2bb856ffd30c)

![messagebox-file-uploaded](https://github.com/kazem2022/client-server-file-share-with-sockets-in-python/assets/118965194/316da3c5-31db-4f39-93a5-6d398806e158)


For more information about the code, you can send me an email: k_jebraeeli@yahoo.com
