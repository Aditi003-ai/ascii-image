from PIL import Image,ImageDraw, ImageFont 
import math

chars = "@%$*+=:."

charArray = list(chars)
charLength = len(charArray)
interval = charLength/256

ScaleFactor = 0.1
oneCharWidth = 8
oneCharHeight = 18

def getChar(inputInt):
    return charArray[math.floor(inputInt*interval)]
    
text_file =open("output.png","w")
im = Image.open("billclinton.png")


width, height = im.size
print(width,height,height/width)
im = im.resize((int(ScaleFactor*width), int(ScaleFactor*height*(oneCharWidth/oneCharHeight))),Image.NEAREST)
width, height = im.size
pix = im.load()

outputImage = Image.new('RGB',(oneCharWidth*width , oneCharHeight*height),color = (0,0,0))

for i in range(height):
    for j in range(width):
        r,g,b = pix[j,i]
        print(r) 
        h = int(r/3 + g/3 + b/3)
        pix[j,i]=(h,h,h)
        text_file.write(getChar(h))
        

    text_file.write('\n')    

outputImage.save('output.png')