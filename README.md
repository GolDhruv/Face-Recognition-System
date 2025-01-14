# Face-Recognition-System
A face recognition system developed using CNN and data science techniques for real-time applications.

This project is a simple Python-based face recognition system to find the best match for an input image from a folder of sample images.

## Project Structure
- images/ # Folder containing sample images for comparison 
- test.py # Python script for finding the best match 


## Requirements
- Python 3.7 or above
- Required libraries: OpenCV, NumPy  
  Install them using: pip install opencv-python numpy


## Usage
1. Add sample images to the `images/` folder.
2. Run the script using:
3. Enter the full path to your input image when prompted:
4. Enter the path to your input image: C:/path/to/your/image.jpg
5. The program will process the images and output the best match from the `images/` folder.

## Key Features
- Compares grayscale versions of the images.
- Automatically resizes images to 100x100 for uniformity.
- Outputs the filename of the best-matching image.

## Notes
- Ensure the input image and sample images are of comparable quality and resolution for better results.
- Tested with basic image datasets.
