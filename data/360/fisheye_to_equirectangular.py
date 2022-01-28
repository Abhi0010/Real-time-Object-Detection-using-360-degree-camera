import os
import cv2
import numpy
import matplotlib.pyplot as plt

class FisheyeToEqui:
    def fish_to_persp(image_path, persp_width = 800, persp_height = 600, fov_persp = 100, fov_fish = 180, center_x = 0 , center_y = 0, fish_radius_horizontal = 0, fish_radius_vertical= 0, tilt_angle = 0, roll_angle = 0, pan_angle = 0, anti_aliasing_level = 0, fourth_order_correction_a = None, fourth_order_correction_b = None, fourth_order_correction_c = None, fourth_order_correction_d = None, verbose = False):
        '''
        Usage: fish2persp [options] fisheyeimage
        Options
            -w n        perspective image width, default = 800
            -h n        perspective image height, default = 600
            -t n        field of view of perspective (degrees), default = 100
            -s n        field of view of fisheye (degrees), default = 180
            -c x y      center of the fisheye image, default is center of image
            -r n        fisheye radius (horizontal), default is half width of fisheye image
            -ry n       fisheye radius (vertical) for anamophic lens, default is circular fisheye
            -x n        tilt angle (degrees), default: 0
            -y n        roll angle (degrees), default: 0
            -z n        pan angle (degrees), default: 0 
            -a n        antialiasing level, default = 2
            -p n n n n  4th order lens correction, default: off
            -d          verbose mode, default: off
        '''
        