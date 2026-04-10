# 📜 AI STUDIO OPERATIONAL RULES (กฎเหล็กการทำงาน)

ไฟล์นี้คือกฎระเบียบสำหรับพัฒนาและรันระบบ AI Content Studio เวอร์ชัน **Hybrid (Python + AHK)**

## 🔐 กฎด้านความปลอดภัย (Stealth & Security)
- **Hybrid Automation**: ใช้ `Python` สำหรับจัดการเตรียมข้อมูลหลังบ้าน และเรียกใช้ `AutoHotkey (AHK)` เพื่อจัดการหน้าต่าง (WinActivate) และการวางข้อความ (Paste) เพื่อความแม่นยำสูงสุด
- **Profile Lockdown**: ต้องรันผ่าน Chrome Profile **"Profile 3"** เท่านั้น เพื่อแยกสภาพแวดล้อมการทำงาน
- **Gemini Centric**: ระบบปัจจุบันถูกออกแบบมาเพื่อ **Gemini (gemini.google.com)** เป็นหลัก

## ⌨️ กฎด้านการพิมพ์และนำทาง (Input & Navigation)
- **AHK Handoff**: เมื่อ Python เตรียม Clipboard เสร็จแล้ว ต้องส่งไม้ต่อให้ `stealth_paste.ahk` จัดการเสมอ ห้ามใช้ `pyautogui` พิมพ์หรือคลิกโดยตรงหากไม่จำเป็น
- **Window Title Matching**: สคริปต์ AHK ต้องค้นหาหน้าต่างที่มีคำว่า **"Gemini"** ในหัวข้อ (Title Match Mode 2)
- **2-Step Prompting**: สำหรับ Gemini ต้องแยกการส่งเป็น 2 รอบ (ส่งเนื้อหาวิเคราะห์ก่อน แล้วจึงสั่งสร้างภาพ) โดยหน่วงเวลาอย่างน้อย 60 วินาทีในขั้นตอนแรก

## 🛠️ มาตรฐานโค้ด (Code Standards)
- **UTF-8 Enforcement**: ทุกสคริปต์ต้องรองรับ UTF-8 เพื่อรองรับภาษาไทยใน Terminal และการส่ง Prompt
- **Fail-Safe**: ต้องมี `KeyboardInterrupt` (Ctrl+C) ใน Python และ `ExitApp` ใน AHK เพื่อให้มนุษย์ตัดการทำงานบอทได้ทันทีเมื่อจำเป็น

---
*กฎนี้ถูกปรับปรุงสำหรับการรัน Gemini แบบเสถียร 100% (Update: 2026-04-11)*
