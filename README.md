# Image to Enhanced Pencil Sketch Converter

This project converts images into enhanced pencil sketches using OpenCV and Tkinter. The application provides a user-friendly interface for selecting an image, applying various filters and transformations, and saving the final pencil sketch to your computer.

### Original Images

![Original Image 1](Vagabond_(manga)_vol._1.png)  


### Converted Pencil Sketches

![Pencil Sketch 1](Vagabond_(manga)_vol._1_enhanced_pencil_sketch.jpg)  


## Features

- **Image Enlargement**: Enhances image quality by enlarging it by 150%.
- **Contrast Enhancement**: Uses CLAHE (Contrast Limited Adaptive Histogram Equalization) to improve contrast.
- **Edge Detection**: Applies edge detection using the Canny algorithm and Laplacian filter for sharper details.
- **Noise Reduction**: Utilizes Gaussian and median blurring techniques to reduce image noise.
- **User Interface**: Provides a simple and intuitive GUI for selecting images and saving the resulting sketches.

## Technologies Used

- Python 3
- OpenCV
- Tkinter
- NumPy

## Getting Started

### Prerequisites

- Python 3.x
- Required libraries: Install them using the following command:

  ```bash
  pip install opencv-python numpy
  ```

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/image-to-pencil-sketch.git
   ```
2. Navigate to the project directory:
   ```bash
   cd image-to-pencil-sketch
   ```

### Running the Application

1. Execute the Python script:
   ```bash
   python image_to_pencil_sketch.py
   ```
2. A window will open with a button labeled "Select an image."
3. Click the button and choose an image (`.jpg`, `.jpeg`, or `.png` format).
4. The application will convert the image to an enhanced pencil sketch and save it in the `Output` folder.

### Output Directory

By default, all pencil sketches are saved in:
```
Output/
```

You can modify this path by changing the `output_directory` variable in the script.

## Project Structure

```
image-to-pencil-sketch/
│
├── image_to_pencil_sketch.py   # Main script for the application
└── Output/                     # Directory where output images are saved
```

## How It Works

1. **Select Image**: Use the Tkinter file dialog to select an image.
2. **Processing**: The selected image undergoes several processing steps:
   - Enlarging the image
   - Converting to grayscale
   - Enhancing contrast with CLAHE
   - Edge detection using Canny and Laplacian filters
   - Combining the original and processed image to create the pencil sketch
3. **Saving**: The final sketch is saved to the specified output directory.
