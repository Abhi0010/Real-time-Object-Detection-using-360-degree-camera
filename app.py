import os
from yolov5 import Yolov5
import argparse
from PIL import Image
import math
import abc
import numpy as np
from src import *
from mss import mss
from PIL import Image
import cv2
import pandas as pd
from gtts import gTTS
import time
import pyttsx3
from playsound import playsound

yolo = Yolov5()

def textToSpeech(mytext,direction):
  
    # Language in which you want to convert
    language = 'en'
    text=mytext+'at'+direction
    # Passing the text and language to the engine, here we have marked slow=False. Which tells the module that the converted audio should have a high speed
    myobj = gTTS(text=text, lang=language, slow=False)
    
    myobj.save("object.mp3")
    playsound("object.mp3")
    os.remove("object.mp3")
    # myobj.save("object.mp3")
    # os.system("object.mp3")

def textSpeech(mytext,direction):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')  
    engine.setProperty("rate", 150)
    for voice in voices:
        print(voice, voice.id)
        engine.setProperty('voice', voice.id)
        text=mytext+'at'+direction  
        engine.say(text)  
        engine.runAndWait()

def main():
    parser = argparse.ArgumentParser(description='360 View Object Detector')
    # parser.add_argument('--approach', required=True, help='Which approach do you want to use? 1: Fisheye 2: Cubemap 3: Equirectangular')
    parser.add_argument('--input', required=True, help='Type of input 1: Video 2: Image 3: Webcam')
    parser.add_argument('--image_path', required=False, help='Path to input file Single image with dual fish eye view. Required in case of Image input')
    parser.add_argument('--video_path', required=False, help='Path to input file Video file. Required in case of Video input')
    parser.add_argument('--webcam_id', required=False, help='Webcam ID. Required in case of Webcam input')
    parser.add_argument('--useBilinear', required=False, help='Use bilinear interpolation when reprojecting. Valid values are true and false.')
    parser.add_argument('--output_path', required=False, help='Path to output file. For approach 1&2: single file for approach 3: 6 files. Output path not required for webcam')
    # parser.add_argument('--output_width', required=True, help='Output width in pixels')
    # parser.add_argument('--output_height', required=True, help='Output height in pixels')
    args = parser.parse_args()

    # approach = None
    # if args.approach.lower() == "Fisheye".lower():
    #     approach = 1
    # elif args.approach.lower() == "Cubemap".lower():
    #     approach = 2
    # elif args.approach.lower() == "Equirectangular".lower():
    #     approach = 3
    # else:
    #     print("Quitting because unsupported approach type: ", args.approach)
    #     return
    

    input = None
    if args.input.lower() == "Video".lower():
        input = 1
    elif args.input.lower() == "Image".lower():
        input = 2
    elif args.input.lower() == "Webcam".lower():
        input = 3
    else:
        print("Quitting because unsupported input type: ", args.input)
        return

    out = None
    # if args.output_path is not None and input != 3:
    #     out = args.output_path
    # else:
    #     print('Quitting because output path is required for image and video input')
    #     return
    
    # if args.output_width is None or args.output_height is None:
    #     print('Quitting because output width and height are required')
    #     return

    if input == 1:
        '''
        Video Logic
        '''
        return
    elif input == 2:
        if args.image_path is None:
            print("Quitting because image path is required for image input")
            return
        else:
            image_path = args.image_path
            if not os.path.isfile(image_path):
                print("Quitting because image path is not valid: ", image_path)
                return
            if approach == 1:
                '''
                Fisheye Logic
                '''
                image = out
                results = yolo.predict(image)
                results.show()
                return
            elif approach == 2:
                '''
                Cubemap Logic
                '''
                fisheye = SideBySideFisheyeProjection()
                fisheye.loadImage(image_path)
                if args.useBilinear is not None and args.useBilinear.lower() == "true":
                    fisheye.set_use_bilinear(True)
                output = CubemapProjection()
                output.initImages(int(args.output_width), int(args.output_height))
                output.reprojectToThis(fisheye)
                imageList = out.split(' ')
                images = output.getImages(imageList[0], imageList[1], imageList[2], imageList[3], imageList[4], imageList[5])
                #output.saveImages(imageList[0], imageList[1], imageList[2], imageList[3], imageList[4], imageList[5])
                results = yolo.predict(images)
                results.show()
                return
            elif approach == 3:
                '''
                Equirectangular Logic
                '''
                fisheye = SideBySideFisheyeProjection()
                fisheye.loadImage(image_path)
                if args.useBilinear is not None and args.useBilinear.lower() == "true":
                    fisheye.set_use_bilinear(True)
                output = EquirectangularProjection()
                output.initImage(int(args.output_width), int(args.output_height))
                output.reprojectToThis(fisheye)
                image = output.getImage()
                results = yolo.predict(image)
                results.show()
                return
        return
    elif input == 3:

        direct='C:/Abhishek/results'
        sct = mss()
        framecount=0
        predicted=[]
        xdirection=['left','mid','right'] #1920 width divided in three areas
        ydirection=['top','centre','bottom'] #1080 height divided in three areas

        #assign first priority for moving objects
        priorityclasses=['bicycle', 'car', 'motorbike', 'aeroplane', 'bus', 'train', 'truck', 'boat'] 

        while True:
            w, h = 1920, 960
            framecount+=1
            monitor = {'top': 0, 'left': 0, 'width': w, 'height': h}
            img = Image.frombytes('RGB', (w,h), sct.grab(monitor).rgb)
            # img=cv2.cvtColor(np.array(img),cv2.COLOR_BGR2RGB)
            starttime=time.time()
            fisheye = SideBySideFisheyeProjection()
            print(time.time()-starttime)
            img.save('temp.png')
            fisheye.loadImage('temp.png')
            print(time.time()-starttime)
            output = CubemapProjection()
            output.initImages(int(512), int(256))
            output.reprojectToThis(fisheye)
            out = "a.png b.png c.png d.png e.png f.png"
            imageList = out.split(' ')
            images = output.getImages(imageList[0], imageList[1], imageList[2], imageList[3], imageList[4], imageList[5])
            # images[0].save('temp1.png')
            # images[1].save('temp2.png')
            # images[2].save('temp3.png')
            # images[3].save('temp4.png')
            # images[4].save('temp5.png')
            # images[5].save('temp6.png')
            print(time.time()-starttime)
            results = yolo.predict(images[1])
            # results = yolo.predict(img)
            # results.show()
            results.save(save_dir=direct+'/'+str(framecount))
            print(results.pandas().xyxy[0])
            arr=results.pandas().xyxy[0]
            for i in range(0,len(arr['confidence'])):
                if arr['name'][i] in priorityclasses:
                    if arr['confidence'][i]>0.7:
                        avgx=(arr['xmin'][i]+arr['xmax'][i])/2
                        avgy=(arr['ymin'][i]+arr['ymax'][i])/2
                        xval=int(avgx/640) #divided to get index of xdirection 
                        yval=int(avgy/320) #divided to get index of ydirection
                        textToSpeech(arr['name'][i],xdirection[xval]+ydirection[yval])

            for i in range(0,len(arr['confidence'])):
                if arr['confidence'][i]>0.7:
                    if arr['xmin'][i]>640 and arr['xmax'][i]<=1280:
                        avgy=(arr['ymin'][i]+arr['ymax'][i])/2
                        val=int(avgy/320)
                        text='mid '+ydirection[val]
                        textToSpeech(arr['name'][i],text)
                        # time.sleep(2)
                        # predicted.append(arr['name'][i])   
                         
            # cv2.imwrite(direct+'/frame'+str(i)+'.png', np.array(results))
            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break

if __name__ == "__main__":
    main()

'''
python app.py --approach CubeMap --input Image --image_path "C:\Abhishek\MV 360 deg\360_0230\frame00236.png" --useBilinear True --output_path "frame01.png frame02.png frame03.png frame04.png frame05.png frame06.png" --output_width 512 --output_height 512
'''




