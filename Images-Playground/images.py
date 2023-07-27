from PIL import Image, ImageFilter

# @see https://pillow.readthedocs.io/en/stable/

img = Image.open('./Pokedex/pikachu.jpg')
# print(img.format)
# print(img.size)
# print(img.mode)

# Add filter to the image.
filtered_img = img.filter(ImageFilter.BLUR)
# save the image with the new effects.
# filtered_img.save('blur-pikachu.png', 'png')

# Convert the image - greyscale.
converted_img = img.convert('L')
# converted_img.save('grey-pikachu.png', 'png')

# Show the image - it opens the image in the default image viewer.
# converted_img.show()

# Rotate image.
crooked = converted_img.rotate(90)
# crooked.save('rotated-pikachu.png', 'png')

# Resize image.
resize = img.resize((300, 300))
# resize.save('resized-pikachu.png', 'png')

# Crop image.
# box = (100, 100, 400, 400)
## region = converted_img.crop(box)
## region.save('cropped-pikachu.png', 'png')

astro = Image.open('./astronaut.jpg')
# Create a thumbnail.
astro.thumbnail((400, 400))
astro.save('thumbnail.jpg')
print(astro.size)
