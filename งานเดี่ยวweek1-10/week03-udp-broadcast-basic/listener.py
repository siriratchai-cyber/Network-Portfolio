# listener.py
# ทำExtra Extension A ส่งข้อความตอบกลับแบบ Unicast ไปยังผู้ส่งโดยตรง
import socket
from config import PORT, BUFFER_SIZE


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind(("", PORT)) 

print(f"[LISTENER] เปิดหูรอฟังการตะโกนที่พอร์ต {PORT}...")

try:
    while True:
       
        data, addr = sock.recvfrom(BUFFER_SIZE)
        message = data.decode()
        print(f"👂 ได้ยินข้อความจาก {addr}: {message}")

       
        if message == "DISCOVER_SERVER_BY_SIRIRAT":
            reply = "I_AM_HERE_673380060-6"
            sock.sendto(reply.encode(), addr)
            print(f"📤 ตอบกลับไปยัง {addr} เรียบร้อย")

except KeyboardInterrupt:
    print("\n[LISTENER] หยุดการทำงาน")
finally:
    sock.close()