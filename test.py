import cv2
import numpy as np
import os

def load_images_from_folder(folder):
    images = []
    filenames = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder, filename))
        if img is not None:
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            images.append(gray)
            filenames.append(filename)
    return images, filenames

def calculate_similarity(img1, img2):
    img1 = cv2.resize(img1, (100, 100))
    img2 = cv2.resize(img2, (100, 100))
    diff = cv2.absdiff(img1, img2)
    similarity = 1 - (np.sum(diff) / (img1.shape[0] * img1.shape[1] * 255))
    return similarity

def find_best_match(input_image_path, processed_folder):
    input_image = cv2.imread(input_image_path, cv2.IMREAD_GRAYSCALE)
    if input_image is None:
        print("Error: Input image not found.")
        return None

    processed_images, filenames = load_images_from_folder(processed_folder)
    best_match = None
    best_similarity = -1
    for i, processed_image in enumerate(processed_images):
        similarity = calculate_similarity(input_image, processed_image)
        if similarity > best_similarity:
            best_similarity = similarity
            best_match = filenames[i]

    print(f"Best match: {best_match}")
    return best_match

# Path
#input_image_path = r"C:/Users/Admin/Downloads/Face-Recognition-System/1.jpg"
input_image_path = input("Enter the path to your input image: ")
processed_folder = r"C:/Users/Admin/Downloads/Face-Recognition-System/images"  # Folder containing the dataset

# Find the best match
find_best_match(input_image_path, processed_folder)
