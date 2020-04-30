import socket
client=socket.socket()
client.connect(('localhost',6969))     #连接服务端
msg=input(">>:").strip()
client.send(msg.encode("utf-8"))     #发送消息
data=client.recv(1024)
print("recv:",data.decode())
client.close()