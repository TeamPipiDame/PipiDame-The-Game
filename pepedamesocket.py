import socket
import sys

host =''
port = 1883
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((host, port))
except socket.error as e:
    print(str(e))

s.listen(5)
print('waiting for a connection')

def treaded_client(conn):
    conn.send(str.encode('Welcome,type your info\n'))

    while True:
        data = conn.recv(2048)
        reply = 'sever output: '+data.decode('utf-8')
        if not data:
            break
        con.sendall(str.encode(reply))
        conn.close

    while True:
         
            conn, addr = s.accept()
            print('connected to: '+addr[0]+':'+str(addr))

            start_new_tread(Tread_client,(conn,))
            
        
