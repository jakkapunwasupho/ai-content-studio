import os
import sys
import json
from datetime import datetime
from tools.video_handler import download_and_cut
from tools.image_cleaner import process_all_incoming

# บังคับให้ใช้ UTF-8 ในการพิมพ์ข้อความ
import sys
sys.stdout.reconfigure(encoding='utf-8')

# --- UI STYLES ---
class Style:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    CYAN = '\033[96m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    END = '\033[0m'

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
QUEUE_FILE = os.path.join(ROOT_DIR, "youtube_queue.json")

def print_banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"\n{Style.CYAN}{Style.BOLD}=== AI CONTENT STUDIO: MISSION CONTROL ==={Style.END}")
    print(f"Status: {Style.GREEN}Online{Style.END} | Date: {datetime.now().strftime('%Y-%m-%d')}")
    print("-" * 50)

def process_daily_video():
    try:
        with open(QUEUE_FILE, "r", encoding="utf-8") as f:
            queue = json.load(f)
        
        # ค้นหาวิดีโอที่ยังไม่ได้ทำ (Pending)
        task = next((item for item in queue if item["status"] == "pending"), None)
        
        if not task:
            print(f"{Style.GREEN}🎉 All tasks complete!{Style.END}")
            return

        print(f"\n{Style.YELLOW}Starting Daily Task: {task['title']}{Style.END}")
        url = task["url"]
        
        # เรียกใช้เครื่องมือตัดวิดีโอ
        # ในที่นี้ตัวอย่างตัด 30 วิแรก (ปรับแต่งได้ตามหน้างาน)
        output = download_and_cut(url, start_time=0, duration=30, output_name=f"daily_{task['id']}.mp4")
        
        if output:
            task["status"] = "done"
            task["processed_at"] = datetime.now().isoformat()
            with open(QUEUE_FILE, "w", encoding="utf-8") as f:
                json.dump(queue, f, indent=4, ensure_ascii=False)
            print(f"{Style.GREEN}✅ Video task complete!{Style.END}")
            
    except Exception as e:
        print(f"{Style.RED}Error in daily task: {e}{Style.END}")

def run_image_cleaning():
    incoming = os.path.join(ROOT_DIR, "projects", "incoming")
    today_str = datetime.now().strftime("%Y-%m-%d")
    final = os.path.join(ROOT_DIR, "projects", "public_commercial", today_str, "images")
    
    print(f"\n{Style.CYAN}Scanning for new images in {incoming}...{Style.END}")
    process_all_incoming(incoming, final)

def main_menu():
    print_banner()
    print(f"{Style.BLUE}[1]{Style.END} 🎬 Process Today's YouTube Task")
    print(f"{Style.BLUE}[2]{Style.END} 🤖 Launch Bot Automation (PyAutoGUI Script)")
    print(f"{Style.BLUE}[3]{Style.END} 🧹 Run Image Cleaning Lab (Crop & Resize)")
    print(f"{Style.BLUE}[4]{Style.END} 📋 View Queue Status")
    print(f"{Style.BLUE}[0]{Style.END} 🚪 Exit")
    
    choice = input(f"\n{Style.BOLD}Choice: {Style.END}")
    
    if choice == "1":
        process_daily_video()
    elif choice == "2":
        print(f"\n{Style.YELLOW}Manual Tip: Run 'python tools/bot_stealth.py' for security.{Style.END}")
    elif choice == "3":
        run_image_cleaning()
    elif choice == "4":
        show_queue()
    elif choice == "0":
        sys.exit()
    
    input(f"\n{Style.CYAN}Press Enter to return...{Style.END}")

def show_queue():
    if os.path.exists(QUEUE_FILE):
        with open(QUEUE_FILE, "r", encoding="utf-8") as f:
            queue = json.load(f)
            for item in queue:
                status = f"{Style.GREEN}[DONE]{Style.END}" if item["status"] == "done" else f"{Style.YELLOW}[PENDING]{Style.END}"
                print(f"{status} {item['title']} - {item['url']}")

if __name__ == "__main__":
    while True:
        main_menu()
