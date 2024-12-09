import os
import pandas as pd
import shutil

base_path = r'D:\Documents\KULIAH\Semester 5\Studi Independen\Project Capstone\Project\Dataset\Data'

# Path to dataset folders
train_dir = os.path.join(base_path, 'train')
valid_dir = os.path.join(base_path, 'valid')
test_dir = os.path.join(base_path, 'test')

# Function to read CSV only if the file exists
def read_annotations(file_path):
    if os.path.isfile(file_path):
        return pd.read_csv(file_path)
    else:
        print(f"File not found: {file_path}")
        return None

# Read CSV files for each dataset
train_annotations = read_annotations(os.path.join(train_dir, 'cleaned_annotations.csv'))
valid_annotations = read_annotations(os.path.join(valid_dir, 'cleaned_annotations.csv'))
test_annotations = read_annotations(os.path.join(test_dir, 'cleaned_annotations.csv'))

# Function to clean and validate CSV data
def clean_annotations(annotations):
    if annotations is not None:
        # Remove rows with missing values in important columns
        annotations = annotations.dropna(subset=['class', 'filename']).drop_duplicates()
        return annotations
    return None

# Function to create class subfolders and move images
def organize_images(annotations, images_dir, max_images_per_class):
    # Clean the data
    annotations = clean_annotations(annotations)

    if annotations is None:
        print("Annotation data is empty or invalid.")
        return

    # Group by class
    class_groups = annotations.groupby('class')

    for class_name, group in class_groups:
        # Limit the number of images per class
        selected_images = group.sample(min(len(group), max_images_per_class), random_state=42)

        # Create class folder if it doesn't exist
        class_dir = os.path.join(images_dir, class_name)
        not_selected_dir = os.path.join(images_dir, "not_selected", class_name)  # Folder for unselected images
        if not os.path.exists(class_dir):
            os.makedirs(class_dir)
        if not os.path.exists(not_selected_dir):
            os.makedirs(not_selected_dir)

        # Move selected images to the class subfolder
        for _, row in selected_images.iterrows():
            filename = row['filename']
            src = os.path.join(images_dir, filename)

            # Ensure the file exists in the source folder (train)
            if os.path.exists(src):
                # Create a new name by adding the class to the filename
                new_filename = f"{class_name}_{filename}"

                dst = os.path.join(class_dir, new_filename)  # Save with the new name
                shutil.move(src, dst)
            else:
                print(f"File not found: {src}")  # Log for files not found

        # Handle unselected images
        not_selected_images = group[~group['filename'].isin(selected_images['filename'])]

        for _, row in not_selected_images.iterrows():
            filename = row['filename']
            src = os.path.join(images_dir, filename)

            # Ensure the unselected image exists in the source folder
            if os.path.exists(src):
                # Create a new name for unselected images
                new_filename = f"{class_name}_{filename}"

                # Move unselected images to the 'not_selected' folder
                dst = os.path.join(not_selected_dir, new_filename)
                shutil.copy(src, dst)  # Copy the file to the 'not_selected' folder
            else:
                print(f"File not found: {src}")  # Log for files not found

        print(f"Image organization for class '{class_name}' completed.")

# Continue with image organization if file is found
if train_annotations is not None:
    print("Starting image organization for 'train' dataset...")
    organize_images(train_annotations, train_dir, max_images_per_class=200)

if valid_annotations is not None:
    print("Starting image organization for 'valid' dataset...")
    organize_images(valid_annotations, valid_dir, max_images_per_class=40)

if test_annotations is not None:
    print("Starting image organization for 'test' dataset...")
    organize_images(test_annotations, test_dir, max_images_per_class=10)

# Final output
print("All datasets have been successfully organized!")