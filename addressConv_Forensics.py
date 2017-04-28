#adress convertor
#Joel Myhre, 4/19/2017
import sys
print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))

#store our arguments in argVar array
argVar = []
for args in sys.argv:
    arg = args.split(' ')
    print('Input Reads')
    if '=' in args:
        arg1 = args.split('=')
        argVar.append([arg1[0]])
        argVar.append([arg1[1]])
        
    #argSub = arg.split('=')
    print(arg)
    #argSub = arg.split('=')
    argVar.append([args])
    
print (argVar)

#byte offset flag
if ['-b'] in argVar:
    flagPosition = argVar.index(['-b'])
    offset = argVar[flagPosition+1]
    print ('offset:',offset)

if ['--partition-start'] in argVar:
    flagPosition = argVar.index(['--partition-start'])
    offset = argVar[flagPosition+1]
    print ('offset:',offset)

#bytes adress flags
if ['-B'] in argVar:
    byteAddressFlag = 1
    print ('Byte Address Flag')

if ['--byte-address'] in argVar:
    byteAddressFlag = 1
    print ('Byte Address Flag')

#sector size flags
if ['-s'] in argVar:
    if ['-B'] in argVar:
        flagPosition = argVar.index(['-s'])
        bytesPerSector = argVar[flagPosition+1]
        print ('Bytes per sector:',bytesPerSector)

if ['--sector-size'] in argVar:
    if ['-B'] in argVar:
        flagPosition = argVar.index(['--sector-size'])
        bytesPerSector = argVar[flagPosition+1]
        print ('Bytes per sector:',bytesPerSector)

#logical flags
if ['--logical-known'] in argVar:
    flagPosition = argVar.index(['--logical-known'])
    logicalAddress = argVar[flagPosition+1]
    print ('known logical address')

if ['-l'] in argVar:
    flagPosition = argVar.index(['-l'])
    logicalAddress = argVar[flagPosition+1]
    print ('known logical address')
 
#both physical flags

if ['--physical-known'] in argVar:
    flagPosition = argVar.index(['--physical-known'])
    physicalAddress = argVar[flagPosition+1]
    print ('known physical address')

if ['-p'] in argVar:
    flagPosition = argVar.index(['-p'])
    physicalAddress = argVar[flagPosition+1]
    print ('known physical address')
    
#both cluster flags

if ['--cluster-known'] in argVar:
    clusterReturn = 0
    if ['-f'] in argVar:
        if ['-t'] in argVar:
            if ['-r'] in argVar:
                if ['-k'] in argVar:
                    flagPosition = argVar.index(['--cluster-known'])
                    clusterAddress = argVar[flagPosition+1]
                    print ('known cluster address')
    if clusterReturn == 0:
        print('Invalid number of cluster arguments')

if ['-c'] in argVar:
    clusterReturn = 0
    if ['-f'] in argVar:
        if ['-t'] in argVar:
            if ['-r'] in argVar:
                if ['-k'] in argVar:
                    flagPosition = argVar.index(['-c'])
                    clusterAddress = argVar[flagPosition+1]
                    print ('known cluster address')
    if clusterReturn == 0:
        print('Invalid number of cluster arguments')
    
#cluster size flags
if ['-k'] in argVar:
    flagPosition = argVar.index(['-k'])
    secPerCluster = argVar[flagPosition+1]
    print ('Sectors Per Cluster:',secPerCluster)

if ['--cluster-size'] in argVar:
    flagPosition = argVar.index(['--cluster-size'])
    secPerCluster = argVar[flagPosition+1]
    print ('Sectors Per Cluster:',secPerCluster)

#reserved flags
if ['-r'] in argVar:
    flagPosition = argVar.index(['-r'])
    reservedSectors = argVar[flagPosition+1]
    print ('Reserved Sectors:',reservedSectors)

if ['--reserved'] in argVar:
    flagPosition = argVar.index(['--reserved'])
    reservedSectors = argVar[flagPosition+1]
    print ('Reserved Sectors:',reservedSectors)

#table flags    
if ['-t'] in argVar:
    flagPosition = argVar.index(['-t'])
    numberFAT = argVar[flagPosition+1]
    print ('Number of FAT tables:',numberFAT)

if ['--fat-table'] in argVar:
    flagPosition = argVar.index(['--fat-table'])
    numberFAT = argVar[flagPosition+1]
    print ('Number of FAT tables:',numberFAT)
    
