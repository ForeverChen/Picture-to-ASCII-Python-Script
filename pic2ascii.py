'''
Author:		Joshua M. Twigg
Date:		October 17, 2014
Program:	Picture to ASCII
Purpose:	Take a picture and convert each pixel to an ascii character.  Save the 
		file as a text document that will display the picture in text format.
Notes:		This script is heavily commented to provide clarification for anyone
		looking to write their own script or edit this one.
'''

from PIL import Image
from PIL import ImageEnhance
import math

# Prompt user to input image
print('\n\nPicture to ASCII\n')
file_name = raw_input('Enter the name of the image (including the extension): ')

# Open image
picture = Image.open(file_name)

# Prompt user to input contrast adjustment
c = raw_input('Enter a number 0.5-4.0 to adjust contrast (default is 1.0): ')

# These next two lines will take the value input by the user and adjust the contrast accordingly
# A number greater than 1.0 will increase the contrast, while a number less will decrease it
picture = ImageEnhance.Contrast(picture)
picture = picture.enhance(float(c))

# Determine image resolution
(w,h) = picture.size

# Resize image to an appropriate width while keeping the height-to-width ratio
if w < h: # If the image is in portrait mode
	width = 150.0
else:	  # Else, the image is in landscape mode
	width = 250.0
height = int(math.floor(((width/w) * h)/1.8))	# This formula adjusts the height to match the width.  It is not always
width = int(width)				#	accurate for odd-shaped pictures, but it works well for most.
picture = picture.resize((width,height),Image.ANTIALIAS)

# Convert image to gray scale.
picture = picture.convert('L')

# Create matrix containing value for each pixel
pixels = picture.load()

# Create character array for ASCII pixel representations
char = ['M','@','%','0','&','o','=','+','?','}',')','*','\'','-','`',' ']

# Scan each pixel and assign an ASCII character based on pixel brightness
with open(file_name[:-4] + ".txt","w") as text:
# 'file_name[:-4]' takes the image file name and removes the last four characters (the extension).
# The 'w' simply allows the script to write to the text file.
	for y in range(height):
		for x in range(width):
			# Each pixel value is between 0 and 255 for grayscale (0=black, 255=white).  There are
			#	16 ASCII characters.  The following formula divides 256 into 16 individual sections.
			#	Pixels with value 0-15 are assigned 'M' (the darkest).  Pixels with values 16-31 are
			#	assigned '@'.  You get the picture... (pun intended)
			text.write(char[int(math.floor((pixels[x,y]/256.0)*16.0))])
		text.write("\n")
