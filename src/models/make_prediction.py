
import os
import sys
import tensorflow as tf
import matplotlib.pyplot as plt

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
import config



def process_and_resize_image(image, target_size=(32, 32)):
    """
    Process and resize an image.

    Parameters:
    - image: numpy.ndarray
        The input image to be processed and resized.
    - target_size: tuple, optional
        The target size of the resized image. Default is (32, 32).

    Returns:
    - numpy.ndarray
        The processed and resized image.
    """
    image = image.astype('float32') / 255.0
    image = tf.image.resize(image, target_size)
    image = tf.cast(image, dtype=tf.float32)
    return image


def prepare_image_for_model(image):
    """
    Prepares an image for model prediction.

    Args:
        image: The input image to be processed.

    Returns:
        processed_image: The processed image ready for model prediction.
    """
    processed_image = process_and_resize_image(image)
    processed_image = tf.expand_dims(processed_image, axis=0)
    return processed_image


def load_model(model_path=config.model_path):
    """
    Load a Keras model from the given model_path.

    Parameters:
        model_path (str): The path to the saved Keras model.

    Returns:
        model (tf.keras.Model): The loaded Keras model.
    """
    model = tf.keras.models.load_model(model_path)
    return model


def make_prediction(image_path):
    """
    Makes a prediction using a trained model.

    Args:
        image_path (str): The path to the image file.

    Returns:
        int: The predicted class label. 1 for real, 0 for fake.
    """
    model = load_model()
    image = plt.imread(image_path)
    processed_image = prepare_image_for_model(image)
    prediction = model.predict(processed_image)
    return (prediction > config.model_prams['threshold']).astype(int)[0][0]





if __name__ == '__main__':
    image_path = "PUT THE PATH TO THE IMAGE YOU WANT TO PREDICT HERE"
    prediction = make_prediction(image_path)
    pred_class = "Real" if prediction == 1 else "Fake"
    print(f"The predicted class label is: {pred_class}")