#FAT sector size flags
if ['-f'] in argVar:
    flagPosition = argVar.index(['-f'])
    FATlength = argVar[flagPosition+1]
    print ('FAT table length in sectors:',FATlength)

if ['--fat-length'] in argVar:
    flagPosition = argVar.index(['--fat-length'])
    FATlength = argVar[flagPosition+1]
    print ('FAT table length in sectors:',FATlength)

def byteConvert(result):
    #Converts address to bytes if -B is in argument
    if (['-s'] in argVar) or (['--sector-size'] in argVar):
                return (result * bytesPerSector)
            #Default 512 bytes per sector
    else: 
        return (result * 512) 

def logicConvert():
    print('Logical Conversion begins:')
    if (['-l'] in argVar) or (['--logical-known'] in argVar):
        result = logicalAddress
    
    #changes physical address to a logical address
    if (['-p'] in argVar) or (['--physical-known'] in argVar):
        result = int(physicalAddress[0]) - int(offset[0])
        
    #Converts for changing a cluster to a logical address
    if (['-c'] in argVar) or (['--cluster-known'] in argVar):
        result = offset + (clusterAddress - 2) * secPerCluster + reservedSectors + (numberFAT * FATlength)
        resut = result - offset
    if (['-B'] in argVar) or (['--byte-address'] in argVar):
        #Calls function to convert to byte address
        byteConvert()
    else:
        return result

def physicalConvert():
    print('Physical Conversion begins:')
    if (['-p'] in argVar) or (['--physical-known'] in argVar):
        result = physicalAddress
    #converts cluster to physical address
    if (['-c'] in argVar) or (['--cluster-known'] in argVar):
        if (['-c'] in argVar) or (['--cluster-known'] in argVar):
            result = offset + (clusterAddress - 2) * secPerCluster + reservedSectors + (numberFAT * FATlength)

    #Converts logical address to physical address
    if (['-l'] in argVar) or (['--logical-known'] in argVar):
        result = logicalAddress + offset
    
    if (['-B'] in argVar) or (['--byte-address'] in argVar):
        #Finds if there was a specification on the bytes per sector
        byteConvert()
    else:
        return result

def clusterConvert():
    print('Cluster Conversion begins:')
    if (['-c'] in argVar) or (['--cluster-known'] in argVar):
        result = clusterAddress
        
    #Converts logical address to a cluster address
    if (['-l'] in argVar) or (['--logical-known'] in argVar):
         result = ((logicalAddress - reservedSectors - (numberFAT * FATlength)) / secPerCluster) + 2

    #Converts physical address to cluster address
    if (['-p'] in argVar) or (['--physical-known'] in argVar):
         result = physicalAddress - offset
    
    #Checks for need of byte conversion, if not returns result
    if (['-B'] in argVar) or (['--byte-address'] in argVar):
        #Finds if there was a specification on the bytes per sector
        byteConvert()
    else:
        return result

#check if arguments are valid
if argVar[1] == ['-L'] in argVar:
        logicConvertFlag = 0    
        if ['-p'] in argVar:
            logicConvertFlag = 1
        if ['--physical-known'] in argVar:
            logicConvertFlag = 1
        if ['-c'] in argVar:
            logicConvertFlag = 1
        if ['--cluster-known'] in argVar:
            logicConvertFlag = 1
        print ('Logical Address Conversion')
        if logicConvertFlag == 1:
            logicConvert()            
elif argVar[1] == ['-P'] in argVar:
        physicalConvertFlag = 0    
        if ['-l'] in argVar:
            physicalConvertFlag = 1
        if ['--logical-known'] in argVar:
            physicalConvertFlag = 1
        if ['-c'] in argVar:
            physicalConvertFlag = 1
        if ['--cluster-known'] in argVar:
            physicalConvertFlag = 1
        if physicalConvertFlag == 1:
            print ('Physical Address Conversion')
            physicalConvert()    
elif argVar[1] == ['-C'] in argVar:
        clusterConvertFlag = 0    
        if ['-p'] in argVar:
            clusterConvertFlag = 1
        if ['--physical-known'] in argVar:
            clusterConvertFlag = 1
        if ['-c'] in argVar:
            clusterConvertFlag = 1
        if ['--cluster-known'] in argVar:
            logicConvertFlag = 1
        if clusterConvertFlag == 1:
            print ('Cluster Address Conversion')
            clusterConvert()    
else:
        print('Invalid Flag Conversion Parameters')
print (argVar[1])