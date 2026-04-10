import pyautogui
import time
import subprocess
import os
import json
import pyperclip
import sys

# บังคับให้ใช้ UTF-8
sys.stdout.reconfigure(encoding='utf-8')

# --- CONFIGURATION ---
CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
CHROME_PROFILE = "Profile 1" 
CHAT_URL = "https://chatgpt.com"

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
QUEUE_FILE = os.path.join(ROOT_DIR, "youtube_queue.json")
PROMPT_FILE = os.path.join(ROOT_DIR, "prompt_template.md")

def get_latest_task():
    try:
        with open(QUEUE_FILE, "r", encoding="utf-8") as f:
            queue = json.load(f)
            return next((item for item in queue if item["status"] == "pending"), queue[0])
    except: return None

def run_mission():
    task = get_latest_task()
    if not task: return

    with open(PROMPT_FILE, "r", encoding="utf-8") as f:
        template = f.read()

    print(f"Mission: {task['title']}")
    
    # 1. เปิด Chrome เปล่า
    subprocess.Popen(f'"{CHROME_PATH}" --profile-directory="{CHROME_PROFILE}" about:blank', shell=True)
    time.sleep(5)
    
    # 2. ชิดขวา
    pyautogui.hotkey('win', 'right')
    time.sleep(1)
    pyautogui.press('esc')
    time.sleep(1)

    # 3. เข้า ChatGPT ผ่าน Address Bar (ใช้ Copy-Paste เพื่อกันภาษาไทย)
    pyautogui.hotkey('ctrl', 'l')
    time.sleep(1)
    pyperclip.copy(CHAT_URL)
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.5)
    pyautogui.press('enter')
    
    # รอโหลด 20 วินาที (ชัวร์ไว้ก่อน)
    print("Waiting 20s for ChatGPT to load fully...")
    time.sleep(20)

    # 4. ใช้ Tab เพื่อหาช่องแชท (Address Bar -> Chat Input)
    # โดยปกติกด Tab ประมาณ 10 ครั้งจะเจอช่องพิมพ์พอดี
    print("Action: Focusing via TAB keys...")
    for _ in range(10): 
        pyautogui.press('tab')
        time.sleep(0.1)

    # 5. พิมพ์ลิงก์วิดีโอ (ตัวกระตุ้น Focus)
    print(f"Action: Typing YouTube URL manually...")
    pyautogui.write(task['url'])
    time.sleep(1)
    
    # ขึ้นบรรทัดใหม่
    pyautogui.hotkey('shift', 'enter')
    time.sleep(0.5)

    # 6. วางเนื้อหาที่เหลือ
    print("Action: Pasting prompt instructions...")
    pyperclip.copy(template)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(2)
    
    # 7. ส่งภารกิจ
    pyautogui.press('enter')
    
    print("✅ Mission Sent Successfully!")

    # นับถอยหลัง 60 วิ
    for i in range(60, 0, -1):
        sys.stdout.write(f"\rGeneration time: {i}s ")
        sys.stdout.flush()
        time.sleep(1)

if __name__ == "__main__":
    time.sleep(2)
    run_mission()
