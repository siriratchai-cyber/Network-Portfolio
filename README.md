# 📘 Personal Portfolio  
## For CP352005 Computer Network  

**Name:** นางสาวศิริรัตน์ ชัยชนะ  
**Student ID:** 673380060-6  
**Section:** 01  

---

# 📚 Assignment

## 🔹 Personal Assignment

| Assignment | Link |
|----------|------|
| Essay about Network | https://docs.google.com/document/d/1ItjjID-W-LSwyPscqbY7Uu-ehx3-itMSd7S_pUexgag/edit?usp=sharing |
| Assignment 2 | https://docs.google.com/document/d/1w3SCjEkUexBMbOvPLaAjAfKhCqWisCXDnur8ssxVnvg/edit?usp=sharing |
| Assignment 3 | https://docs.google.com/document/d/1KiR1PDzE0_6DleW5LWMD7SlPNPhuxST1GoJgHDklkJ8/edit?usp=sharing |
| Assignment 4 | https://docs.google.com/document/d/1zKWLkZqVfRU9IsZHhQkBXyQ_wuV9Vcel80XuvjXMByw/edit?usp=sharing |

---
## 💻 Network Programming (Week 1–10)
ผลการเรียนรู้และการเขียนโปรแกรมเครือข่ายพื้นฐานงานเดี่ยว

* [คลิกเพื่อดูโฟลเดอร์งานทั้งหมด](./Personal%20Week1-10/)
* [คลิกเพื่อดูผลลัพธ์ของงานweek1-10](./Personal%20Week1-10/ผลการรันของweek1-10)
---

# 🧪 GroupLab (Week1–5)

| Lab | Description | Link |
|----|------------|------|
| Lab 1 | Complete Lab-Focused Teaching Package | https://docs.google.com/document/d/1vtYlqgI2a4dl8QZcOM_5dX60jl6MhDn5w2cXu4fyqHA/edit?usp=sharing |
| Lab 2 | VLAN Design (Router-on-a-Stick) | https://docs.google.com/document/d/1om_9G98FlEn59QgyA8rxmZpEz1ys2JRl5T8UrRHiEac/edit?usp=sharing |
| Lab 3 | MIME + Wireshark Analysis | https://docs.google.com/document/d/1nlxIK_lX2oP6NwvAXjeYUols5mv-GYe2VFN2yb5yuWk/edit?usp=sharing |
| Lab 4 | Stateful vs Stateless Network | https://docs.google.com/document/d/1KmzmrqtmaWmJNcFg0ESWmcoffmTp2RtY8NoLxUFedNE/edit?usp=sharing |
| Lab 5 | Internet Edge + WAN + Microservices | https://docs.google.com/document/d/1yV_dftiP-KKhuW3z2_VLPL1zQWvbU0OqBTiaUtjGmDU/edit?usp=sharing |

---

# 📜 Certificate
- Cisco Packet Tracer  
<img width="1999" height="1354" alt="image" src="https://github.com/user-attachments/assets/5e8258cb-0f85-48bb-ac14-a529de15683d" />
- Checkpoint Exam
<img width="1838" height="362" alt="image" src="https://github.com/user-attachments/assets/df0c6951-074c-417d-b8da-508d0a7ccf88" />


---

# 🚀 Final Project — High-Mountain Network 
https://github.com/Nattha-nan/High-Mountain-Network.git

## 📌 Project Overview
โปรเจกต์นี้เป็นการออกแบบ **เครือข่ายสำหรับพื้นที่ภูเขาสูง (High-Mountain Network)**  
ที่มีข้อจำกัดด้าน:

- การเชื่อมต่อไม่เสถียร  
- พลังงานไม่ต่อเนื่อง  
- โครงสร้างพื้นฐานจำกัด  

แนวคิดหลักของระบบคือ:

> ❝ เครือข่ายล่มได้ แต่ต้องไม่พังทั้งระบบ ❞  
(**Resilience over Speed**)

---

## 👤 My Role — Network Architect

