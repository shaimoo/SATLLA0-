from PIL import Image

import os

input_image_path = '/home/satlla0/Desktop/scripts/0.jpg'


original_image = Image.open(input_image_path)

compression_level = 50

compresssd_image_path = '/home/satlla0/Desktop/scripts/0.jpg'

original_image.save(compresssd_image_path,optimize = True, quality = compression_level)





