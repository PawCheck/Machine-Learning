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
def organize_images(annotations, images_dir):
    # Clean the data
    annotations = clean_annotations(annotations)

    if annotations is None:
        print("Annotation data is empty or invalid.")
        return

    # Group by class
    class_groups = annotations.groupby('class')

    for class_name, group in class_groups:
        # Create class folder if it doesn't exist
        class_dir = os.path.join(images_dir, class_name)
        if not os.path.exists(class_dir):
            os.makedirs(class_dir)

        # Move all images to the class subfolder
        for _, row in group.iterrows():
            filename = row['filename']
            src = os.path.join(images_dir, filename)

            # Ensure the file exists in the source folder
            if os.path.exists(src):
                # Create a new name by adding the class to the filename
                new_filename = f"{class_name}_{filename}"

                dst = os.path.join(class_dir, new_filename)
                shutil.move(src, dst)
            else:
                print(f"File not found: {src}")

        print(f"Image organization for class '{class_name}' completed.")

# Continue with image organization if file is found
if train_annotations is not None:
    print("Image organization for 'train' dataset.")
    organize_images(train_annotations, train_dir)

if valid_annotations is not None:
    print("Image organization for 'valid' dataset.")
    organize_images(valid_annotations, valid_dir)

if test_annotations is not None:
    print("Image organization for 'test' dataset.")
    organize_images(test_annotations, test_dir)

# Final output
print("All datasets have been successfully organized!")