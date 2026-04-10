# 🧘 AI Content Studio: Dharma Automation Pipeline

ระบบอัตโนมัติสำหรับผลิตเนื้อหา "ธรรมทาน" โดยใช้พลังของ AI (ChatGPT/Gemini) และสคริปต์ Python ในการคุมระบบแบบ Stealth Automation

## 🚀 ฟีเจอร์หลัก (Main Features)
- **Mission Control Dashboard**: หน้าจอควบคุมกลาง (`studio.py`) สำหรับจัดการคิวงาน
- **Stealth Bot**: บอทอัจฉริยะ (`tools/bot_stealth.py`) ที่เลียนแบบพฤติกรรมมนุษย์ในการส่ง Prompt และจัดการรูปภาพผ่านเบราเซอร์
- **Video Handler**: ระบบดาวน์โหลดและตัดคลิป Highlight อัตโนมัติจาก YouTube
- **Image Cleaning Lab**: ระบบตกแต่งรูปภาพ ตัดลายน้ำ และปรับขนาดเป็น 4:5 (1080x1350) สำหรับโซเชียลมีเดีย
- **Prompt Templating**: ระบบแยกชุดคำสั่งไว้ใน `prompt_template.md` เพื่อให้ง่ายต่อการปรับแต่งเนื้อหา

## 🛠️ โครงสร้างโปรเจกต์ (Project Structure)
```text
ai-content-studio/
├── studio.py              # หน้าจอหลัก (Mission Control)
├── prompt_template.md     # แม่แบบคำสั่งชุดใหญ่สำหรับ AI
├── youtube_queue.json     # คิวงานและสถานะวิดีโอ 100+ รายการ
├── tools/
│   ├── bot_stealth.py     # บอทคุม Chrome (ChatGPT/Gemini)
│   ├── video_handler.py   # จัดการโหลด/ตัดวิดีโอ
│   └── image_cleaner.py   # จัดการตกแต่งรูปภาพ
└── requirements.txt       # Library ที่จำเป็น (Pillow, PyAutoGUI, etc.)
```

## 🎮 วิธีการเริ่มต้น (Getting Started)

### 1. ติดตั้ง Library
```bash
pip install -r requirements.txt
```

### 2. ตั้งค่าคิวงาน
แก้ไขไฟล์ `youtube_queue.json` เพื่อเพิ่มลิงก์ YouTube ที่ต้องการประมวลผล

### 3. รันภารกิจ (Start Mission)
รันบอทเพื่อส่ง Prompt ไปยัง AI:
```bash
python tools/bot_stealth.py
```

### 4. ตรวจสอบ Dashboard
รันหน้าจัดการหลักเพื่อดูสถานะงานทั้งหมด:
```bash
python studio.py
```

## 🛡️ นโยบายความปลอดภัย (Stealth Strategy)
ระบบนี้ถูกออกแบบมาเพื่อ **หลีกเลี่ยงการโดนแบน** โดยใช้เทคนิค:
1. **OS-Level Automation**: ไม่มีการฉีดโค้ดเข้าเบราเซอร์ ทำงานผ่านสัญญาณคีย์บอร์ดจริง
2. **Browser Profile Isolation**: ใช้โปรไฟล์ Chrome แยกเฉพาะ (panagon) เพื่อความปลอดภัยของบัญชีหลัก
3. **Behavior Simulation**: มีการหน่วงเวลา และใช้การก๊อปปี้วางที่เป็นธรรมชาติ

---
*Created with 🙏 for Dharma Sharing Automation*
