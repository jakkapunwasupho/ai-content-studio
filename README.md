# 🎬 YouTube Video Cutter Project (yt-dlp & FFmpeg)

โปรเจกต์นี้ใช้สำหรับการดาวน์โหลดวิดีโอจาก YouTube ขนาดใหญ่ (Long-form) และทำการตัดเฉพาะส่วนที่ต้องการ (Clipping) โดยเน้นความแม่นยำสูงสุด (Frame Accuracy) และแก้ปัญหาเสียงไม่ตรงกับภาพ (Audio Sync)

---

## 🛠️ การตั้งค่าเริ่มต้น (Initial Setup)

เพื่อให้โปรเจกต์ทำงานได้สมบูรณ์ โปรดจัดวางไฟล์ตามโครงสร้างนี้:

1.  **เตรียมเครื่องมือ**:
    *   วาง `yt-dlp.exe` ไว้ที่ **หน้าแรก (Root)** ของโปรเจกต์
    *   วาง `ffmpeg.exe` ไว้ในโฟลเดอร์ `bin/` (ซึ่งถูกสร้างไว้ให้แล้ว)
2.  **ตั้งค่า Git**: โปรเจกต์นี้มีไฟล์ `.gitignore` เพื่อป้องกันไม่ให้ไฟล์ `.exe` และไฟล์วิดีโอถูกอัปโหลดขึ้น GitHub โดยไม่จำเป็น

---

## 📁 โครงสร้างโฟลเดอร์ (Project Structure)

```text
youtube-video-cutter/ (Root)
├── yt-dlp.exe          <-- เครื่องมือดาวน์โหลด
├── .gitignore          <-- ตั้งค่าข้ามไฟล์วิดีโอและ exe
├── bin/
│   └── ffmpeg.exe      <-- เครื่องมือตัดวิดีโอ
└── Download_YYYY-MM-DD/ <-- โฟลเดอร์ที่สร้างขึ้นใหม่ตามวันที่รันงาน
    └── clip_result.mp4
```

---

## 🚀 ขั้นตอนการทำงาน (Step-by-Step Workflow)

### 1. การเตรียมพื้นที่ทำงาน (Create Workspace)
เปิด Command Prompt (CMD) ในโฟลเดอร์โปรเจกต์ และสร้างโฟลเดอร์สำหรับงานวันนี้:
```cmd
:: คำสั่งสร้างโฟลเดอร์อัตโนมัติ (อาจขึ้นอยู่กับ Format วันที่ของเครื่อง)
mkdir "Download_%date:~-10,2%-%date:~-7,2%-%date:~-4,4%"

:: หรือสร้างเองด้วยชื่อที่ต้องการ
mkdir "Download_MyProject"
```

### 2. ดาวน์โหลดวิดีโอตัวเต็ม (Download Full Video)
รันคำสั่งที่ **Root ของโปรเจกต์** เพื่อโหลดวิดีโอเข้าไปในโฟลเดอร์ที่เตรียมไว้:
```dos
yt-dlp.exe "[YOUTUBE_URL]" -o "Download_folder_name/full_video.webm"
```
*(แนะนำให้โหลดไฟล์เต็มก่อน เพื่อป้องกันปัญหาเน็ตหลุดระหว่างตัด)*

### 3. ตัดคลิปเฉพาะช่วง (Cut & Re-encode)
ใช้ FFmpeg ตัดส่วนที่ต้องการ โดยระบุตำแหน่งไฟล์ให้ถูกต้อง:
```dos
bin\ffmpeg.exe -ss [START_SECONDS] -t [DURATION_SECONDS] -i "Download_folder_name/full_video.webm" -c:v libx264 -c:a aac -preset fast -crf 22 "Download_folder_name/[FILENAME].mp4"
```

---

### 🧠 ข้อมูลสำหรับ AI Assistant (Instruction for AI)
หากต้องการให้ AI ช่วยคำนวณและสร้างคำสั่ง โปรดแจ้งข้อมูลดังนี้:
1.  **ลิงก์ YouTube**
2.  **เวลาเริ่ม (HH:MM:SS) และเวลาจบ (HH:MM:SS)**

**กฎการคำนวณที่ AI ต้องใช้:**
*   **Start Seconds (-ss):** `(Hour * 3600) + (Minute * 60) + Second`
*   **Duration (-t):** `(End Seconds) - (Start Seconds)`
*   **Path:** ต้องใช้ `yt-dlp.exe` ที่ Root และ `bin\ffmpeg.exe` เสมอ

---

### 🧹 การทำความสะอาด (Cleanup)
เมื่อได้ไฟล์คลิป `.mp4` ที่ต้องการสำเร็จแล้ว ให้ลบไฟล์ต้นฉบับเพื่อประหยัดพื้นที่:
```dos
del "Download_folder_name\full_video.webm"
```

### 🔧 การบำรุงรักษา (Maintenance)
หากดาวน์โหลดไม่ได้ ให้ลองอัปเดตเครื่องมือด้วยคำสั่ง:
```cmd
yt-dlp.exe -U
```
