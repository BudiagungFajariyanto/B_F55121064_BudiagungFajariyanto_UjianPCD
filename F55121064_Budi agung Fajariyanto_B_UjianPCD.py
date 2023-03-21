# Nama : Budi agung Fajariyanto
# NIM : F55121064
# Kelas : B

# Import Packages yang digunakan
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
import numpy as np

# Perbaikan citra dengan metode peningkatan kecerahan
def brightness_increase(img):
    brightness = 50
    brightness_img = cv2.add(img, brightness)
    return brightness_img

# Perbaikan citra dengan metode sharpening (penajaman)
def sharpening(img):
    kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
    sharpening_img = cv2.filter2D(img, -1, kernel)
    return sharpening_img

# Fungsi untuk menampilkan gambar
def show_image(img, x, y, title):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(img)
    img = ImageTk.PhotoImage(img)
    label = tk.Label(root, image=img)
    label.image = img
    label.place(x=x, y=y)
    title_label = tk.Label(root, text=title)
    title_label.place(x=x, y=y-20)

# Fungsi untuk memproses citra dan menampilkan hasilnya
def process_image(method):
    global original_img
    if method == 'brightness':
        corrected_img = brightness_increase(original_img)
        show_image(corrected_img, 450, 150, 'Citra Peningkatan Kecerahan')
    elif method == 'sharpening':
        corrected_img = sharpening(original_img)
        show_image(corrected_img, 900, 150, 'Citra Penajaman')

# Fungsi untuk menampilkan informasi creator
def show_creator():
    creator_label = tk.Label(root, text='Nama : Budi agung Fajariyanto    NIM : F55121064    Kelas : B')
    creator_label.place(x=850, y=60)

# Fungsi untuk membuka gambar
def open_image():
    global original_img
    file_path = filedialog.askopenfilename()
    if file_path:
        original_img = cv2.imread(file_path)
        show_image(original_img, 30, 150, 'Citra Asli')
        size_label.config(text='Dimensi : {} x {}'.format(original_img.shape[1], original_img.shape[0]))

# Membuat jendela utama
root = tk.Tk()
root.geometry('1700x1700')
root.title('GUI Aplikasi Penerapan Perbaikan Citra')

# Menambahkan judul citra asli
title_label = tk.Label(root, text='Citra Asli')
title_label.place()

# Menambahkan tombol untuk membuka gambar
open_button = tk.Button(root, text='Masukkan Gambar', command=open_image)
open_button.place(x=300, y=65)

# Menambahkan label untuk menampilkan dimensi gambar
size_label = tk.Label(root, text='Dimensi : -')
size_label.place()

# Menambahkan kotak untuk perbaikan citra
correction_box = tk.LabelFrame(root, text='Perbaikan Citra_F55121064', padx=5, pady=5)
correction_box.place(x=20, y=20, width=250, height=100)

# Tombol untuk perbaikan metode peningkatan kecerahan
brightness_button = tk.Button(correction_box, text='Peningkatan Kecerahan', command=lambda: process_image('brightness'))
brightness_button.pack(side=tk.LEFT, padx=5)

# tombol untuk perbaikan metode sharpening (penajaman)
sharpening_button = tk.Button(correction_box, text='Penajaman', command=lambda: process_image('sharpening'))
sharpening_button.pack(side=tk.LEFT, padx=5)

# Menambahkan kotak untuk informasi creator
creator_box = tk.LabelFrame(root, text='Creator', padx=3, pady=3)
creator_box.place(x=800, y=30, width=430, height=80)

# Menampilkan informasi pembuat program
show_creator()

# Menjalankan program
root.mainloop()