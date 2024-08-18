from PIL import Image, ImageOps
import os

def resize_with_padding(image, target_size, padding_color=(0, 0, 0)):
    """
    Resize the image while keeping the aspect ratio and adding padding.
    
    :param image: PIL.Image object
    :param target_size: Tuple (width, height) for the target size
    :param padding_color: Tuple (R, G, B) color for padding
    :return: Resized and padded image
    """

    # Resize image while keeping aspect ratio
    image.thumbnail(target_size, Image.LANCZOS)
    
    # Calculate padding to add to make the image square
    delta_w = target_size[0] - image.size[0]
    delta_h = target_size[1] - image.size[1]
    padding = (delta_w // 2, delta_h // 2, delta_w - (delta_w // 2), delta_h - (delta_h // 2))
    
    # Add padding
    new_image = ImageOps.expand(image, padding, fill=padding_color)
    return new_image

def resize_images_with_padding(input_dir, output_dir, target_size=(64, 64), padding_color=(0, 0, 0)):
    """
    Resize and pad all images in the input directory, saving them to the output directory.
    
    :param input_dir: Path to input images
    :param output_dir: Path to save resized and padded images
    :param target_size: Target size (width, height) for resizing
    :param padding_color: Color for padding
    """
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Iterate over all files in the input directory
    for filename in os.listdir(input_dir):
        file_path = os.path.join(input_dir, filename)
        
        # Open an image file
        with Image.open(file_path) as img:
            # Resize with padding
            resized_img = resize_with_padding(img, target_size, padding_color)
            
            # Save the resized and padded image to the output directory
            resized_img.save(os.path.join(output_dir, filename))

    print(f"All images have been resized to {target_size} with padding and saved to {output_dir}.")

# Set the input directory, output directory, and target size
input_directory = "./test_set/test_set/dogs"
output_directory = "./test_set/test_set/dogs_test"
target_size = (80, 80)  # Desired size with padding
padding_color = (0, 0, 0)  # Black padding

# Call the function to resize images with padding
resize_images_with_padding(input_directory, output_directory, target_size, padding_color)
