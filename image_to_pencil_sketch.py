import cv2
import tkinter as tk
from tkinter import filedialog, messagebox
import os
import numpy as np

# Default output path
output_directory = "Output/"

def enhanced_image_to_pencil_sketch(image_path, output_path):
    # Read the image
    image = cv2.imread(image_path)
    
    # Enlarge the image for better quality
    scale_percent = 150  # Increase the image size by 150%
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized_image = cv2.resize(image, dim, interpolation=cv2.INTER_LINEAR)

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
    
    # Apply CLAHE (Contrast Limited Adaptive Histogram Equalization) to enhance contrast
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    enhanced_gray_image = clahe.apply(gray_image)
    
    # Invert the enhanced grayscale image
    inverted_gray_image = 255 - enhanced_gray_image
    
    # Apply a stronger Gaussian blur
    blurred_image = cv2.GaussianBlur(inverted_gray_image, (25, 25), sigmaX=0, sigmaY=0)
    
    # Apply median blur to reduce noise
    median_blurred = cv2.medianBlur(blurred_image, 11)
    
    # Apply edge detection using the Canny algorithm
    edges = cv2.Canny(median_blurred, threshold1=200, threshold2=200)
    
    # Apply Laplacian filter to enhance edges
    laplacian = cv2.Laplacian(edges, cv2.CV_8U)
    inverted_laplacian = cv2.bitwise_not(laplacian)

    # Combine edges with the original image
    pencil_sketch = cv2.divide(enhanced_gray_image, inverted_laplacian, scale=256.0)

    # Save the resulting image
    cv2.imwrite(output_path, pencil_sketch)
    messagebox.showinfo("Success", f"Enhanced pencil sketch saved at: {output_path}")

def select_image():
    # Open a dialog to select an image
    image_path = filedialog.askopenfilename(title="Select an image", 
                                            filetypes=[("Image files", "*.jpg *.jpeg *.png")])
    
    if image_path:
        # Create the output directory if it doesn't exist
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)
        
        # Define the output filename
        output_filename = os.path.splitext(os.path.basename(image_path))[0] + "_enhanced_pencil_sketch.jpg"
        output_path = os.path.join(output_directory, output_filename)
        
        # Convert the image to an enhanced pencil sketch
        enhanced_image_to_pencil_sketch(image_path, output_path)

# Create the main user interface
root = tk.Tk()
root.title("Image to Enhanced Pencil Sketch Converter")
root.geometry("400x200")

# Add a button to select the image
select_button = tk.Button(root, text="Select an image", command=select_image, font=("Arial", 14))
select_button.pack(pady=40)

# Run the application
root.mainloop()
