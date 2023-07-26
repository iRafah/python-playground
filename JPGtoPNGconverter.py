import sys
import os
from PIL import Image
from pathlib import Path

# Command example:
# python3 .\JPGtoPNGconverter.py Pokedex\ Converter\


def create_folder(folder_name):
    current_path = os.getcwd()
    ## os.chdir(os.path.join(path, origin_folder_path))
    full_path = os.path.join(current_path, folder_name)

    os.makedirs(full_path, exist_ok=True)


# Grab first and second argument (directories).
origin_folder_path = sys.argv[1]
destiny_folder_path = sys.argv[2]

# Check if they exist - if not, create them.
create_folder(origin_folder_path)
create_folder(destiny_folder_path)

# Loop through Pokedex (or main directory).
for file in os.listdir(origin_folder_path):
    img = Image.open(f'{origin_folder_path}{file}')

    clean_name = os.path.splitext(file)[0]
    # Convert images to PNG and save them in the new folder.
    img.save(f'{destiny_folder_path}{clean_name}.png', 'png')
    print('The image was converted from JPG to PNG')
