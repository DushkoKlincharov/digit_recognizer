from PIL import Image
import PIL.ImageOps
import numpy as np
from scipy import ndimage

def convert():
    img = Image.open('image.png')
    img = PIL.ImageOps.invert(PIL.ImageOps.grayscale(img))
    img = img.resize((20, 20), PIL.Image.ANTIALIAS)
    img.save('image.png') 
    arr = np.array(img)
    x, y = ndimage.measurements.center_of_mass(arr)
    x = int(round(x))
    y = int(round(y))
    new_img = Image.new('P', (28,28), (0))
    offset = (14 - y, 14 - x)
    new_img.paste(img, offset)
    new_img.save('image.png')

if __name__ == "__main__":
    convert()