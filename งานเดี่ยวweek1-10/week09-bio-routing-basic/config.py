# config.py

HOST = "127.0.0.1"
BASE_PORT = 10000
PEER_PORTS = [10001, 10002]
BUFFER_SIZE = 1024
INITIAL_PHEROMONE = 1.0
DECAY_FACTOR = 0.9      #  ฟีโรโมนจางลง 10% ทุกรอบ (Extra: Step 0)
REINFORCEMENT = 0.5     #  เพิ่มฟีโรโมน 0.5 เมื่อส่งสำเร็จ
UPDATE_INTERVAL = 5     # วินาทีในการ Decay