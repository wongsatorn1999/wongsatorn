import socket
import time
import cryptography
from cryptography.fernet import Fernet
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
def load_key():
    return open("key.key", "rb").read()
 
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    host = "127.0.0.1"
    port = 8002
    status_connect = s.connect_ex((host, port)) #คือการเชื่อมต่อไปที่ server ที่อยู่ 127.0.01 port 8002
    while status_connect == 0: #ถ้ามีการเชื่อมต่ออยู่ก็ทำซ้ำ ตรงนี้ยังบัคอยู่ถ้าเกิด server down ตอนกำลัง ส่งข้อมูลมันจะ error ตรง senall
        write_key()
        msg = input("Enter your messager : ").encode('utf-8') #การรับข้อมูลเป็น string แล้วให้เปลี่ยนเป็น bytes เลย
        f = Fernet( load_key())
        s.sendall(f.encrypt(msg)) #ส่งข้อมูล(msg) ไปที่ server ที่ทำการเชื่อมต่ออยู่ ถ้าการเชื่อมต่อหายจะ error ตรงนี้ 555 เพราะไม่มี server จะให้ส่งข้อมูล ต้องใส่ try catch  ไว้
        print("client recv : ",f.decrypt(s.recv(300)).decode('utf-8')) #ทำการรับข้อมูลจาก server ขนาดไม่เกิน 300 bytes และถอดรหัสจาก bytes เป็น string และทำการถอดรหัสด้วยฟังก์ชั่น Fernet จาก key ที่มีอยู่
        time.sleep(1)
