from pdf2image import convert_from_path
import os

def pdf_to_images(pdf_path, output_folder):
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Convert PDF to a list of images
    images = convert_from_path(pdf_path)

    # Save each image in the output folder
    for i, image in enumerate(images):
        image_path = os.path.join(output_folder, f'page_{i + 1}.png')
        image.save(image_path, 'PNG')
        print(f'Saved {image_path}')

# Example usage
pdf_path = 'data/menu1.pdf'  # Path to the PDF file
output_folder = 'output/menu1/output_images'  # Folder to save images

pdf_to_images(pdf_path, output_folder)
