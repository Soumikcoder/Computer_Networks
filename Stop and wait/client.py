import socket as sock

HOST="localhost"
PORT=5000

client_server=sock.socket(sock.AF_INET,sock.SOCK_STREAM)
client_server.connect((HOST,PORT))

data=input("Enter some Data:")
data=list(data)
i=0
while i != len(data):
    send_data=f"frame: {i&1} Data: {data[i]} "
    print(f"Send: {send_data}")
    client_server.sendall(send_data.encode())
    try:
        client_server.settimeout(3)
        server_data=client_server.recv(1024).decode()
        print(f"Received: {server_data}")
        ack_no=int(server_data.split(" ")[1])
        if i&1 != ack_no:
            i+=1
    except:
        print("Dropped")
client_server.close()

