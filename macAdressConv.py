#Mac Address Conversion 
#Leo Lacroix
import sys


print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))

dates = {1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June', 
         7:'July', 8:'August', 9:'September', 10:'October', 11:'November', 
         12:'December'}

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
    
def timeConversion():
    #Time conversion for -f
    if ['-f'] in argVar:
        with open(args.fileName, 'r') as L:
            info = int(L.read(), 16)
        
    #Time conversion for -h
    if ['-h'] in argVar:
        info = hexValue
   
    info = littleConverter(info)
    
    seconds = (info & 0x1f) * 2
    minutes = (info >> 5) & 0x3f
    hours = (info >> 11) & 0x1f
    
    nightNday = 'AM' 
    seconds = (info & 0x1f) * 2
    minutes = (info >> 5) & 0x3f
    hours = (info >> 11) & 0x1f
    #if the time is PM
    if (hours > 12):
        hours = hours - 12
        nightNday = 'PM'
    return 'Time: {0}:{1} {2}'.format(hours, minutes, seconds,
                  nightNday)
    
    
    
#Converts from little endian format
def littleConverter(something):
    something = int(something[0], 16)
    return (something >> 8) | ((something & 0xff) << 8)
  

def dateConversion():
    #Date conversion for -f
    if ['-f'] in argVar:
        with open(fileName, 'r') as L:
            info = int(L.read(), 16)
        
    #Date conversion for -h
    if ['-h'] in argVar:
        info = hexValue
     
    info = littleConverter(info)
    
    month = dates[(info>>5) & 0xf]
    day = info & 0x1f
    year = ((info >> 9) & 0x7f) + 1980
           
    return ('Date: {0} {1}, {2}'.format(month, day, year))

# -f file name parse
if ['-f'] in argVar:
    flag = argVar.index(['-f'])
    fileName = argVar[flag + 1]
    print ('File name: ', fileName)
    
if ['-h'] in argVar:
    flag = argVar.index(['-h'])
    hexValue = argVar[flag + 1]
    print ('Hex value: ', hexValue)

if ['-T'] in argVar:
    #Run time conversions
    
    print (timeConversion())

if ['-D'] in argVar:
    #Run Date conversions
    print(dateConversion())