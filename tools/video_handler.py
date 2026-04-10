import subprocess
import os
import json
import re
from datetime import datetime

# Import styles from a shared place or define here
class Style:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    END = '\033[0m'

CATEGORIES = ['images', 'music', 'video-animation', 'video-clips']

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

def download_and_cut(url, start_time=None, duration=None, last_seconds=None, output_name="clip.mp4", project_type="public_commercial"):
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    bin_dir = os.path.join(root_dir, "bin")
    ytdlp_path = os.path.join(bin_dir, "yt-dlp.exe")
    ffmpeg_path = os.path.join(bin_dir, "ffmpeg.exe")
    
    project_dir = os.path.join(root_dir, "projects", project_type)
    today_str = datetime.now().strftime("%Y-%m-%d")
    date_dir = os.path.join(project_dir, today_str)
    
    for cat in CATEGORIES:
        os.makedirs(os.path.join(date_dir, cat), exist_ok=True)
        
    master_dir = os.path.join(root_dir, "projects", "source-vault")
    os.makedirs(master_dir, exist_ok=True)
    
    output_path = os.path.join(date_dir, "video-clips", output_name)
    vid_id = get_video_id(url)
    total_duration = get_video_duration(url, ytdlp_path)
    
    if last_seconds and total_duration:
        start_time = max(0, total_duration - last_seconds)
        duration = last_seconds

    # --- CLI Status ---
    print(f"[{Style.BLUE}INFO{Style.END}] Processing: {vid_id} in {project_type}")

    is_long_video = total_duration and total_duration > 1800
    
    if is_long_video:
        master_file = os.path.join(master_dir, f"master_{vid_id}.mp4")
        if not os.path.exists(master_file):
            print(f"[{Style.YELLOW}WAIT{Style.END}] Downloading Master (Long Video)...")
            subprocess.run([ytdlp_path, '-f', 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]', '-o', master_file, url])
        
        cmd = [ffmpeg_path, '-y', '-i', master_file]
        if start_time: cmd += ['-ss', str(start_time)]
        if duration: cmd += ['-t', str(duration)]
        cmd += ['-c', 'copy', output_path]
        subprocess.run(cmd, capture_output=True)
    else:
        # Direct Streaming Strategy
        cmd_url = [ytdlp_path, '-g', '-f', 'bestvideo+bestaudio/best', url]
        res = subprocess.run(cmd_url, capture_output=True, text=True)
        if res.returncode == 0:
            urls = res.stdout.strip().split('\n')
            v_url = urls[0]
            a_url = urls[1] if len(urls) > 1 else v_url
            cmd = [ffmpeg_path, '-y']
            if start_time: cmd += ['-ss', str(start_time)]
            cmd += ['-i', v_url]
            if len(urls) > 1:
                if start_time: cmd += ['-ss', str(start_time)]
                cmd += ['-i', a_url]
            if duration: cmd += ['-t', str(duration)]
            cmd += ['-c:v', 'libx264', '-c:a', 'aac', '-preset', 'fast', '-shortest', output_path]
            subprocess.run(cmd, capture_output=True)

    if os.path.exists(output_path):
        save_metadata(output_path, {"url": url, "processed_at": datetime.now().isoformat()})
        print(f"[{Style.GREEN}OK{Style.END}] Saved: {output_path}")
        return output_path
    return None
