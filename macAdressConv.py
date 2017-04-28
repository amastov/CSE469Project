#Mac Address Conversion 
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

# -f file name parse
if ['-f'] in argVar:
    flag = argVar.index(['-f'])
    fileName = argVar[flag + 1]
    print ('File name: ', fileName)
    
if ['-h'] in argVar:
    flag = argVar.index(['-h'])
    hexValue = argVar[flag + 1]
    
if ['-T'] in argVar:
    #Run time conversions
    result = timeConversion()
    print (result)

if ['-D'] in argVar:
    #Run Date conversions
    result = dateConversion()
    print (result)
    
def timeConversion():
    #Time conversion for -f
    if ['-f'] in argVar:
    with open(args.file, 'r') as L:
        info = int(L.read(), 16)
        
    #Time conversion for -h
    if ['-h'] in argVar:

def littleConverter(something):
    return (something >> 8) | ((something & 0xff) << 8)
  
def dateConversion():
    #Date conversion for -f
    if ['-f'] in argVar:
    
    #Date conversion for -h
    if ['-h'] in argVar:
        
        