## C242-PS340<br/> 
* M323B4KY4241 – Syafa’at Ramadhan
* M323B4KX0451 – Amanda Betania Maritza
* M323B4KX0573 – Annisa Airinadita
* C777B4NY113D – Dika Zulhidayat
* C323B4KX0265 – Aisyah Nabila Rahmawati
* A323B4KY1151 – Dimaz Anugrahman Yusuf
* A437B4KY2980 – Muhammad Nurfadhli
<br>

# PawCheck
In Indonesia, eye disorders rank among the top health concerns affecting dogs, with a considerable percentage resulting in vision impairment or blindness if not appropriately addressed. The 2023 Intage Group U&A Survey on Dog and Cat Owners highlighted that dogs are increasingly popular pets in Indonesia, with an ownership rate of 7.4% in households. This growing popularity reflects a heightened awareness of pet health, although eye health issues in dogs remain prevalent. Factors such as congenital problems, infections, degeneration, parasites, and inadequate nutrition can lead to these disorders.  Ophthalmic examinations play a critical role in the early detection of systemic disorders, particularly those impacting the vascular and nervous systems. To tackle these challenges, we have developed an app that leverages advanced technology to aid dog owners in monitoring and maintaining their pets' eye health. The app facilitates early detection of eye diseases through photo analysis and offers tailored care recommendations based on the specific conditions identified. Our goal is to bridge the existing gap in pet healthcare services and promote healthier, happier lives for dogs.

## Features

- **AI-powered eye disease detection**: Detects common eye diseases in dogs through image analysis.
- **Actionable health recommendations**: Provides tailored care suggestions based on the detected condition.
- **User-friendly interface**: Simple navigation for easy use by dog owners with no technical background.
- **Offline support**: Access to the app is available even without an internet connection.

## Requirements

- **Android device** (version 6.0 or higher)
- **Internet connection** for uploading photos and receiving recommendations
- **Firebase** account for cloud storage and app management
<br>

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Technologies](#technologies)
- [Machine Learning Model](#machine-learning-model)
- [License](#license)
<br>

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/pawcheck.git

2. Navigate to the project directory:
   ```bash
   cd pawcheck
3. Set up the Android development environment:
    * Install Android Studio
    * Ensure you have the required SDKs and dependencies installed as per the Android development guidelines.
4. Install the necessary Python dependencies for training the model:
   pip install -r requirements.txt
5. Prepare your dataset by following the instructions in the data/ folder to format and label images properly.
6. Train the custom machine learning model using TensorFlow:
   * Navigate to the model/ directory.
   * Run the script to train the model:
      ```bash
      python Model.py
7. Save the model to h5 for API.
8. Convert the model to TensorFlow Lite for mobile app integration.
<br>

## Usage
1. Launch the app on your Android device.
2. Upload or take a picture of your dog's eyes.
3. The app will analyze the image and provide a diagnosis of potential eye diseases.
4. Follow the recommended steps provided by the app for treatment or further consultation with a veterinarian.
<br>

## Technologies
* <b>Android Development:</b> Kotlin, Jetpack Compose
* <b>Machine Learning:</b> TensorFlow, TensorFlow Lite
* <b>Backend:</b> Node.js, Express.js
* <b>Database:</b> Firebase, Firestore
* <b>Cloud:</b> Google Cloud Run
* <b>Version Control:</b> Git
<br>

## Machine Learning Model
The machine learning model is trained using a custom dataset of labeled images of dog eye conditions. Unlike pre-trained models, we developed a custom model to ensure higher accuracy, particularly due to the specific nature of the dataset. The model performs image classification to detect various eye diseases in dogs.

## Model Training Steps:
* Image preprocessing (resize, normalize, augment)
* Model architecture: Custom CNN (Convolutional Neural Network)
* Training with the dataset
* Model conversion to TensorFlow Lite for mobile deployment
<br>

## Liciense
