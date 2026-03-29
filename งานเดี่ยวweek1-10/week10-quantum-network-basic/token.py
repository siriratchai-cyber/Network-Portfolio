# token.py
import time

class Token:
    def __init__(self, message):
        self.message = message
        self.read = False
        self.timestamp = time.time()

    def access(self):
        # ถ้าอ่านแล้ว หรือหมดเวลา จะเข้าถึงไม่ได้อีก
        if self.read:
            return "⚠️ [COLLAPSED] ข้อความนี้ถูกอ่านไปแล้วและสลายตัวแล้ว"
        
        if time.time() - self.timestamp > 10: # TOKEN_EXPIRY
            return "⚠️ [EXPIRED] ข้อความสลายตัวตามกาลเวลา (Quantum Decoherence)"
        
        self.read = True  # เปลี่ยนสถานะทันทีที่อ่าน
        return f"🔓 [SECRET]: {self.message}"