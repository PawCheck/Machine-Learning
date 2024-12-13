# Machine Learning Model
The machine learning model is trained using a custom dataset of labeled images of dog eye conditions. Unlike pre-trained models, we developed a custom model to ensure higher accuracy, particularly due to the specific nature of the dataset. The model performs image classification to detect various eye diseases in dogs.

## Key Features of the Machine Learning Model
* Custom model: Built to handle the specific nature of the dog eye disease dataset for improved accuracy.
* Image classification: Detects common eye diseases like Blepharitis, Conjunctivitis, Entropion, etc.
* TensorFlow Lite: Optimized for mobile integration to ensure real-time predictions on Android devices.

## Model Architecture
* CNN (Convolutional Neural Network): The model uses multiple convolutional layers to extract features from dog eye images, followed by fully connected layers for classification.
* Preprocessing: Images are resized, normalized, and augmented to improve generalization and accuracy during training.

## Key Steps in Training:
1. Image Preprocessing: Includes resizing images to a standard size, normalization, and augmentation (such as rotation, flipping) to improve model robustness.
2. Custom CNN Architecture: The model uses a deep CNN to extract features relevant to eye disease detection. It consists of multiple convolutional layers followed by pooling and dense layers.
3. Training: The model is trained using the prepared dataset, with hyperparameter tuning to optimize performance.
4. Evaluation: Accuracy and loss are evaluated during training and validation phases to ensure the model is generalizing well to unseen data.

## Machine Learning Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Machine-Learning.git
2. Navigate to the project directory:
   ```bash
   cd pawcheck
3. Install the necessary Python dependencies for training the model:
   pip install -r requirements.txt
4. Prepare your dataset by following the instructions in the data/ folder to format and label images properly.
5. Train the custom machine learning model using TensorFlow:
   * Navigate to the model/ directory.
   * Run the script to train the model:
      ```bash
      python Model.py
6. Save the model to h5 for API.
7. Convert the model to TensorFlow Lite for mobile app integration.
<br>

## Machine Learning Team<br/> 
* M323B4KY4241 – Syafa’at Ramadhan
* M323B4KX0451 – Amanda Betania Maritza
* M323B4KX0573 – Annisa Airinadita
