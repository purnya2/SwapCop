import os, time
from pydub import AudioSegment

def init(phrase):
    phrase = "say.exe -w out.wav \"[:phoneme on]" + str(phrase)+"\""
    os.chdir('tts')
    print(phrase)
    os.system(phrase)
    print("a")
    
    time.sleep(1)
    os.chdir('../')