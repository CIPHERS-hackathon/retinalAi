import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np

# Load the saved model
model = tf.keras.models.load_model('image_classifier.h5')

# Function to predict the class of a new image
def classify_image(img_path):
    # Load the image and resize it to the target size
    img = image.load_img(img_path, target_size=(150, 150))
    
    # Convert the image to a numpy array and scale the pixel values
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    img_array = img_array / 255.0  # Normalize the pixel values
    
    # Predict the class
    predictions = model.predict(img_array)
    
    # Get the class with the highest probability
    predicted_class = np.argmax(predictions, axis=1)
    
    # Get the class label based on the index
    class_labels = list(train_generator.class_indices.keys())
    
    # Output the predicted class label
    predicted_label = class_labels[predicted_class[0]]
    print(f"The image is classified as: {predicted_label}")
    
# Example usage: Classifying a new image
new_image_path = '/home/steve-allan-paul/Documents/data set/normal/8_left.jpg'
classify_image(new_image_path)
