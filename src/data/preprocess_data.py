import os
import sys
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
import config



def process_image(image):
    """
    Preprocesses an image by converting it to float32 and normalizing its values between 0 and 1.

    Args:
        image: A numpy array representing the image.

    Returns:
        The preprocessed image as a numpy array.
    """
    image = image.astype('float32')
    image = image / 255.0
    image = tf.cast(image, dtype=tf.float32)
    return image


def image_to_tensor(image, is_real: bool):
    """
    Convert an image to a tensor by flattening the image and concatenating it with a constant tensor.

    Args:
        image: The input image.
        is_real: A boolean value indicating whether the image is real or not.

    Returns:
        tensor_image: The tensor representation of the image, obtained by flattening the image and concatenating it with a constant tensor.
    """
    flatten_image = tf.reshape(image, (-1,))
    constant_tensor = tf.constant([float(is_real)], dtype=tf.float32)
    tensor_image = tf.concat([flatten_image, constant_tensor], axis=0)
    return tensor_image


def stack_tensors(folder_path, is_real):
    """
    Stack tensors from images in a folder.

    Args:
        folder_path (str): Path to the folder containing the images.
        is_real (bool): Flag indicating whether the images are real or not.

    Returns:
        tf.Tensor: Stacked tensor of processed images.

    Raises:
        FileNotFoundError: If the folder_path does not exist.
    """
    list_tensors = []
    for image_name in os.listdir(folder_path):
        image_path = os.path.join(folder_path, image_name)
        image = plt.imread(image_path)
        processed_image = process_image(image)
        tensor = image_to_tensor(processed_image, is_real=is_real)
        list_tensors.append(tensor)
    return tf.stack(list_tensors, axis=0)


def save_tensor_csv(stack_tensors, save_path):
    """
    Save a stack of tensors as a CSV file.

    Args:
        stack_tensors (torch.Tensor): The stack of tensors to be saved.
        save_path (str): The path where the CSV file will be saved.

    Returns:
        None
    """
    np_array = stack_tensors.numpy()
    np.savetxt(save_path, np_array, delimiter=',')


def main():
    for key, value in zip(config.images_path.keys(), config.images_path.values()):
        tensors = stack_tensors(value[1], value[0])
        save_tensor_csv(tensors, config.datasets[key])






if __name__ == '__main__':
    main()