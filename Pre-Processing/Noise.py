import os
import cv2
import numpy as np
from tqdm import tqdm

# Path dataset
base_path_train = r'D:\Documents\KULIAH\Semester 5\Studi Independen\Project Capstone\Project\Dataset\Data\train'
base_path_test = r'D:\Documents\KULIAH\Semester 5\Studi Independen\Project Capstone\Project\Dataset\Data\test'
base_path_valid = r'D:\Documents\KULIAH\Semester 5\Studi Independen\Project Capstone\Project\Dataset\Data\valid'

# Output path to save the processed image
output_base_train = r'D:\Documents\KULIAH\Semester 5\Studi Independen\Project Capstone\Project\Dataset\Data\train'
output_base_test = r'D:\Documents\KULIAH\Semester 5\Studi Independen\Project Capstone\Project\Dataset\Data\test'
output_base_valid = r'D:\Documents\KULIAH\Semester 5\Studi Independen\Project Capstone\Project\Dataset\Data\valid'

# Ensure output directory exists
def ensure_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

# Processing images
def process_image(image_path):
    img = cv2.imread(image_path)

    # Removing noise with Gaussian Blur
    denoised_img = cv2.GaussianBlur(img, (5, 5), 0)

    # Convert to YUV color space for brightness improvement
    yuv_img = cv2.cvtColor(denoised_img, cv2.COLOR_BGR2YUV)

    # Check brightness level
    avg_brightness = np.mean(yuv_img[:, :, 0])  # Channel Y

    # If the average brightness is low, use CLAHE.
    if avg_brightness < 120:
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        yuv_img[:, :, 0] = clahe.apply(yuv_img[:, :, 0])

    # Convert back to BGR color space
    processed_img = cv2.cvtColor(yuv_img, cv2.COLOR_YUV2BGR)
    return processed_img

# Processing datasets
def process_dataset(input_base_path, output_base_path):
    for root, dirs, files in os.walk(input_base_path):
        for file in tqdm(files, desc=f"Processing {root.split('/')[-1]}"):
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                input_path = os.path.join(root, file)
                relative_path = os.path.relpath(input_path, input_base_path)
                output_path = os.path.join(output_base_path, relative_path)

                # Make sure the output directory exists
                ensure_dir(os.path.dirname(output_path))

                # Image process
                processed_img = process_image(input_path)

                # Save the processed image
                cv2.imwrite(output_path, processed_img)

# Processing train, test, and valid datasets
process_dataset(base_path_train, output_base_train)
process_dataset(base_path_test, output_base_test)
process_dataset(base_path_valid, output_base_valid)
