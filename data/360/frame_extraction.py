import cv2
import os
import glob
video_paths = glob.glob('Videos/*')
print(video_paths)
output_path = 'Videos_to_images/'
if not os.path.exists(output_path):
    os.makedirs(output_path)

img_name = 0
video_name = 0
for video_path in video_paths:
    cap = cv2.VideoCapture(video_path)
    index = 0
    while cap.isOpened():
        ret, mat = cap.read()
        if ret:
            index += 1
            if index % 30 != 0:
                continue
            cv2.imwrite(output_path +str(video_name)+ '-' + str(img_name) + '.png', mat)
            img_name += 1
        else:
            break
    cap.release()
    video_name += 1

print('Done')

