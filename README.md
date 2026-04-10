# 🚀 AI-Content-Studio
> **The Ultimate All-in-One AI-Generated Media Hub & Manager**

ศูนย์รวมและเครื่องมือจัดการวัตถุดิบ Content จาก AI แบบครบวงจร แยกหมวดหมู่ตามโครงการและวันที่

---

## 📁 โครงสร้างโปรเจกต์ (Project Structure)

```text
AI-Content-Studio/ (Root)
├── yt-dlp.exe              <-- เครื่องมือดาวน์โหลด
├── bin/                    <-- เครื่องมือตัดต่อ (ffmpeg)
├── youtube/
│   └── masters/            <-- เก็บวิดีโอตัวเต็ม (แชร์ร่วมกัน) 📦
├── projects/
│   ├── public_commercial/  <-- งานสร้างรายได้ 💰
│   │   └── [YYYY-MM-DD]/   <-- โฟลเดอร์วันที่
│   │       ├── youtube/    ├── images/
│   │       ├── music/      └── animations/
│   └── personal_religious/ <-- งานส่วนตัว/ศาสนา 🙏
│       └── [YYYY-MM-DD]/
│           ├── youtube/    ├── images/
│           ├── music/      └── animations/
└── AI_STUDIO_RULES.md      <-- กฎเกณฑ์กำกับ AI Assistant 🧠
```

---

## 🚀 การใช้งาน (Usage)

ใช้คำสั่งผ่าน Terminal เพื่อดาวน์โหลดและตัดคลิปอัตโนมัติ:

### 1. งานทั่วไป (Public)
```dos
download.bat "[URL]" --start [SEC] --duration [SEC] --output "clip.mp4"
```

### 2. งานส่วนตัว/ศาสนา (Private)
```dos
download.bat "[URL]" --start [SEC] --duration [SEC] --output "clip.mp4" --project personal_religious
```

*ใช้ `--last [SEC]` เพื่อตัดเอาช่วงท้ายคลิปอัตโนมัติ*

---

## 🧠 ข้อมูลสำหรับ AI Assistant
โปรเจกต์นี้ทำงานตามกฎใน [AI_STUDIO_RULES.md](AI_STUDIO_RULES.md) กรุณาอ่านและปฏิบัติตามโครงสร้างเสมอ

## 🔧 การบำรุงรักษา (Maintenance)
*   **Update yt-dlp**: `yt-dlp.exe -U`
*   **Clean Up**: ไฟล์สื่อในโฟลเดอร์วันที่ถูกละเว้นจาก Git สามารถลบได้เมื่อจบงานโดยไม่กระทบต่อ Git History
