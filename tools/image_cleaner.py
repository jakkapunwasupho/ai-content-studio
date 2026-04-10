import os
import sys
from PIL import Image

class Style:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'

def clean_and_format_image(input_path, output_path, resolution=(1080, 1350)):
    """
    ลบลายน้ำโดยการ Crop ขอบล่าง และปรับสัดส่วนเป็น 4:5
    """
    try:
        img = Image.open(input_path)
        width, height = img.size
        
        # 1. ลบลายน้ำ (Crop ขอบล่างออกประมาณ 5-7%)
        # โดยปกติ Gemini Watermark จะอยู่มุมล่าง
        crop_bottom = int(height * 0.07)
        img_cropped = img.crop((0, 0, width, height - crop_bottom))
        
        # 2. ปรับสัดส่วนเป็น 4:5 (1080x1350)
        # เราจะใช้วิธี Resize และรักษาสัดส่วน หรือ Padding
        img_cropped.thumbnail(resolution, Image.Resampling.LANCZOS)
        
        # สร้างพื้นหลังสีดำ (หรือโปร่งใส) เพื่อรองรับสัดส่วนที่ขาด
        final_img = Image.new("RGB", resolution, (0, 0, 0))
        # วางรูปไว้ตรงกลาง
        offset = ((resolution[0] - img_cropped.width) // 2, (resolution[1] - img_cropped.height) // 2)
        final_img.paste(img_cropped, offset)
        
        final_img.save(output_path, "JPEG", quality=95)
        print(f"[{Style.GREEN}CLEANED{Style.END}] Saved to: {output_path}")
        return True
    except Exception as e:
        print(f"[{Style.RED}ERROR{Style.END}] Failed to process image: {e}")
        return False

def process_all_incoming(incoming_dir, final_dir):
    if not os.path.exists(incoming_dir):
        os.makedirs(incoming_dir, exist_ok=True)
        return

    files = [f for f in os.listdir(incoming_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    if not files:
        print(f"[{Style.YELLOW}SKIP{Style.END}] No new images to clean.")
        return

    os.makedirs(final_dir, exist_ok=True)
    for filename in files:
        in_p = os.path.join(incoming_dir, filename)
        out_p = os.path.join(final_dir, f"clean_{filename}")
        if clean_and_format_image(in_p, out_p):
            # ย้ายไฟล์ต้นฉบับไปไว้ใน archive หรือลบทิ้ง
            # os.remove(in_p) 
            pass

if __name__ == "__main__":
    # ทดสอบรัน
    print("Image Cleaner Module Ready.")
