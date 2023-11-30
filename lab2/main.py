import tkinter as tk
from tkinter import filedialog
import numpy as np
import cv2
import os

def highquality_filter(img):
    kernel = np.array([[0, -1, 0],
                        [-1, 4, -1],
                        [0, -1, 0]])
    result = cv2.filter2D(img, -1, kernel)
    return result

def dilate(img):
    kernel = np.ones((3, 3))
    result = cv2.dilate(img, kernel=kernel, iterations=1)
    return result

def select_input_directory():
    input_directory = filedialog.askdirectory(title="Select Input Directory")
    input_entry.delete(0, tk.END)
    input_entry.insert(0, input_directory)

def select_output_directory():
    output_directory = filedialog.askdirectory(title="Select Output Directory")
    output_entry.delete(0, tk.END)
    output_entry.insert(0, output_directory)

def process_images():
    input_directory = input_entry.get()
    output_directory = output_entry.get()
    methods = [highquality_filter, dilate]
    for method in methods:
        method_output_directory = os.path.join(output_directory, method.__name__)
        os.makedirs(method_output_directory, exist_ok=True)
        image_files = os.listdir(input_directory)
        for image_file in image_files:
            if image_file.endswith('.png') or image_file.endswith('.jpg') or image_file.endswith('.jpeg'):
                image_path = os.path.join(input_directory, image_file)
                image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
                processed_image = method(image)
                output_image_path = os.path.join(method_output_directory, image_file)
                cv2.imwrite(output_image_path, processed_image)

root = tk.Tk()

button1 = tk.Button(root, text="Select Input Directory", command=select_input_directory)
button1.pack()
input_entry = tk.Entry(root)
input_entry.pack()
button2 = tk.Button(root, text="Select Output Directory", command=select_output_directory)
button2.pack()
output_entry = tk.Entry(root)
output_entry.pack()
button3 = tk.Button(root, text="Process Images", command=process_images)
button3.pack()

root.mainloop()