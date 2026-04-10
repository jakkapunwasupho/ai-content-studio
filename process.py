import subprocess
import sys
import os
import argparse
import re
import json
from datetime import datetime

# --- CONFIGURATION (Add more categories here in the future) ---
CATEGORIES = ['images', 'music', 'animations', 'youtube']

# --- Ultra-Premium CLI Styles ---
class Style:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    END = '\033[0m'

def log_success(msg): print(f"{Style.GREEN}✔ [SUCCESS]{Style.END} {msg}")
def log_info(msg):    print(f"{Style.BLUE}ℹ [INFO]{Style.END} {msg}")
def log_warn(msg):    print(f"{Style.YELLOW}⚠ [WARNING]{Style.END} {msg}")
def log_error(msg):   print(f"{Style.RED}✖ [ERROR]{Style.END} {msg}")
def log_step(msg):    print(f"{Style.BOLD}{Style.BLUE}🚀 {msg}{Style.END}")

def get_video_id(url):
    match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11}).*", url)
    return match.group(1) if match else "video"

def get_video_duration(url, ytdlp_path):
    cmd = [ytdlp_path, '--get-duration', url]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0: return None
    duration_str = result.stdout.strip()
    parts = list(map(int, duration_str.split(':')))
    if len(parts) == 3: return parts[0] * 3600 + parts[1] * 60 + parts[2]
    elif len(parts) == 2: return parts[0] * 60 + parts[1]
    elif len(parts) == 1: return parts[0]
    return None

def save_metadata(path, data):
    meta_path = os.path.splitext(path)[0] + ".json"
    with open(meta_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    log_info(f"Metadata saved to: {os.path.basename(meta_path)}")

def process_video(url, start_time=None, duration=None, last_seconds=None, output_name="clip_result.mp4", project_type="public_commercial"):
    root_dir = os.path.dirname(os.path.abspath(__file__))
    ytdlp_path = os.path.join(root_dir, "yt-dlp.exe")
    ffmpeg_path = os.path.join(root_dir, "bin", "ffmpeg.exe")
    
    # Project Base Path
    project_dir = os.path.join(root_dir, "projects", project_type)
    today_str = datetime.now().strftime("%Y-%m-%d")
    date_dir = os.path.join(project_dir, today_str)
    
    # INITIALIZE ALL CATEGORIES
    for cat in CATEGORIES:
        os.makedirs(os.path.join(date_dir, cat), exist_ok=True)
    
    # Master storage setup
    master_dir = os.path.join(root_dir, "youtube", "masters")
    os.makedirs(master_dir, exist_ok=True)
    
    output_path = os.path.join(date_dir, "youtube", output_name)
    vid_id = get_video_id(url)

    log_step(f"AI STUDIO ENGINE: [{project_type.upper()}] | Initializing {today_str}...")
    
    total_duration = get_video_duration(url, ytdlp_path)
    is_long_video = total_duration and total_duration > 1800
    
    if last_seconds and total_duration:
        start_time = max(0, total_duration - last_seconds)
        duration = last_seconds

    metadata = {
        "url": url,
        "video_id": vid_id,
        "start_time": start_time,
        "duration": duration,
        "processed_at": datetime.now().isoformat(),
        "project": project_type,
        "strategy": "Master+Clip" if is_long_video else "Streaming"
    }

    if is_long_video:
        log_step("Strategy: Master + Clip workflow")
        master_file = os.path.join(master_dir, f"master_{vid_id}.mp4")
        if not os.path.exists(master_file):
            log_info(f"Downloading Master for {vid_id}...")
            dl_cmd = [ytdlp_path, '-f', 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]', '-o', master_file, url]
            subprocess.run(dl_cmd)
        
        ffmpeg_cmd = [ffmpeg_path, '-y', '-i', master_file]
        if start_time is not None: ffmpeg_cmd += ['-ss', str(start_time)]
        if duration is not None: ffmpeg_cmd += ['-t', str(duration)]
        ffmpeg_cmd += ['-c', 'copy', output_path]
        subprocess.run(ffmpeg_cmd, capture_output=True)
    else:
        log_step("Strategy: Direct Streaming")
        cmd_url = [ytdlp_path, '-g', '-f', 'bestvideo+bestaudio/best', url]
        res = subprocess.run(cmd_url, capture_output=True, text=True)
        if res.returncode != 0: return
        urls = res.stdout.strip().split('\n')
        v_url = urls[0]
        a_url = urls[1] if len(urls) > 1 else v_url
        ffmpeg_cmd = [ffmpeg_path, '-y']
        if start_time is not None: ffmpeg_cmd += ['-ss', str(start_time)]
        ffmpeg_cmd += ['-i', v_url]
        if len(urls) > 1:
            if start_time is not None: ffmpeg_cmd += ['-ss', str(start_time)]
            ffmpeg_cmd += ['-i', a_url]
        if duration is not None: ffmpeg_cmd += ['-t', str(duration)]
        ffmpeg_cmd += ['-c:v', 'libx264', '-c:a', 'aac', '-preset', 'fast', '-shortest', output_path]
        subprocess.run(ffmpeg_cmd, capture_output=True)

    if os.path.exists(output_path) and os.path.getsize(output_path) > 0:
        save_metadata(output_path, metadata)
        log_success(f"Work Complete! Saved to: {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AI Content Studio")
    parser.add_argument("url", help="YouTube URL")
    parser.add_argument("--start", type=float, help="Start time in seconds")
    parser.add_argument("--duration", type=float, help="Duration in seconds")
    parser.add_argument("--last", type=float, help="Cut the last X seconds")
    parser.add_argument("--output", default="clip_result.mp4", help="Output filename")
    parser.add_argument("--project", choices=["public_commercial", "personal_religious"], default="public_commercial", help="Project type")
    
    args = parser.parse_args()
    process_video(args.url, args.start, args.duration, args.last, args.output, args.project)
