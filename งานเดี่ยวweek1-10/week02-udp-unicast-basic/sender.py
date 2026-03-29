# sender.py
import socket
from config import HOST, PORT

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
seq_count = 1  # ส่วนที่เพิ่มจาก EXTRA: ตัวนับลำดับข้อความ

print("UDP Sender (พิมพ์ 'exit' เพื่อปิด)")
while True:
    user_input = input(f"ป้อนข้อความสำหรับลำดับที่ {seq_count}: ")
    
    #ส่วนที่เพิ่มจาก EXTRA: รวมเลขลำดับเข้าไปใน Data Payload
    full_payload = f"{seq_count}|{user_input}"
    
    # ส่งไปยังปลายทางโดยตรง 
    sock.sendto(full_payload.encode(), (HOST, PORT))
    
    if user_input.lower() == 'exit': break
    seq_count += 1  

sock.close()