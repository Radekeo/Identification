import easyocr
from helpers import nigeria

# read image file
IMAGE_PATH = 'samplepassport.jpg'

# extract text from image
reader = easyocr.Reader(['en'], gpu=False)
result = reader.readtext(IMAGE_PATH)
# print(result)

# store useful values extracted from image in lists
places = []
strr = []

for value in result:
    if value[1] in nigeria:     # get values that have Nigerian states or cities
        places.append(value[1])
    elif '<' in value[1]:       # get values at the bottom of the image
        strr.append(value[1])