import socket
server=socket.socket()
server.bind(('localhost',6969))     #绑定要监听端口
server.listen()   #监听
conn,addr=server.accept()     #等电话打进来
print(conn,addr)
data=server.recv(1024)
print("recv:",data)
conn.send(data.upper())
server.close()