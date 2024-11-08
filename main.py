import tkinter as tk
from tkinter import messagebox


def show_message():
    messagebox.showinfo("Happy Diwali!", "Wishing you a joyous and prosperous Diwali!")

def create_gradient(canvas, width, height, color1, color2):
   
    for i in range(0, height, 2):
        r = int(color1[0] + (color2[0] - color1[0]) * (i / height))
        g = int(color1[1] + (color2[1] - color1[1]) * (i / height))
        b = int(color1[2] + (color2[2] - color1[2]) * (i / height))
        color = f'#{r:02x}{g:02x}{b:02x}'
        canvas.create_line(0, i, width, i, fill=color)


root = tk.Tk()
root.title("Diwali Wishes")
root.geometry("400x300")


canvas = tk.Canvas(root, width=400, height=300)
canvas.pack(fill="both", expand=True)


color1 = (255, 99, 71)   
color2 = (75, 0, 130)   
create_gradient(canvas, 400, 300, color1, color2)


label = tk.Label(root, text="Happy Diwali!", font=("Helvetica", 24, "bold"), fg="white", bg="#4B0082")
label.place(relx=0.5, rely=0.3, anchor="center")


button = tk.Button(root, text="Click for Wishes", font=("Helvetica", 14), fg="white", bg="#FFA500", command=show_message)
button.place(relx=0.5, rely=0.7, anchor="center")

root.mainloop()
