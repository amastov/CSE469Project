#image Reader, attribute producer

import sys
import os.path
import hashlib
import math

import hashlib



#read in Image file
pathImage = []
#    arg = args.split('/')
#    pathImage.append(args)

def extract_MD5_SH1(): 
    pathImage = []
    for args in sys.argv:
        arg = args.split(' ')
        pathImage.append(arg)
    base=os.path.basename(pathImage[1][0])
    name = os.path.splitext(base)
    #base = base imageName, with extention
    print(base)
    name = name[0]
    #Base is image name stripped of file type designation
    print(name)
    #

def main():
    extract_MD5_SH1()
    print('stuff')

if __name__ == '__main__':
	main()