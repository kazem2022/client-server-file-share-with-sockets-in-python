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

For more information about the code, you can send me an email: k_jebraeeli@yahoo.com