ในฐานะ **Architect** รับผิดชอบการออกแบบระดับระบบ (System-Level Design) และกำหนดแนวทางให้ทีมพัฒนา

---

## 🧩 Responsibilities

### 🏗️ 1. Architecture Design
- ออกแบบโครงสร้างเครือข่าย 3 ชั้น:
  - Access Layer  
  - Backbone Layer (Mesh Network)  
  - Gateway Layer  
- ออกแบบให้ระบบยังทำงานได้แม้ Gateway ล่ม  

---

### 🌐 2. Topology Design (Graph Theory)
- ใช้แนวคิด **2-connected graph**
- ทุก node มี ≥ 2 paths  
- ลด Single Point of Failure  

---

### 🔢 3. Network Planning
- กำหนดจำนวน:
  - 13 nodes  
  - 5 networks  
- ออกแบบ subnet และ segmentation  
- แยก sensor network เพื่อความปลอดภัย  

---

### ⚙️ 4. System Design Strategy
- รองรับ **Delay-Tolerant Networking (DTN)**  
- วางแนวคิด QoS และ priority traffic  
- ออกแบบระบบให้รองรับ failure scenario  

---

### 📂 5. Documentation & GitHub
ไฟล์ที่ออกแบบและจัดทำ:

- `01_conceptual.pdf` → แนวคิดระบบ  
- `02_formalization.pdf` → โมเดลเชิงคณิตศาสตร์  
- `03_architecture.md` → โครงสร้างระบบ  
- `04_implementation.md` → แนวทาง implement  
- `05_deployment.pdf` → การ deploy  

---

## 📅 Development Timeline (Sprint)

### 🔹 Week 1 — Architecture Foundation
- ออกแบบ mesh topology (≥2-connected)
- กำหนด routing cost model
- วางโครงสร้าง GitHub

---

### 🔹 Week 2 — Core System Design
- ตรวจสอบ routing logic
- ออกแบบ multi-path routing
- กำหนด weight ของ cost model

---

### 🔹 Week 3 — Integration & Testing
- ตรวจสอบ architecture หลังรวมระบบ
- ทดสอบ failure scenarios
- วิเคราะห์ energy degradation

---

### 🔹 Week 4 — Final Validation
- ตรวจสอบสถาปัตยกรรมขั้นสุดท้าย
- วิเคราะห์ QoS behavior
- เตรียมระบบสำหรับ deployment

---

## 🏗️ Network Architecture

```
Access Layer  → ผู้ใช้งาน / Sensor
        ↓
Backbone Layer → Mesh Network (Core)
        ↓
Gateway Layer → Internet Access
```

✔ ระบบยังทำงานได้แม้ Gateway ล่ม  
✔ รองรับการสื่อสารภายในแบบ decentralized  

---

## 🔗 Theory Integration

| Concept | Theory | Purpose |
|--------|--------|--------|
| Multi-path | Graph Theory | เพิ่มความทนทาน |
| DTN | Delay-Tolerant Networking | รองรับ delay |
| Segmentation | OSI Layer 3 | ควบคุม traffic |
| QoS | Queuing Theory | จัด priority |

---

## 🧠 Learning Outcomes

### 🔹 Architectural Thinking
- เข้าใจการออกแบบระบบระดับใหญ่  
- คิดเรื่อง resilience มากกว่า performance  

### 🔹 Networking
- เข้าใจ topology เชิงลึก  
- ออกแบบ network ที่ไม่มี single point failure  

### 🔹 Real-world Application
- เชื่อมโยง theory → implementation  
- ทำงานร่วมกับทีมหลาย role  

---

# 🎤 Presentation Role

ในส่วนของการนำเสนอ ทำหน้าที่อธิบาย:

- แนวคิดของระบบ (Resilience over Speed)  
- ปัญหาของพื้นที่ภูเขา  
- ภาพรวม Architecture 3 Layer  

---

# ✅ Summary
Portfolio นี้แสดงถึงความสามารถในการออกแบบระบบเครือข่ายในระดับ Architecture  
ที่เน้น **Resilience, Fault Tolerance และ Real-world Constraints**  
