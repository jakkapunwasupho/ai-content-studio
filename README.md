# 🚀 AI-Content-Studio
> **The Ultimate All-in-One AI-Generated Media Hub & Manager**

ศูนย์รวมและเครื่องมือจัดการวัตถุดิบ Content จาก AI แบบครบวงจร (YouTube, Images, Music, Animations)

---

## 🛠️ การตั้งค่าเริ่มต้น (Initial Setup)

1.  **เตรียมเครื่องมือ**:
    *   วาง `yt-dlp.exe` ไว้ที่ **หน้าแรก (Root)** ของโปรเจกต์
    *   วาง `ffmpeg.exe` ไว้ในโฟลเดอร์ `bin/` (มีให้แล้ว)
2.  **จัดการไฟล์**: นำไฟล์สื่อที่ได้จาก AI หรือดาวน์โหลดมา วางลงในโฟลเดอร์หมวดหมู่ที่เตรียมไว้ให้แล้ว

---

## 📁 โครงสร้างโปรเจกต์ (Project Structure)

```text
AI-Content-Studio/ (Root)
├── yt-dlp.exe      <-- เครื่องมือดาวน์โหลด
├── bin/            <-- เครื่องมือตัดต่อ (ffmpeg)
├── youtube/        <-- เก็บวิดีโอจาก YouTube 🎥
├── images/         <-- เก็บรูปจาก AI (Gemini, Grok) 🖼️
├── animations/     <-- เก็บวิดีโอ AI (Runway, Luma) 🎬
└── music/          <-- เก็บเพลง AI (Suno, Udio) 🎵
```

---

## 🚀 ขั้นตอนการทำงาน (Workflow)

### 1. จัดเก็บสื่อ
ลากไฟล์ที่ได้จาก AI มาวางในโฟลเดอร์ตามหมวดหมู่ได้ทันที (Git จะมองข้ามไฟล์เหล่านี้โดยอัตโนมัติ)

### 2. ตัดวิดีโอ YouTube
รันคำสั่งโดยระบุตำแหน่งโฟลเดอร์โครงการ:
```dos
:: โครงการปกติ (Public/Commercial)
download.bat "[URL]" --start [SEC] --duration [SEC] --output "result.mp4"

:: โครงการส่วนตัว (Personal/Religious)
download.bat "[URL]" --start [SEC] --duration [SEC] --output "result.mp4" --project personal_religious
```
*   **--project**: เลือกได้ระหว่าง `public_commercial` (ค่าเริ่มต้น) หรือ `personal_religious`
*   **Storage**: 
    - `projects/public_commercial/` -> สำหรับงานสร้างรายได้
    - `projects/personal_religious/` -> สำหรับงานส่วนตัว/ศาสนา

---

### 🧠 ข้อมูลสำหรับ AI Assistant (Instruction for AI)
หากต้องการให้ AI ช่วย:
- **YouTube**: บอก URL และเวลาเริ่ม/จบ (AI จะสร้างคำสั่งให้)
- **Organization**: บอกประเภทไฟล์ AI จะแนะนำโฟลเดอร์ที่ถูกต้องให้

---

### 🔧 การบำรุงรักษา (Maintenance)
*   **Update yt-dlp**: `yt-dlp.exe -U`
*   **Clean Up**: โฟลเดอร์เหล่านี้จะถูกละเว้นจาก Git คุณสามารถลบไฟล์ข้างในได้ทุกเมื่อโดยไม่กระทบต่อ Git History
