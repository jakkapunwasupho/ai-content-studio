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
    
    # 1. เปิด Chrome ไปที่ ChatGPT โดยตรง
    print(f"Action: Opening Chrome at {CHAT_URL}...")
    subprocess.Popen(f'"{CHROME_PATH}" --profile-directory="{CHROME_PROFILE}" {CHAT_URL}', shell=True)
    time.sleep(10) # รอเบราเซอร์เปิด
    
    # 2. รอโหลด ChatGPT จนสมบูรณ์
    print("Waiting 10s for ChatGPT to start loading...")
    time.sleep(10)

    # 3. เตรียมข้อมูลลง Clipboard
    print(f"Action: Preparing full prompt to clipboard...")
    full_prompt = f"{task['url']}\n\n{template}"
    pyperclip.copy(full_prompt)
    time.sleep(1)

    # 4. เรียกใช้ AutoHotkey มาจัดการ Focus และ Paste (ชัวร์ที่สุดบน Windows)
    print("Action: Triggering AutoHotkey for Stealth Paste...")
    ahk_script = os.path.join(ROOT_DIR, "tools", "stealth_paste.ahk")
    os.startfile(ahk_script) # รันไฟล์ .ahk โดยตรง
    
    print("✅ Mission Handoff to AHK Successful!")
    
    print("✅ Mission Sent Successfully!")

    # นับถอยหลัง 60 วิ
    for i in range(60, 0, -1):
        sys.stdout.write(f"\rGeneration time: {i}s ")
        sys.stdout.flush()
        time.sleep(1)

if __name__ == "__main__":
    time.sleep(2)
    run_mission()
