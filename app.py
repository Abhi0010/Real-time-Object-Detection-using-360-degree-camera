import os
from yolov5 import Yolov5
import argparse
from PIL import Image
import math
import abc
import numpy as np
from src import *
yolo = Yolov5()
def main():
    parser = argparse.ArgumentParser(description='360 View Object Detector')
    parser.add_argument('--approach', required=True, help='Which approach do you want to use? 1: Fisheye 2: Cubemap 3: Equirectangular')
    parser.add_argument('--input', required=True, help='Type of input 1: Video 2: Image 3: Webcam')
    parser.add_argument('--image_path', required=False, help='Path to input file Single image with dual fish eye view. Required in case of Image input')
    parser.add_argument('--video_path', required=False, help='Path to input file Video file. Required in case of Video input')
    parser.add_argument('--webcam_id', required=False, help='Webcam ID. Required in case of Webcam input')
    parser.add_argument('--useBilinear', required=False, help='Use bilinear interpolation when reprojecting. Valid values are true and false.')
    parser.add_argument('--output_path', required=False, help='Path to output file. For approach 1&2: single file for approach 3: 6 files. Output path not required for webcam')
    parser.add_argument('--output_width', required=True, help='Output width in pixels')
    parser.add_argument('--output_height', required=True, help='Output height in pixels')
    args = parser.parse_args()

    approach = None
    if args.approach.lower() == "Fisheye".lower():
        approach = 1
    elif args.approach.lower() == "Cubemap".lower():
        approach = 2
    elif args.approach.lower() == "Equirectangular".lower():
        approach = 3
    else:
        print("Quitting because unsupported approach type: ", args.approach)
        return
    

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
    if args.output_path is not None and input != 3:
        out = args.output_path
    else:
        print('Quitting because output path is required for image and video input')
        return
    
    if args.output_width is None or args.output_height is None:
        print('Quitting because output width and height are required')
        return

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
                return
        return
    elif input == 3:
        '''
        Web cam logic
        '''
        return
    return

if __name__ == "__main__":
    main()




