from PIL import Image, ImageDraw, ImageFont
import os

def generate_text_logo(text, filename, color):
    # Image settings
    width, height = 500, 150
    image = Image.new("RGBA", (width, height), (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)
    
    # Try to find a good font
    font_paths = [
        "C:\\Windows\\Fonts\\bahnschrift.ttf",
        "C:\\Windows\\Fonts\\segoeuib.ttf",
        "C:\\Windows\\Fonts\\arialbd.ttf"
    ]
    
    font = None
    for path in font_paths:
        if os.path.exists(path):
            try:
                font = ImageFont.truetype(path, 80)
                break
            except:
                continue
    
    if not font:
        font = ImageFont.load_default()
    
    # Calculate text position (center)
    # Use textbbox in newer Pillow versions
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    x = (width - text_width) // 2
    y = (height - text_height) // 2 - 10 # Slight adjustment
    
    draw.text((x, y), text, fill=color, font=font)
    
    # Trim the transparent edges
    bbox_trimmed = image.getbbox()
    if bbox_trimmed:
        image = image.crop(bbox_trimmed)
        # Add some padding
        padding = 10
        new_width = image.width + padding * 2
        new_height = image.height + padding * 2
        final_image = Image.new("RGBA", (new_width, new_height), (255, 255, 255, 0))
        final_image.paste(image, (padding, padding))
        image = final_image

    image.save(filename)
    print(f"Generated {filename}")

os.makedirs("C:\\Users\\kangdo\\tobesmart-website\\images", exist_ok=True)

# Colors
DARK_COLOR = (51, 51, 51, 255) # Match #333333
LIGHT_COLOR = (255, 255, 255, 255)

# Generate logos
generate_text_logo("SALESCUBE", "C:\\Users\kangdo\\tobesmart-website\\images\\sales_cube_b.png", DARK_COLOR)
generate_text_logo("SALESCUBE", "C:\\Users\kangdo\\tobesmart-website\\images\\sales_cube.png", LIGHT_COLOR)
generate_text_logo("CONTROLCUBE", "C:\\Users\kangdo\\tobesmart-website\\images\\control_cube_b.png", DARK_COLOR)
generate_text_logo("CONTROLCUBE", "C:\\Users\kangdo\\tobesmart-website\\images\\control_cube.png", LIGHT_COLOR)
