import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np

# Load the saved model
model = tf.keras.models.load_model('image_classifier.h5')

# Class labels in the same order as during training
class_labels = ['cataract', 'glaucoma', 'normal']  # Update as per your training

# Function to predict the class of a new image
def classify_image(img_path):
    try:
        # Load and preprocess image
        img = image.load_img(img_path, target_size=(150, 150))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
        img_array /= 255.0  # Normalize pixel values

        # Predict
        predictions = model.predict(img_array)
        predicted_class = np.argmax(predictions, axis=1)
        predicted_label = class_labels[predicted_class[0]]

        print(f"The image is classified as: {predicted_label}")
    except Exception as e:
        print(f"Error processing image: {e}")

# Example usage
new_image_path = "C:\\Users\\VATHSALYA\\OneDrive\\Documents\\college\\Hackathon\\Porjectfest\\retinal-disease-ai\\models\\data set\\training\\normal\\1034_left.jpg"
classify_image(new_image_path)  
