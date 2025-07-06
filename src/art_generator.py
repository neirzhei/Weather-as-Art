import random
import math
from PIL import Image, ImageDraw

def generate_art(temp, rain):
    if temp is None or rain is None:
        return None
    try:
        width, height = 1200, 1200
        img = Image.new('RGB', (width, height), 'white')
        draw = ImageDraw.Draw(img)

        if temp < 10:
            base_color = (220, 230, 240)
        elif temp < 20:
            base_color = (230, 240, 250)
        elif temp < 25:
            base_color = (240, 250, 230)
        elif temp < 30:
            base_color = (250, 240, 220)
        else:
            base_color = (250, 220, 200)
        draw.rectangle([0, 0, width, height], fill=base_color)

        if temp < 20:
            for _ in range(int(2000 + temp * 50 + rain * 10)):
                x, y = random.randint(0, width), random.randint(0, height)
                size = random.randint(5, int(30 - temp + rain * 0.1))
                color = random.choice([(200, 220, 255), (255, 255, 255)])
                if random.choice([True, False]):
                    points = [(x + size * math.cos(i * math.pi / 3), y + size * math.sin(i * math.pi / 3)) for i in range(6)]
                    draw.polygon(points, fill=color)
                else:
                    draw.ellipse([x - size, y - size, x + size, y + size], fill=color)
        else:
            for _ in range(int(1000 + (temp - 20) * 100 + rain * 8)):
                x, y = random.randint(0, width), random.randint(0, height)
                size = random.randint(10, int(50 + (temp - 20) * 5 + rain * 0.1))
                color = (random.randint(50, 100), random.randint(100, 200), random.randint(150, 255))
                draw.rectangle([x, y, x + size, y + size], fill=color)

        draw.rectangle([5, 5, 250, 30], fill=(0, 0, 0))
        draw.text((10, 10), f"Temp: {temp:.1f}°C, Rain: {rain:.1f}mm", fill=(255, 255, 255))

        img.save("artwork.png")
        return "artwork.png"
    except Exception as e:
        print(f"Error generating artwork: {e}")
        return None
