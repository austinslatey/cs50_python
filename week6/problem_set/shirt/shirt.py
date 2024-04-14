import sys
import os.path
from PIL import Image, ImageOps

def overlay_shirt(input_filename, output_filename):
    # Check if the input file exists
    if not os.path.exists(input_filename):
        sys.exit("Input does not exist")

    # Check if the input and output file extensions are the same
    input_ext = os.path.splitext(input_filename)[1].lower()
    output_ext = os.path.splitext(output_filename)[1].lower()
    if input_ext != output_ext:
        sys.exit("Input and output have different file extensions")

    # Open the input image
    input_image = Image.open(input_filename)

    # Open the shirt image with a transparent background
    shirt = Image.open("shirt.png")

    # Resize and crop the input image to the same size as the shirt image
    input_image_resized = ImageOps.fit(input_image, shirt.size)

    # Overlay the shirt on the input image
    input_image_resized.paste(shirt, (0, 0), shirt)

    # Save the results as the output image
    input_image_resized.save(output_filename)
def main():
    # Check if the num of command-line arguments is correct
    if len(sys.argv)!= 3:
        sys.exit("Too few command-line arguments")

    # Extract the input and output filenames from the command-line arguments
    input_filename = sys.argv[1]
    output_filename = sys.argv[2]

    # Check if the filenames end with.jpg,.jpeg, or.png
    valid_extensions = [".jpg", ".jpeg", ".png"]
    if not input_filename.lower().endswith(tuple(valid_extensions)) or not output_filename.lower().endswith(tuple(valid_extensions)):
        sys.exit("Input and output have different file extensions")

    # Call the overlay_shirt function to overlay the shirt on the input image
    overlay_shirt(input_filename, output_filename)



if __name__ == "__main__":
    main()
