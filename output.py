import tkinter as tk
from tkinter import*
import requests
from tkinter import filedialog
from PIL import Image, ImageTk
import pytesseract
from PIL import Image 
#
m= tk.Tk()
m.title("Klip")
#ytics import TextAnalyticsClient
#import pytesseract
#from selenium import webdriver
#import time
hi = 700
wi = 1200
def UploadAction(event=None):
    filename = filedialog.askopenfilename()
    a = filename
    pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract.exe"

    img=Image.open(a)

    text=pytesseract.image_to_string(img)

    print(text)


#     print('Selected:', filename)
   

def UploadAction1(event=None):
    filename = filedialog.askopenfilename()
#     print('Selected:', filename)

canvas = tk.Canvas(m, height=hi, width=wi)
canvas.pack()

background_image = tk.PhotoImage(file="0.png")
backgorund_label = tk.Label(m, image=background_image)
backgorund_label.place(relwidth=1, relheight=1)

z = tk.Label(m, text="Klip", bg="white", font=('Helvetica', 24, 'bold italic'))
z.place(relx = 0.40, rely = 0.05, relwidth=0.17, relheight =0.1)

x = tk.Label(m, text="Upload the source image", bg="cyan", font=('Times Header', 12))
x.place(relx = 0.13, rely = 0.47, relwidth=0.17, relheight =0.08)


y = tk.Label(m, text="Upload the destination image", bg="cyan", font=('Times Header', 12))
y.place(relx = 0.13, rely = 0.6, relwidth=0.17, relheight =0.08)

frame = tk.Frame(m, bg = '#131B88', bd=5)
frame.place(relx=0.40, rely=0.48, relwidth=0.05, relheight=0.055, anchor='n')

button1 = tk.Button(frame, text='Source',command=UploadAction)
button1.place(relx = 0.8, rely = 0.2, relwidth=30, relheight =1 )
button1.config(height=100,width=100)
button1.pack()

lower_frame = tk.Frame(m, bg='#131B88', bd=5 )
lower_frame.place(relx=0.40, rely=0.615, relwidth=0.065, relheight=0.055, anchor='n')

button2 = tk.Button(lower_frame, text='Destination',command=UploadAction1)
button2.place(relx = 0.2, rely = 0.2, relwidth=10, relheight =10 )
button2.config(height=100,width=100)
button2.pack()

go_frame = tk.Frame(m, bg='#7A83F3', bd=5 )
go_frame.place(relx=0.55, rely=0.545, relwidth=0.06, relheight=0.055, anchor='n')

button3 = tk.Button(go_frame, text='GO')
button3.place(relx = 0.20, rely = 0.2, relwidth=400, height =400)
button3.config(height=200, width=200)
button3.pack()

m.mainloop()


