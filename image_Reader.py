# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 23:33:26 2017

@author: lelac
"""

#image Reader, attribute producer

import sys
import os.path
import hashlib
import math
import binascii
import hashlib
import struct

def extract_MD5_SH1(name, pathImage): 
    sha1Name = 'SHA1-' + name + '.txt'
    md5Name = 'MD5-' + name + '.txt'
    print("================================================================================")
    print(md5Name)
    print(sha1Name)
    #calculations go here
    #print (pathImage[1][0])
    md5Checksum = md5(pathImage[1][0])
    sha1Checksum = sha1(pathImage[1][0])
    print("================================================================================")
    print("MD5 Checksum: " + md5Checksum)
    print("SHA-1 Checksum: " + sha1Checksum)
    print("================================================================================")
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

def littleConverter(something):
    something = int(something[0], 16)
    return (something >> 8) | ((something & 0xff) << 8)    

def extractMBR(fileName):
    partitionCounter = 0
    file = open(fileName, "rb")
    partitionType = {
    '01': 'DOS 12-bit FAT',
    '04': 'DOS 16-bit FAT for partitions smaller than 32MB',
    '05': 'Extended partition',
    '06': 'DOS 16-bit FAT for partitions larger than 32MB',
    '07': 'NTFS',
    '08': 'AIX bootable partition',
    '09': 'AIX data partition',
    '0b': 'DOS 32-bit FAT',
    '0c': 'DOS 32-bit FAT for interrupt 13 support',
    '17': 'Hidden NTFS partition (XP and earlier)',
    '1b': 'Hidden FAT32 partition',
    '1e': 'Hidden VFAT partition',
    '3c': 'Partition Magic recovery partition',
    '66': 'Novell partitions',
    '67': 'Novell partitions',
    '68': 'Novell partitions',
    '69': 'Novell partitions',
    '81': 'Linux',
    '82': 'Linux swap partition (can also be associated with Solaris partitions)',
    '83': 'Linux native file systems (Ext2, Ext3, Reiser, xiafs)',
    '86': 'FAT16 volume/stripe set (Windows NT)',
    '87': 'High Performance File System (HPFS) fault-tolerant mirrored partition or NTFS volume/strip set',
    'a5': 'FreeBSD and BSD/386',
    'a6': 'OpenBSD',
    'a9': 'NetBSD',
    'c7': 'Typical of a corrupted NTFS volume/stripe set',
    'eb': 'BeOS'
    }

    fatTypes = {
        '01',
        '04',
        '06',
        '0b',
        '0c',
        '1b',
        '86'
    }

    file.seek(446)
    partitionEntry1 = file.read(16)
    partitionEntry2 = file.read(16)
    partitionEntry3 = file.read(16)
    partitionEntry4 = file.read(16)

    hexadecimal1 = binascii.hexlify(partitionEntry1)
    hexadecimal2 = binascii.hexlify(partitionEntry2)
    hexadecimal3 = binascii.hexlify(partitionEntry3)
    hexadecimal4 = binascii.hexlify(partitionEntry4)

    partitionType1 = str(hexadecimal1[8:10])
    partitionType2 = str(hexadecimal2[8:10])
    partitionType3 = str(hexadecimal3[8:10])
    partitionType4 = str(hexadecimal4[8:10])

    partitionSize1 = str(int(hexadecimal1[30:32] + hexadecimal1[28:30] + hexadecimal1[26:28] + hexadecimal1[24:26], 16))
    partitionSize2 = str(int(hexadecimal2[30:32] + hexadecimal2[28:30] + hexadecimal2[26:28] + hexadecimal2[24:26], 16))
    partitionSize3 = str(int(hexadecimal3[30:32] + hexadecimal3[28:30] + hexadecimal3[26:28] + hexadecimal3[24:26], 16))
    partitionSize4 = str(int(hexadecimal4[30:32] + hexadecimal4[28:30] + hexadecimal4[26:28] + hexadecimal4[24:26], 16))

    partitionStart1 = str(int(hexadecimal1[22:24] + hexadecimal1[20:22] + hexadecimal1[18:20] + hexadecimal1[16:18], 16))
    partitionStart2 = str(int(hexadecimal2[22:24] + hexadecimal2[20:22] + hexadecimal2[18:20] + hexadecimal2[16:18], 16))
    partitionStart3 = str(int(hexadecimal3[22:24] + hexadecimal3[20:22] + hexadecimal3[18:20] + hexadecimal3[16:18], 16))
    partitionStart4 = str(int(hexadecimal4[22:24] + hexadecimal4[20:22] + hexadecimal4[18:20] + hexadecimal4[16:18], 16))

    print("(" + partitionType1.upper() + ") " + partitionType[partitionType1] + ", " + partitionStart1 + ", " + partitionSize1)
    print("================================================================================")
    print("(" + partitionType2.upper() + ") " + partitionType[partitionType2] + ", " + partitionStart2 + ", " + partitionSize2)
    print("================================================================================")
    print("(" + partitionType3.upper() + ") " + partitionType[partitionType3] + ", " + partitionStart3 + ", " + partitionSize3)
    print("================================================================================")
    print("(" + partitionType4.upper() + ") " + partitionType[partitionType4] + ", " + partitionStart4 + ", " + partitionSize4)
    print("================================================================================")
    file.close()

    if partitionType1 in fatTypes:
        extractVBR(fileName, int(partitionStart1), partitionType1, partitionType[partitionType1], partitionCounter)
        partitionCounter = partitionCounter + 1

    if partitionType2 in fatTypes:
        extractVBR(fileName, int(partitionStart2), partitionType2, partitionType[partitionType2], partitionCounter)
        partitionCounter = partitionCounter + 1

    if partitionType3 in fatTypes:
        extractVBR(fileName, int(partitionStart3), partitionType3, partitionType[partitionType3], partitionCounter)
        partitionCounter = partitionCounter + 1

    if partitionType4 in fatTypes:
        extractVBR(fileName, int(partitionStart4), partitionType4, partitionType[partitionType4], partitionCounter)
        partitionCounter = partitionCounter + 1

def extractVBR(fileName, startSector, fatType, partitionString, partitionCounter):
    print("Partition " + str(partitionCounter) + " (" + partitionString + ")")
    fat1612 = {
        '01',
        '04',
        '06',
        '86'
    }
    fat32 = {
        '0b',
        '0c',
        '1b'
    }
    startByte = startSector * 512
    file = open(fileName, "rb")
    file.seek(startByte)
    if fatType in fat1612:
        VBR = file.read(36)
    if fatType in fat32:
        VBR = file.read(48)
    VBRhex = binascii.hexlify(VBR)
    #reserved area #start sector #ending sector #size
    startSectorRA = 0
    endSectorRA = str(int(VBRhex[28:30], 16) - 1)
    RAsize = str(int(VBRhex[28:30], 16))
    #sectors per cluster
    secPerCluster = str(int(VBRhex[27], 16))
    
    #fat area: start sector: end sector:
    fatStart = RAsize
    
    # # of fats
    numOfFats = str(int(VBRhex[33],16))
    
    # size of each fat
    if fatType in fat1612:
        sizeOfFat = str(int(VBRhex[44:46], 16))

    if fatType in fat32:
        sizeOfFat = str(int(VBRhex[76:78] + VBRhex[74:76] + VBRhex[72:74], 16))
    
    endFatSector = str(int(RAsize) + int(numOfFats) * int(sizeOfFat) - 1)
    
    # first sector of cluster 2
    spotOfCluster2 = str(int(RAsize) + int(numOfFats) * int(sizeOfFat) + int(VBRhex[34:36],16))
    
    print('Reserved area: Start Sector: 0 Ending sector: ' + endSectorRA + ' Size: ' + RAsize + ' sectors')
    print('Sectors per cluster: ' + secPerCluster + ' sectors')
    print('FAT area: Start sector: ' + RAsize + ' Ending sector: ' + endFatSector)
    print('# of FATs: ' + numOfFats)
    print('The size of each FAT: ' + sizeOfFat + ' sectors')
    print('The first sector of cluster 2: ' + spotOfCluster2 + ' sectors')
    file.close()
    print("================================================================================")

def main():
    pathImage = []
    for args in sys.argv:
        arg = args.split(' ')
        pathImage.append(arg)
    base=os.path.basename(pathImage[1][0])
    name = os.path.splitext(base)
    #base = base imageName, with extention
    #print(base)
    name = name[0]
    #Base is image name stripped of file type designation
    #print(name)

    extract_MD5_SH1(name, pathImage)
    extractMBR(pathImage[1][0])
    

if __name__ == '__main__':
	main()
