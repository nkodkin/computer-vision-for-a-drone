import tkinter as tk
from PIL import Image, ImageTk, ImageDraw
import random
from GenerateSquares import generate_white_image, draw_random_square
from AnalyseImages import show_images
import matplotlib.pyplot as plt


def load_images():
    images = []

    image_paths = ["test_img/image1.png",
                   "test_img/image2.png", "test_img/image.png"]
    for path in image_paths:
        image = Image.open(path)
        # image = image.resize((200, 200))  # Resize the image
        photo = ImageTk.PhotoImage(image)
        images.append(photo)
    return images


def generate_images():

    image1 = generate_white_image(300, 300)
    draw_random_square(image1, 30)
    image1.save("test_img/image1.png")
    photo1 = ImageTk.PhotoImage(image1)
    image_label1.config(image=photo1)
    image_label1.image = photo1

    image2 = generate_white_image(300, 300)
    draw_random_square(image2, 30)
    image2.save("test_img/image2.png")
    photo2 = ImageTk.PhotoImage(image2)
    image_label2.config(image=photo2)
    image_label2.image = photo2

    show_images("test_img/image1.png", "test_img/image2.png")

    image3 = Image.open("test_img/image.png")
    photo3 = ImageTk.PhotoImage(image3)
    image_label3.config(image=photo3)
    image_label3.image = photo3


window = tk.Tk()
window.title("Image Viewer")


images = load_images()

image_label1 = tk.Label(window, image=images[0])
image_label1.grid(row=0, column=0, padx=10, pady=10)

image_label2 = tk.Label(window, image=images[1])
image_label2.grid(row=0, column=1, padx=10, pady=10)


image_label3 = tk.Label(window, image=images[2])
image_label3.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

generate_button = tk.Button(
    window, text="Generate Images", command=generate_images)
generate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)


window.configure(background="grey")
window.mainloop()
