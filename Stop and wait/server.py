import socket as sock
import time
import random as rand
HOST="localhost"
PORT=5000
#Run this file first

server_socket=sock.socket(sock.AF_INET,sock.SOCK_STREAM)
server_socket.bind((HOST,PORT))
server_socket.listen(4)
conn,addr=server_socket.accept()
prev_frame_no=-1
received_data=[]
while True :
    data=conn.recv(1024).decode()
    if not data : break
    time.sleep(rand.randint(0,5))
    data=data.split(" ")
    frame_no=int(data[1])
    conn.sendall(f"Ack: {(frame_no+1)%2}".encode())
    if(prev_frame_no!=frame_no):
        print("From client:",data[3])
        received_data.append(data[3])
        prev_frame_no = frame_no

print("Received data:","".join(received_data))
conn.close()
server_socket.close()