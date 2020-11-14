import os, random
import cv2
from PIL import Image
import glob
import numpy as np

h, w, layers = (320,320,3)

#TODO conversione in secondi
class Timeline:
    time = 0
    files = {None}

    sceneList = [None]

    def __init__(self,diz,height,width,framerate):
        files = diz
        self.out = cv2.VideoWriter('out.avi',cv2.VideoWriter_fourcc(*'DIVX'), framerate, (height,width))
    
    def composite(self):
        for scene in sceneList:
            #fai roba
            pass
        
        
        pass

    sceneList = [None]
    def update(self,frame):
        print(frame)
        self.out.write(frame)
        self.time += 1
    
    sceneList = [None]
    sceneList = [None]
    def finish(self):
        self.out.release()
        os.system('ffmpeg -y -i  out.avi -i audio.mp3 -vcodec libx264 -preset ultrafast -acodec copy outwithaudio.mp4')
#TODO accatastare varie scene tra di loro

#TODO SPACCATI LA TESTA, TAGLIATI LE VENE E METTO ARRAY DI IMMAGINI PER ONGI
class Scene:

    def __init__(self,l):
        self.time=0
        self.length = l
        self.layer = {}
        self.img = None
        Timeline.sceneList.append(self)
        pass

    def composite(self):
        self.img = self.layer['0'].img
        
        #TODO rendere automatica questa cosa

    def frame(self):
        return self.img

class Layer:
    
    #TODO avere un sistema che tenga conto dei secondi passati
    
    #TODO fare in modo che questa roba produca una immagine
    def testo(self,str,x=0,y=0,size=10,font="Comic Sans"):
        pass

    #TODO funzione che riceve letteralmente un file
    def image(self,file,sizeX=w,sizeY=h,posx=0,posy=0):
        pass

    def __init__(self):
        self.img = None
        pass
        
    def solidColor(self,r,g,b):

        out = np.zeros((h,w,3), np.uint8)
        out[:] = (b,g,r)
        self.img = out
        pass
    
    def __str__(self):
        out = str(self.img)
        return out

    def moveImage(self, posx, posy):
        M = np.float32([[1,0,posx],[0,1,posy]])
        out = cv2.warpAffine(self.img,M,(height,width))
        self.img=out

    def rotateImage(self, pivot, angle, scale):
        M = cv2.getRotationMatrix2D(pivot, angle, scale)
        out = cv2.warpAffine(self.img, M, (height, width))
        self.img=out

def main():
##########################
    os.chdir('test/images')
    img_diz = {}
    for filename in glob.glob('*.png'):
        
        img = cv2.imread(filename)
        img = cv2.resize(img,(w,h))
        #img = img[0:500, 0:500]
        img_diz[filename] = img
        size = (h,w)
    os.chdir('../')
##########################
    dorime = Timeline(img_diz,h, w,30)
    
    #sce = Scene()
    scena1 = Scene(10)
    scena2 = Scene(10)

    #setta i layer lol
    #scena1.layer['0'] = testo("heyyy",320,200,10,"comic sans")
    #scena1.layer['1'] = image(dorime.files["pray.png"],250,250)
    #scena1.layer['2'] =.image(dorime.files["dummy.png"])
    blacklayer = Layer()
    blacklayer.solidColor(234,100,222)



    scena1.layer['0'] = blacklayer

    #DEVO ESSERE IN GRADO DI OTTENERE LA POSIZIONE CORRENTE NEI PRIMI DUE PARAMETRI
    blacklayer.moveImage([0,0],[100,100],atwhattime,10s) #in caso, dopo, fmetto il parametro di easing
    #print(scena1.layer['0'])
    for i in range(60):
        blacklayer.solidColor(i,i,i)
        scena1.composite()
        dorime.update(scena1.frame())

    dorime.finish()
    print(dorime.time)


if __name__ == "__main__":
    main()