import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image


def encode_message():
    file_path = filedialog.askopenfilename(title="Select Image", filetypes=[("PNG Files", "*.png")])
    if not file_path:
        return

    img = Image.open(file_path)
    message = tk.simpledialog.askstring("Input", "Enter the message to hide:")
    
    if not message:
        messagebox.showerror("Error", "No message entered!")
        return

    message += "####"  
    binary_message = ''.join(format(ord(char), '08b') for char in message)

    img_data = list(img.getdata())
    new_pixels = []
    binary_index = 0

    for pixel in img_data:
        new_pixel = list(pixel)
        for i in range(3):  
            if binary_index < len(binary_message):
                new_pixel[i] = new_pixel[i] & ~1 | int(binary_message[binary_index])
                binary_index += 1
        new_pixels.append(tuple(new_pixel))

    encoded_img = Image.new(img.mode, img.size)
    encoded_img.putdata(new_pixels)

    save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*.png")])
    if save_path:
        encoded_img.save(save_path)
        messagebox.showinfo("Success", "Message encoded and saved successfully!")


def decode_message():
    file_path = filedialog.askopenfilename(title="Select Encoded Image", filetypes=[("PNG Files", "*.png")])
    if not file_path:
        return

    img = Image.open(file_path)
    img_data = list(img.getdata())

    binary_message = ""
    for pixel in img_data:
        for i in range(3):
            binary_message += str(pixel[i] & 1)

    chars = [binary_message[i:i+8] for i in range(0, len(binary_message), 8)]
    decoded_text = ''.join(chr(int(char, 2)) for char in chars)

    if "####" in decoded_text:
        decoded_text = decoded_text[:decoded_text.index("####")]
        messagebox.showinfo("Decoded Message", f"Hidden Message: {decoded_text}")
    else:
        messagebox.showerror("Error", "No hidden message found!")


root = tk.Tk()
root.title("Secure Image Steganography")
root.geometry("400x250")

tk.Label(root, text="Image Steganography", font=("Arial", 14, "bold")).pack(pady=10)
tk.Button(root, text="Encode Message", command=encode_message, width=20).pack(pady=5)
tk.Button(root, text="Decode Message", command=decode_message, width=20).pack(pady=5)
tk.Button(root, text="Exit", command=root.quit, width=20).pack(pady=5)

root.mainloop()
