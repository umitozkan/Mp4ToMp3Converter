import os
from moviepy.editor import *

# please convert snake_case to camelCase 
def convert(name):
    #print(name)
    mp3 = name.replace('mp4', 'mp3')
    print(mp3)

    mp4_file = name

    mp3_file = mp3
    videoClip = VideoFileClip(mp4_file)
    audioClip = videoClip.audio

    audioClip.write_audiofile(mp3_file)
    audioClip.close()
    videoClip.close()




path = os.getcwd()

f = open("yol.txt", "r")
path = f.readline()
path = path.replace("\n", "")
f.close()
obj = os.scandir(path)

for entry in obj:
    if entry.is_file():
        
        if entry.name.lower().endswith('.mp4'):
            convert(path+"\\"+entry.name)
            new = path+"\\"+entry.name
 




obj = os.scandir(path)

for entry in obj:
    if entry.is_dir() :
      
        
        obj2 = os.scandir(path +"\\"+ entry.name)
      
        for entry2 in obj2:
            if entry2.name.lower().endswith('.mp4') :
                    newpath = path +"\\"+ entry.name
                    convert(newpath +"\\"+entry2.name)
                    new = newpath+"\\"+entry2.name
 
      
               
