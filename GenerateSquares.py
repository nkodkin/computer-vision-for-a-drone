from PIL import Image, ImageDraw
import random
import tkinter as tk


def generate_white_image(width, height):
    
    image = Image.new("RGB", (width, height), "white")
    return image


def draw_random_square(image, size):
    draw = ImageDraw.Draw(image)

    color = (138, 43, 226)

    x = random.randint(0, image.width - size)
    y = random.randint(0, image.height - size)

    draw.rectangle([(x, y), (x + size, y + size)], fill=color)
