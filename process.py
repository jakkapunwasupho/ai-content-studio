import subprocess
import sys
import os
import argparse
import re

def get_video_id(url):
    # Simple regex to get video id
    match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11}).*", url)
    return match.group(1) if match else "video"

def get_video_duration(url, ytdlp_path):
    cmd = [ytdlp_path, '--get-duration', url]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        return None
    
    duration_str = result.stdout.strip()
    parts = list(map(int, duration_str.split(':')))
    if len(parts) == 3:
        return parts[0] * 3600 + parts[1] * 60 + parts[2]
    elif len(parts) == 2:
        return parts[0] * 60 + parts[1]
    elif len(parts) == 1:
        return parts[0]
    return None

def process_video(url, start_time=None, duration=None, last_seconds=None, output_name="clip_result.mp4"):
    root_dir = os.path.dirname(os.path.abspath(__file__))
    ytdlp_path = os.path.join(root_dir, "yt-dlp.exe")
    ffmpeg_path = os.path.join(root_dir, "bin", "ffmpeg.exe")
    output_dir = os.path.join(root_dir, "youtube")
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    output_path = os.path.join(output_dir, output_name)
    vid_id = get_video_id(url)

    print(f"--- Analyzing: {url} ---")
    total_duration = get_video_duration(url, ytdlp_path)
    
    # Threshold: 30 Minutes (1800 seconds)
    is_long_video = total_duration and total_duration > 1800
    
    if last_seconds and total_duration:
        start_time = max(0, total_duration - last_seconds)
        duration = last_seconds
        print(f"> Target: Last {last_seconds}s (Starts at {start_time}s)")
    
    if is_long_video:
        print(f">>> Strategy: Master + Clip (Video > 1.5h)")
        master_file = os.path.join(output_dir, f"master_{vid_id}.mp4")
        
        # Step 1: Download Master if not exists
        if not os.path.exists(master_file):
            print(f"Step 1: Downloading Full Master (This may take a while)...")
            # Using -f "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]" for compatibility
            dl_cmd = [ytdlp_path, '-f', 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]', '-o', master_file, url]
            subprocess.run(dl_cmd)
        else:
            print(f"Step 1: Master file already exists at {master_file}")
            
        # Step 2: Cut from Local Master
        print(f"Step 2: Cutting clip from local master...")
        ffmpeg_cmd = [ffmpeg_path, '-y', '-i', master_file]
        if start_time is not None:
            ffmpeg_cmd += ['-ss', str(start_time)]
        if duration is not None:
            ffmpeg_cmd += ['-t', str(duration)]
        
        ffmpeg_cmd += ['-c', 'copy', output_path] # Use copy for speed from local
        subprocess.run(ffmpeg_cmd)
        
    else:
        print(f">>> Strategy: Direct Streaming (Video < 1.5h)")
        # Fetch stream URL
        cmd_url = [ytdlp_path, '-g', '-f', 'bestvideo+bestaudio/best', url]
        result = subprocess.run(cmd_url, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Error fetching URL: {result.stderr}")
            return
        
        urls = result.stdout.strip().split('\n')
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
        subprocess.run(ffmpeg_cmd)

    print(f"--- Process Complete! ---")
    print(f"Saved to: {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download and cut YouTube video")
    parser.add_argument("url", help="YouTube URL")
    parser.add_argument("--start", type=float, help="Start time in seconds")
    parser.add_argument("--duration", type=float, help="Duration in seconds")
    parser.add_argument("--last", type=float, help="Cut the last X seconds")
    parser.add_argument("--output", default="clip_result.mp4", help="Output filename")
    
    args = parser.parse_args()
    process_video(args.url, args.start, args.duration, args.last, args.output)
