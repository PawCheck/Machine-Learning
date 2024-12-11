from sklearn.preprocessing import StandardScaler, LabelEncoder
import os
import pandas as pd

# Function to clean the dataset
def clean_dataset(df):
    # Normalize/Standardize
    scaler = StandardScaler()
    df[['width', 'height']] = scaler.fit_transform(df[['width', 'height']])

    # Encode categories
    label_encoder = LabelEncoder()
    df['class'] = label_encoder.fit_transform(df['class'])

    return df

cleaned_datasets = {}
base_path = r'D:\Documents\KULIAH\Semester 5\Studi Independen\Project Capstone\Project\Dataset\Data'
folders = ['train', 'test', 'valid']

for folder in folders:
    folder_path = os.path.join(base_path, folder)
    file_path = os.path.join(folder_path, 'cleaned_annotations.csv')
    if os.path.isfile(file_path):
        print(f"Processing file: {file_path}")

        # Read the CSV file
        df = pd.read_csv(file_path)

        # Apply dataset cleaning
        cleaned_df = clean_dataset(df)
        print(f"Dataset in folder '{folder}' has been successfully cleaned.")

        # Save the cleaned dataset
        cleaned_datasets[folder] = cleaned_df
    else:
        print(f"File {file_path} not found. Skipping.")

print("All folders have been processed!")