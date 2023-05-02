from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

GREEN = "#9bdeac"
YELLOW = "#f7f5dd"

def Upload2():
    global window
    types = [('PNG Files', '*.png'),('Jpg Files', '*.jpg') ]
    filename = filedialog.askopenfilename(filetypes=types)
    canvas = Canvas()
    image = Image.open(filename)
    image = image.resize((350,350), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)
    logo = Image.open("Logo.png")
    logo = logo.resize((113,38), Image.ANTIALIAS)
    logo = ImageTk.PhotoImage(logo)
    window.logo = logo
    window.image = image
    canvas.create_image(200, 100, image=image)
    canvas.create_image(310,250, image=logo)
    canvas.grid(row=3, column=0, columnspan=4, rowspan=4)



window = Tk()
window.title("Image Watermarking")
window.config()
window.geometry("450x400")
label = Label(text="Upload an Image", font=("Montserat", 20, "bold"), fg="black",padx=102)
label.grid(column=0, row=0)
button = Button(window, text="Upload File",width=20, command=Upload2)
button.grid(column=0, row=1)









window.mainloop()