# config.py
HOST = "127.0.0.1"
BASE_PORT = 7000
BUFFER_SIZE = 1024
NEIGHBORS = [7001, 7002]      # พอร์ตของ Node เพื่อนบ้าน
FORWARD_PROBABILITY = 0.5     # ทำ EXTRA: โอกาสส่งต่อ 50%
TTL = 3                       # ทำ EXTRA: จำนวนทอดสูงสุดที่จะส่งต่อ (Time-To-Live)