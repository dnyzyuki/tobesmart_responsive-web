from PIL import Image
import os

def trim(im):
    bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
    diff = Image.frombytes(im.mode, im.size, bytes([255 - (a^b) for a, b in zip(im.tobytes(), bg.tobytes())])) # Simple diff for RGB
    # Better approach for possibly noisy images or alpha
    # Convert to grayscale and invert
    # Actually, let's assuming white background and RGB/RGBA.
    
    if im.mode != 'RGB' and im.mode != 'RGBA':
        im = im.convert('RGBA')
    
    bg = Image.new(im.mode, im.size, (255, 255, 255, 255))
    diff = list(im.getdata())
    
    # Simple bounding box
    bbox = im.getbbox()
    if bbox:
        return im.crop(bbox)
    return im

def trim_white_bg(image_path):
    try:
        img = Image.open(image_path)
        img = img.convert("RGBA")
        
        # Create a mask of non-white pixels
        # (Assuming white is (255, 255, 255))
        # We can also consider "near white"
        datas = img.getdata()
        
        newData = []
        for item in datas:
            # Change all white (also shades of whites)
            # to transparent
            if item[0] > 240 and item[1] > 240 and item[2] > 240:
                newData.append((255, 255, 255, 0))
            else:
                newData.append(item)
        
        img.putdata(newData)
        
        # Now get bbox of non-transparent
        bbox = img.getbbox()
        if bbox:
            cropped = img.crop(bbox)
            cropped.save(image_path)
            print(f"Trimmed {image_path}: {bbox}")
        else:
            print(f"Skipped {image_path} (empty bbox)")
            
    except Exception as e:
        print(f"Error processing {image_path}: {e}")

directory = r"C:\Users\kangdo\tobesmart-website\images"
for i in range(1, 17):
    path = os.path.join(directory, f"partner_logo_{i}.png")
    trim_white_bg(path)
