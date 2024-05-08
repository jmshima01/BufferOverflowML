from PIL import Image
from sys import argv
import os

files_missed = 0

def makeIMG(imgpath,dest):
    global files_missed
    
    data = [0]*65536 # 256 by 256 pixel image with 
    with open(imgpath,"rb")as f:
        d = f.read()
        for i,v in enumerate(d):
            try:
                data[i]= v
            except:
                print("ind out of bounds,",imgpath,i,len(d))
                files_missed+=1
                return
    image = Image.frombytes('L',(256,256), bytes(data), 'raw')
    sav = imgpath.split("/")[-1].split(".")[0]
    image.save(f"{dest}/{sav}.png")


if __name__ == "__main__":
    for f in os.scandir(argv[1]):
        # print("Working on",f.path)
        for j in os.scandir(f.path):
            if j.name == "partial.o":
                continue
            makeIMG(j.path,f"images/{f.name}")
    # print(files_missed)
        
