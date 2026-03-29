📖 Guide: How to Run Network Labs (Week 1 - 10)
Student Name: Sirirat Chaichana
Student ID: 673380060-6
Sec: 1

คู่มือนี้จะอธิบายวิธีการรันโปรแกรมในแต่ละสัปดาห์อย่างสรุป เพื่อความรวดเร็วในการตรวจสอบผลลัพธ์

🛠 Preparation (สิ่งที่ต้องทำก่อนรัน)
ติดตั้ง Python 3.x 
เปิด VS Code และใช้ฟีเจอร์ Split Terminal (เปิดหลายจอพร้อมกัน) เพื่อจำลองโหนดต่าง ๆ ในเครือข่าย

🚀 Execution Steps (ขั้นตอนการรันรายสัปดาห์)
🔵 Phase 1: Basic Unicast & Broadcast (W1 - W3) เน้นการคุยกันตรง ๆ หรือตะโกนหาทุกคน
Week 1-2 (TCP/UDP): รัน server.py ก่อน แล้วจึงรัน client.py
Week 3 (Broadcast): รัน receiver.py หลาย ๆ จอ แล้วรัน sender.py เพื่อส่งข้อความหาทุกคนพร้อมกัน

🟢 Phase 2: Group & Peer Communication (W4 - W5)
Week 4 (Multicast): 1. รัน receiver.py (เพื่อ Join Group)
2. รัน sender.py เพื่อส่งข้อมูลเข้ากลุ่ม 224.1.1.1

Week 5 (P2P): 1. จอที่ 1: python peer.py 1
2. จอที่ 2: python peer.py 2
3. พิมพ์ ID เพื่อนเพื่อคุยโต้ตอบกัน

🟡 Phase 3: Ad-Hoc & Routing (W6 - W9)
เน้นการส่งต่อข้อมูล (Forwarding) และการตัดสินใจ

Week 6 (Ad-Hoc/MANET):
รัน 3 จอ: python node.py 0, python node.py 1, python node.py 2
ส่งจากโหนด 0 ข้อมูลจะไหลผ่านโหนด 1 ไปยังโหนด 2 เอง

Week 7 (Store-and-Forward):
รันโหนดรับ: python node.py 2
ปิดโหนดรับ แล้วรันโหนดส่งเพื่อฝากข้อความไว้ใน Queue
เปิดโหนดรับอีกครั้ง ข้อความที่ฝากไว้จะถูกส่งตามไปอัตโนมัติ

Week 8 (Opportunistic):
รันหลายโหนดพร้อมกัน สังเกตตาราง Probability ถ้าค่าสูงเกินเกณฑ์ ข้อความถึงจะถูกส่งออกไป

Week 9 (Bio-Inspired):
รันหลายโหนด ส่งข้อความบ่อย ๆ เพื่อเพิ่มค่า Pheromone สังเกตการเลือกเส้นทางที่ฟีโรโมนสูงสุด

🔴 Phase 4: Quantum-Inspired (W10)
เน้นความปลอดภัยและการสลายตัวของข้อมูล

รัน python node.py 1 และ python node.py 2

เมนู [1]: ส่งข้อความลับ

เมนู [2]: เช็คตู้จดหมาย

เมนู [3]: อ่านข้อความ (ข้อความจะสลายตัวทันทีหลังอ่านครั้งแรก หรือหมดเวลา 10 วินาที)

⚠️ Troubleshooting (ปัญหาที่พบบ่อย)
Error: Address already in use: ให้รอประมาณ 10-30 วินาทีก่อนรันใหม่ หรือเปลี่ยน Port ใน config.py

ValueError ใน Week 7/8: อย่ากด Enter ว่างในช่องใส่พอร์ต ให้พิมพ์ตัวเลขพอร์ตให้ชัดเจน

Firewall Block: หากรันข้ามเครื่อง ให้ตรวจสอบว่า Firewall ยอมรับ Python หรือไม่


7-10	Adv. Routing	8000-11000	node.py
