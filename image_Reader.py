#image Reader, attribute producer

import sys
import os.path
import hashlib
import math
import image

#read in Image file
pathImage = []
for args in sys.argv:
    arg = args.split(' ')
    pathImage.append(args)

for pathImage[1] in pathImage:
    try:
        im=Image.open(pathImage[1])
    # do stuff
    except IOError:
        print('Invalid Path')
    # filename not an image file

print(pathImage)