import socket
import time
 
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #สร้าง socket ด้วย TCP/IP
 
# Bind the socket to the port
server_address = ('localhost', 8002) #กำหนดที่อยู่ server และ port ไว้ที่ตัวแปร server_address
print('starting up on %s port %s' % server_address)
sock.bind(server_address) #ผูก socket ไว้กับ server , port
sock.listen(1) #รับการเชื่อมต่อสูงสุดแค่ 1 connect
 
while True:
    connection, client_address = sock.accept() #รอรับข้อมูลที่ส่งมาจาก client ทั้งข้อมูล และ ที่อยู่
    server_wait = True
    try:
        while server_wait:
            try:
                data = connection.recv(300) #รับข้อมูลไม่เกิน 300 bytes จาก client ยิ่งตัวเลขมากเท่าไรข้อมูลที่รับได้ก็มากขึ้นตาม
                if not data: server_wait = False #ถ้าไม่มีข้อมูลก็ออก loop ไม่ต้องส่งข้อมูลกลับไปยัง client
                print('Server Recv and Send back : ',data.decode("utf-8")) #รับข้อมูลมาและถอดรหัสด้วยการเข้ารหัสแบบ utf-8
                connection.sendall(data) #ส่งข้อมูลที่ได้รับกลับไปยัง client ที่ทำการเชื่อมต่อเข้ามา
            except :
                server_wait = False
 
    finally:
        # Clean up the connection
        connection.close() #ปิดการเชื่อมต่อ
 
