import os
from PIL import Image
from tqdm import tqdm

def convert_folder_png_to_jpeg(input_folder, output_folder):
    # Check if the output folder exists, create it if it doesn't
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop through all files in the input folder
    for filename in tqdm(os.listdir(input_folder)):
        if filename.endswith(".png"):
            # Construct full file path
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + '.jpeg')
            
            # Open the image
            image = Image.open(input_path)
            
            # Convert the image to RGB mode in case it's in RGBA or another mode
            if image.mode in ('RGBA', 'LA') or (image.mode == 'P' and 'transparency' in image.info):
                image = image.convert('RGB')
            
            # Save the image in JPEG format
            image.save(output_path, 'JPEG')

# Example usage
input_folder = 'blur2blur/qualitative/REDS'
output_folder = 'blur2blur/qualitative/REDS'

convert_folder_png_to_jpeg(input_folder, output_folder)

