# secure-data-hiding-in-images-using-steganography
Existing communication methods often expose messages to security risks, including interception, unauthorized access, and cyber threats. While encryption protects data, encrypted messages are easily noticeable, potentially leading to further scrutiny or decryption attempts. 
Secure Image Steganography Tool
This is a simple Python-based GUI application for encoding and decoding messages within images using LSB (Least Significant Bit) Steganography. The tool allows users to hide a message within an image and later retrieve it, ensuring privacy.

Features
Encode Message: Hide a message inside an image file.
Decode Message: Extract and display the hidden message from an encoded image.
Simple User Interface: Built with Tkinter for a user-friendly GUI.
Supports PNG Files: Only PNG images are supported for encoding and decoding.

Requirements
Python 3.x
PIL (Pillow) library for image processing
tkinter library for GUI (usually comes pre-installed with Python)
To install the required libraries:
bash
Copy
Edit
pip install pillow

How to Use
1. Encoding a Message:
Click on the "Encode Message" button.
Select an image (PNG file) from your file explorer.
Enter the message you want to hide in the image.
The tool will encode the message and save the modified image to your desired location.
2. Decoding a Message:
Click on the "Decode Message" button.
Select an encoded image (PNG file).
The tool will extract the hidden message and display it in a pop-up window.
3. Exit:
Click on the "Exit" button to close the application.

Code Explanation
Encoding Process:
The user selects an image, and the tool asks for a message.
The message is converted to a binary format and hidden within the image's least significant bits (LSB) of the pixel values.
The encoded image is then saved as a new file.

Decoding Process:
The user selects an encoded image.
The tool reads the image's pixels and retrieves the hidden binary message from the least significant bits.
The binary message is then converted back to text and displayed.

Example
Original Image: A PNG image with no hidden message.
Encoded Image: The same PNG image with a hidden message in its pixel data (invisible to the human eye).
Decoded Message: The hidden message extracted and displayed in a pop-up window.
