import os, random
import cv2
from PIL import Image
import glob
import numpy as np
#frame1  = 110
#frame2  = 168
#frame3  = 230
#frame4  = 290
#frame5  = 340
#frame6  = 390
#frame7  = 460
#frame8  = 530
finalFrame = 720
keyframelist=[110,168,230,290,340,390,450,530,finalFrame]
height, width, layers = (500,500,3)

def overlay_transparent(background, overlay, x, y):

    background_width = background.shape[1]
    background_height = background.shape[0]

    if x >= background_width or y >= background_height:
        return background

    h, w = overlay.shape[0], overlay.shape[1]

    if x + w > background_width:
        w = background_width - x
        overlay = overlay[:, :w]

    if y + h > background_height:
        h = background_height - y
        overlay = overlay[:h]

    if overlay.shape[2] < 4:
        overlay = np.concatenate(
            [
                overlay,
                np.ones((overlay.shape[0], overlay.shape[1], 1), dtype = overlay.dtype) * 255
            ],
            axis = 2,
        )

    overlay_image = overlay[..., :3]
    mask = overlay[..., 3:] / 255.0

    background[y:y+h, x:x+w] = (1.0 - mask) * background[y:y+h, x:x+w] + mask * overlay_image

    return background

def moveImage(inImage, posx, posy):
    M = np.float32([[1,0,posx],[0,1,posy]])
    out = cv2.warpAffine(inImage,M,(height,width))
    return out

def rotateImage(inImage, pivot, angle, scale):
    M = cv2.getRotationMatrix2D(pivot, angle, scale)
    out = cv2.warpAffine(inImage, M, (height, width))
    return out

def keyframe1():
    return np.zeros((height,width,3), np.uint8)
    
def keyframe2(img_diz,textfile,i,keyframeback,keyframeafter):
    #set images
    text = img_diz[textfile]
    dummy = img_diz['dummy.png']
    pray = img_diz['pray.png']
    pray = cv2.resize(pray,(250,250))
    #make canvas
    img = np.zeros((height,width,3), np.uint8)
    img[:] = (255,255,255)

    i = np.interp(i, [keyframelist[keyframeback],keyframelist[keyframeafter]], [1,0.5])
    dummy = moveImage(dummy,200*i,125)
    pray = moveImage(pray,300*i,300)
    
    dummy = np.where(pray==0,dummy,pray)
    outframe = np.where(dummy==0,img,dummy)
    outframe = np.where(text!=0,outframe,text)

    return outframe

def keyframe4(img_diz,textfile,i,keyframeback,keyframeafter):
    img = img_diz['background1.png']
    text = img_diz[textfile]
    
    dummy = img_diz['dummy.png']
    dummy = cv2.resize(dummy,(300,300))
    dummy = moveImage(dummy,200,200)
    dummy = rotateImage(dummy,(height/2, width/2),-45,1)
    dummy = moveImage(dummy,140,50)

    palm = img_diz['palmsup.png']
    palm = cv2.resize(palm,(300,300))
    palm = moveImage(palm,200,200)
    palm = rotateImage(palm,(height/2, width/2),45,0.5)
    palm = moveImage(palm,-50,100)

    dummy = np.where(palm==0,dummy,palm)
    outframe = np.where(dummy==0,img,dummy)
    outframe = np.where(text!=0,outframe,text)
    return outframe

def keyframe3(img_diz,textfile,i,keyframeback,keyframeafter):
    img = img_diz['background0.png']
    text = img_diz[textfile]
    
    dummy = img_diz['dummy.png']
    dummy = cv2.resize(dummy,(400,400))
    dummy = moveImage(dummy,200,200)

    outframe = np.where(dummy==0,img,dummy)
    outframe = np.where(text!=0,outframe,text)
    return outframe

def keyframe5(img_diz,textfile,i,keyframeback,keyframeafter):
    img = np.zeros((height,width,3), np.uint8)
    img[:] = (0,0,0)
    offsetx = random.randrange(0,5)
    offsety = random.randrange(0,5)
    redimg =  np.zeros((height,width,3), np.uint8)
    redimg[:] = (0,0,255)

    dummy = img_diz['dummy.png']
    dummy = cv2.resize(dummy,(400,400))
    dummy = moveImage(dummy,10+offsetx,10+offsety)
    outframe = np.where(dummy==0,img,dummy)
    outframe = np.where(outframe != 0, cv2.add(outframe, redimg), outframe)

    if i > 600 and i< 660:
        #outframe = np.where(img_diz['omanarered.png'] != 0,outframe ,img_diz['omanarered.png'])
        text = img_diz['omanarered.png']
            

    else:
        text = img_diz['amenored.png']
    outframe = np.where((text==[255,255,255]),outframe,text)
    #outframe = np.where(outframe==(255,255,255),img,outframe)


    return outframe

def keyframe6():
    img = np.zeros((height,width,3), np.uint8)
    img[:] = (0,0,255)
    return img

def keyframe7():
    img = np.zeros((height,width,3), np.uint8)
    img[:] = (0,255,0)
    return img

def start(): 
    '''start si occupa di, prendere i file, e creare l'oggetto out, 
    per poi andare in sequenza dentro le funzioni per avere un out finale ahh cazzo
    NON SO COSA CAZZO STO FACENDO
    DIO CANE'''
    os.chdir('dorime\images')
    img_diz = {}
    for filename in glob.glob('*.png'):
        
        img = cv2.imread(filename)
        img = cv2.resize(img,(width,height))
        #img = img[0:500, 0:500]
        img_diz[filename] = img
        size = (width,height)
    os.chdir('../')


    out = cv2.VideoWriter('out.avi',cv2.VideoWriter_fourcc(*'DIVX'), 24, (height,width))
    for i in range(finalFrame):
        if i < keyframelist[0]:
            print("sequencing 1 keyframe")

            frame = keyframe1()
        elif i < keyframelist[1]:
            print("sequencing 2 keyframe")


            frame = keyframe2(img_diz,'dorime.png',i,0,1)
        elif i < keyframelist[2]:
            print("sequencing 3 keyframe")


            frame = keyframe3(img_diz,'interimo.png',i,1,2)
        elif i < keyframelist[3]:
            print("sequencing 4 keyframe")


            frame = keyframe2(img_diz,'dorime.png',i,2,3)
        elif i < keyframelist[4]:
            print("sequencing 5 keyframe")


            frame = keyframe4(img_diz,'ameno.png',i,3,4)
        elif i < keyframelist[5]:
            print("sequencing 6 keyframe")


            frame = keyframe2(img_diz,'latire.png',0,6,7)
            lastframe5 = keyframe2(img_diz,'latire.png',0,6,7)
        elif i < keyframelist[6]:
            print("sequencing 7 keyframe")


            j = i
            j = np.interp(j, [float(keyframelist[5]),float(keyframelist[5]+24)], [0.0,1.0])
            k = 1.0 - j
            frame6 = keyframe2(img_diz,'latiremo.png',0,6,7)
            frame =  cv2.addWeighted(lastframe5, k, frame6, j, 0.0)
        elif i < keyframelist[7]:
            print("sequencing 8 keyframe")


            frame = keyframe2(img_diz,'dorime.png',i,6,7)
        elif i < keyframelist[8]:
            print("sequencing 9 keyframe")
            frame = keyframe5(img_diz,'dorime.png',i,7,8)
        out.write(frame)


    out.release()

    os.system('ffmpeg -y -i  out.avi -i audio.mp3 -vcodec libx264 -preset ultrafast -acodec copy outwithaudio.mp4')
    os.chdir('../')

if __name__ == "__main__":
    start()