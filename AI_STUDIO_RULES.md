# 📜 AI STUDIO OPERATIONAL RULES (กฎเหล็กการทำงาน)

ไฟล์นี้คือกฎระเบียบสำหรับพัฒนาและรันระบบ AI Content Studio เพื่อรักษาความปลอดภัยและความแม่นยำ

## 🔐 กฎด้านความปลอดภัย (Stealth & Security)
- **ห้ามเปลี่ยนวิธีคุมเบราเซอร์**: ต้องใช้ `PyAutoGUI` (OS-Level) เท่านั้น ห้ามใช้ Selenium หรือ Playwright เด็ดขาดเพื่อป้องกันการโดน AI ฝั่งตรงข้ามตรวจพบ (Anti-Bot Detection).
- **Profile Lockdown**: ต้องรันผ่าน Chrome Profile **"panagon"** (`Profile 1`) เท่านั้น ห้ามรันผ่านโปรไฟล์ส่วนตัว.
- **Human-Like Delay**: ห้ามตัดเวลา `time.sleep()` ออกจนเหลือศูนย์ ต้องรักษาความเร็วในการพิมพ์และคลิกให้เหมือนมนุษย์.

## ⌨️ กฎด้านการพิมพ์และนำทาง (Input & Navigation)
- **No Direct Typing**: ห้ามใช้ `pyautogui.write` สำหรับภาษาไทยหรือ URL ยาวๆ ให้ใช้การ **Copy-Paste (Ctrl+V)** เสมอเพื่อความแม่นยำ.
- **Address Bar Navigation**: การเข้าเว็บใหม่ต้องทำผ่าน Address Bar (`Ctrl+L`) เสมอ ไม่ใช้การคลิกเมนูสุ่มเสี่ยง.
- **Snap to Right**: เบราเซอร์งานต้องถูก Snap ไปที่ **ฝั่งขวาของหน้าจอ (3440x1440px)** เสมอ.

## 🛠️ มาตรฐานโค้ด (Code Standards)
- **UTF-8 Enforcement**: ทุกสคริปต์ต้องมีการบังคับ `sys.stdout.reconfigure(encoding='utf-8')` เพื่อรองรับภาษาไทยใน Terminal.
- **Modular Tools**: โค้ดใหม่ต้องแยกเป็นไฟล์ย่อยในโฟลเดอร์ `tools/` ไม่นำมาปนกับ `studio.py`.
- **Fail-Safe**: ต้องมี `KeyboardInterrupt` (Ctrl+C) ที่ทำงานได้ตลอดเวลาเพื่อให้มนุษย์ตัดการทำงานบอทได้ทันที.

---
*กฎนี้ถูกตั้งขึ้นเพื่อความยั่งยืนของบัญชีและประสิทธิภาพของสตูดิโอ*
