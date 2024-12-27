from PIL import Image

# Open the TIFF image
image_path = 'C:/Users/Sunny/Downloads/at3_1m4_01.tif'  # Replace with the actual path to your TIFF file
img = Image.open(image_path)

# Display the image
img.show()
