#NoEnv
SetTitleMatchMode, 2 ; ค้นหาหน้าต่างที่มีคำบางส่วนตรงกัน

; 1. รอจนหน้าต่าง Gemini ปรากฏ (Timeout 30 วินาที)
WinWait, Gemini,, 30
if ErrorLevel {
    MsgBox, Gemini window not found!
    ExitApp
}

; 2. บังคับดึงหน้าต่างขึ้นมาด้านหน้าสุด (Force Focus)
WinActivate, Gemini
WinWaitActive, Gemini,, 5

; 3. หน่วงเวลานิดนึงให้หน้าเว็บพร้อม
Sleep, 1000

; 4. กด Paste และ Enter
Send, ^v
Sleep, 500
Send, {Enter}

ExitApp
