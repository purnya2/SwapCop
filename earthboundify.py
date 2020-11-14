import PythonMagick as Magick
import os
from PIL import Image, ImageDraw, ImageFont
import random

def start(textBox = "I shot my wife"):
    os.chdir('earthboundify\images')
    imgGui =  Magick.Image("UI.png")
    img = Magick.Image("dummy.png")
    img.resize("256x224!")
    img.composite(imgGui, 0, 0, Magick.CompositeOperator.OverCompositeOp)
    

     
    textImg = Image.new('RGBA', (256, 224), color = (0, 0, 0, 0))
    
    fnt = ImageFont.truetype('../apple_kid.ttf', 15)
    d = ImageDraw.Draw(textImg)
    #46
    count = 0
    textBoxn = ""
    for i in range(len(textBox)):
      count += 1
      if count > 46:
        count = 0
        textBoxn += '\n    '
      else:
        textBoxn += textBox[i]
         
      d.text((10,15), "-  "+textBoxn, font=fnt, fill=(255, 255, 255))
    
    textImg.save('text.png')

    textImg = Magick.Image('text.png')
    img.composite(textImg, 0, 0, Magick.CompositeOperator.OverCompositeOp)
    img.write("final.png")
        
    os.chdir('../')
    #os.system("ffmpeg -y -i images/final.png -i music"+str(random.randrange(1,4))+".m4a -loop 1 -vcodec libx264 -preset ultrafast -acodec copy outwithaudio.mp4")
    os.system("ffmpeg -y -i music"+str(random.randrange(1,4))+".m4a -loop 1 -i images/final.png -c:a aac -b:a 256k -ar 44100 -c:v libx264 -pix_fmt yuv420p -preset faster -tune stillimage -shortest outwithaudio.mp4")

    os.chdir('../')





  # playsound("test1.mp3")


if __name__ == '__main__':
  start()
