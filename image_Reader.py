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
    sha1Name = 'SHA1-' + name + '.txt'
    md5Name = 'MD5-' + name + '.txt'
    print(sha1Name)
    print(md5Name)
    #calculations go here
    print (pathImage[1][0])
    md5Checksum = md5(pathImage[1][0])
    print(md5Checksum)
    sha1Checksum = sha1(pathImage[1][0])
    print(sha1Checksum)
    text_fileSHA1 = open(sha1Name, "w")
    text_fileSHA1.write(sha1Checksum)
    text_fileSHA1.close()
    text_fileMD5 = open(md5Name, "w")
    text_fileMD5.write(md5Checksum)
    text_fileMD5.close()
    
    
def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def sha1(fname):
    hash_md5 = hashlib.sha1()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def main():
    extract_MD5_SH1()
    
if __name__ == '__main__':
	main()