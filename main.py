
from tkinter import *
from PIL import ImageTk, Image, ImageFont, ImageDraw
from tkinter import filedialog, messagebox
import shutil
import os


import matplotlib.pyplot as plt
import numpy as np

from tkinter import filedialog

watermark_to_enter = []
filenamed=[]
deletable_buttons_etc = []
wmed_image = []

def browseFiles():
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("Text files",
                                                      "*.txt*"),
                                                     ("all files",
                                                      "*.*")))

    filenamed.append(filename)

    # Change label contents
    label_file_explorer.configure(text="File Opened: " + filename)
    global img
    img = Image.open(filename)

    # resize the image and apply a high-quality down sampling filter
    img = img.resize((300, 300), Image.LANCZOS)

    # PhotoImage class is used to add image to widgets, icons etc
    display_img = ImageTk.PhotoImage(img)

    # create a label
    panel = Label(window, image=display_img)

    # set the image as img
    panel.image = display_img
    panel.grid(column=1, row=4)

    watermark_label = Label(window, text = "enter Watermark:")
    watermark_label.grid(column=0, row=5)
    deletable_buttons_etc.append(watermark_label)

    watermark_entry = Entry(window, width=30)
    watermark_entry.grid(column=1, row=5)
    watermark_to_enter.append(watermark_entry)

    watermark_button = Button(window, text="submit", command=make_watermark)
    watermark_button.grid(column=2, row=5)
    deletable_buttons_etc.append(watermark_button)


def make_watermark():
    wm_entry = watermark_to_enter[0]
    #print(filenamed[0])
    watermark_image = Image.open(filenamed[0])
    #watermark_image.show()

    # resize the image and apply a high-quality down sampling filter
    watermark_image = watermark_image.resize((300, 300), Image.LANCZOS)

    draw = ImageDraw.Draw(watermark_image)
    # ("font type",font size)
    w, h = watermark_image.size
    x, y = int(w / 2), int(h / 2)
    if x > y:
        font_size = y
    elif y > x:
        font_size = x
    else:
        font_size = x

    font = ImageFont.truetype("arial.ttf", int(font_size / 6))

    # add Watermark
    # (0,0,0)-black color text
    draw.text((x, y), wm_entry.get(), fill=(0, 0, 0), font=font, anchor='ms')
    # plt.subplot(1, 2, 1)
    # plt.title("black text")
    # plt.imshow(watermark_image)
    #watermark_image.show()
    wmed_image.append(watermark_image)
    display_img = ImageTk.PhotoImage(watermark_image)
    panel2 = Label(window, image=display_img)
    deletable_buttons_etc.append(panel2)

    # set the image as img
    panel2.image = display_img
    panel2.grid(column=1, row=6)


    save_button = Button(window, text="save photo", command=save_photo)
    save_button.grid(column=1, row=7)
    deletable_buttons_etc.append(save_button)

    start_again_button = Button(window,text="start again", command=start_process_again)
    start_again_button.grid(column=2, row=7)
    deletable_buttons_etc.append(start_again_button)


def start_process_again():
    watermark_to_enter.clear()
    filenamed.clear()
    wmed_image.clear()
    for tk_thing in deletable_buttons_etc:
        tk_thing.destroy()

    browseFiles()


def save_photo():
    img_to_save = wmed_image[0]
    #img_to_save.show()
    file = filedialog.asksaveasfile(mode='w', defaultextension=".jpg",
                                    filetypes=(("JPG file", "*.jpg"), ("PNG file", "*.png"), ("All Files", "*.*")))

    if file:
        img_to_save.save(file)  # saves the image to the input file name.





# Create the root window
window = Tk()

# Set window title
window.title('File Explorer')

# Set window size
window.geometry("500x500")

# Set window background color
window.config(background="white")
window.resizable(width = True, height = True)

# Create a File Explorer label
label_file_explorer = Label(window,
                            text="watermark APP using Tkinter",
                            width=100, height=4,
                            fg="blue")

button_explore = Button(window,
                        text="Browse Files",
                        command=browseFiles)

button_exit = Button(window,
                     text="Exit",
                     command=exit)

# Grid method is chosen for placing
# the widgets at respective positions
# in a table like structure by
# specifying rows and columns
label_file_explorer.grid(column=1, row=1)

button_explore.grid(column=1, row=2)

button_exit.grid(column=1, row=3)

# Let the window wait for any events
window.mainloop()
