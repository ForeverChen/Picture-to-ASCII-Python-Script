'''
Author:		Joshua Twigg
Date:		October 17, 2014
Program:	Picture to ASCII
Purpose:	Take a picture and convert each pixel to an ascii character.  Save the 
		file as a text document that will display the picture in text format.
'''

from PIL import Image
from PIL import ImageEnhance
import math

# Prompt user to input image
print('\n\nPicture to ASCII\n')
file_name = raw_input('Enter the name of the image (including the extension): ')

# Open image
picture = Image.open(file_name)

# Adjust contrast
c = raw_input('Enter a number 0.5-4.0 to adjust contrast (default is 1.0): ')
picture = ImageEnhance.Contrast(picture)
picture = picture.enhance(float(c))

# Determine image resolution
(w,h) = picture.size

# Resize image to a width of 150 pixels while keeping height to width ratio
if w < h:
	width = 150.0
else:
	width = 250.0
height = int(math.floor(((width/w) * h)/1.8))	# This formula adjusts the height to match the width.  It is not always
width = int(width)				#	accurate for odd-shaped pictures, but it mostly works well.
picture = picture.resize((width,height),Image.ANTIALIAS)

# Convert image to gray scale
picture = picture.convert('L')

# Create matrix containing value for each pixel
pixels = picture.load()

# Create character array for ASCII pixel representations
char = ['M','@','%','0','&','o','=','+','?','}',')','*','\'','-','`',' ']

# Scan each pixel and assign an ASCII character based on darkness
with open(file_name[:-4] + ".txt","w") as text:
	for y in range(height):
		for x in range(width):
			text.write(char[int(math.floor((pixels[x,y]/256.0)*16.0))])
		text.write("\n")
