from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Image viewer')


root.geometry("800x600")
#Gambar yang akan digunakan
img_path = [
    "image/454498640_1027618212059025_2435864408701899092_n.jpg",
    "image/1974782-1c10d.jpg",
    "image/cesario-and-a-piece-of-paper-v0-f1u0tk3x53pd1.jpeg",
    "image/GUiG241a8AQV-Ma.png",
    "image/4f44c22ec1a138e02c7d3705fc1f558c.jpg"
]

original_images = [Image.open(path) for path in img_path]


current_index = 0

#Untuk meresized image di img_path
def update_size(event = None):
    global img_resized, image_label
    #dapatkan ukuran jendela
    width, height = root.winfo_width(), root.winfo_height()
    img_resized = original_images[current_index].copy()
    img_resized.thumbnail((width, height), Image.Resampling.LANCZOS)
    #resize gambar sesuai ukuran window
    img_resized = original_images[current_index].resize((width, height))
    img_tk = ImageTk.PhotoImage(img_resized)
    # update label gambar
    image_label.config(image=img_tk)
    image_label.image = img_tk

        
frameImage = Frame(root)
frameImage.pack(fill=BOTH, expand=True)

canvas = Canvas(frameImage, width=800, height=600)
canvas.pack(fill=BOTH, expand=True)

image_label = Label(canvas)
image_label.pack(fill=BOTH, expand=True)

#Function untuk tombol next dan previous

def show_previous():
    global current_index
    if current_index > 0:
        current_index -= 1
        update_size()

def show_next():
    global current_index
    if current_index < len(original_images) - 1:
        current_index += 1
        update_size()

        

#Event listener
root.bind("<Configure>", update_size)

root.bind("<Escape>", lambda event:root.quit())
root.bind("<Left>", lambda event:show_previous())
root.bind("<Right>", lambda event:show_next())
#Tampilkan gambar pertama
update_size()

root.mainloop()