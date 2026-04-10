# 🧘 AI Content Studio: Dharma Automation Pipeline (Gemini Edition)

ระบบอัตโนมัติสำหรับผลิตเนื้อหา "ธรรมทาน" โดยใช้พลังของ **Gemini AI** และสคริปต์ **Hybrid (Python + AutoHotkey)** ในการคุมระบบแบบ Stealth Automation

## 🚀 ฟีเจอร์หลัก (Main Features)
- **Hybrid Stealth Bot**: รวมพลัง `Python` (ประมวลผล) และ `AutoHotkey` (ควบคุมหน้าต่าง) เพื่อความแม่นยำ 100% บนหน้าเว็บ Gemini
- **Gemini Centric Workflow**: รองรับการส่ง Prompt แบบ 2 ขั้นตอน (วิเคราะห์ก่อน แล้วจึงสั่งสร้างภาพ)
- **Profile Isolation**: รันผ่าน Chrome **Profile 3** เพื่อความปลอดภัยของบัญชีหลัก
- **Video & Image Hub**: พร้อมระบบจัดการวิดีโอ YouTube และเตรียมรูปภาพ 4:5 (1080x1350)

## 🛠️ โครงสร้างโปรเจกต์ (Project Structure)
```text
ai-content-studio/
├── studio.py              # หน้าจอควบคุมภารกิจหลัก
├── youtube_queue.json     # คิวงานและสถานะการประมวลผล
├── prompt_template.md     # แม่แบบคำสั่งเพื่อให้ Gemini สร้างภาพธรรมะ
├── tools/
│   ├── bot_stealth.py     # ตัวคุมเบราเซอร์ (เปิด Gemini และเตรียม Clipboard)
│   ├── stealth_paste.ahk  # ตัวช่วยของเบราเซอร์ (คลิกวางและส่งงานแม่นๆ)
│   ├── video_handler.py   # จัดการโหลด/ตัดวิดีโอ
│   └── image_cleaner.py   # ตกแต่งรูปภาพ
└── requirements.txt       # Library ที่จำเป็น
```

## 🎮 วิธีการเริ่มต้น (Getting Started)

1. **ติดตั้ง Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **รันภารกิจ (Start Mission)**
   เปิดเบราเซอร์และส่งงานอัตโนมัติ:
   ```bash
   python tools/bot_stealth.py
   ```

3. **ตรวจสอบสถานะ**
   ดูคิวงานและจัดการวิดีโอผ่านหน้า Dashboard:
   ```bash
   python studio.py
   ```

## 🛡️ นโยบายความปลอดภัย (Stealth Strategy)
ระบบใช้เทคนิค **Hybrid Automation** เพื่อหลีกเลี่ยงการโดนแบนโดย AI ฝั่งตรงข้าม:
1. **Window-Level Control**: ใช้ AutoHotkey เจาะจงหน้าต่าง Gemini ทำให้คลิกวางและส่งผลลัพธ์แม่นยำเหนือระดับ
2. **2-Step Prompting**: หน่วงเวลาการส่ง 60 วินาทีเพื่อให้ Gemini วิเคราะห์เนื้อหาก่อนสั่งสร้างภาพ (เลียนแบบการทำบทสรุปของมนุษย์)

---
*Created with 🙏 for Dharma Sharing Automation (Gemini Hybrid Version)*
