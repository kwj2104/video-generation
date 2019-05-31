
# Importing all necessary libraries 
import cv2 
import numpy as np
import os 
import argparse
import random
from shutil import copyfile
  

parser = argparse.ArgumentParser()
parser.add_argument("--video")
parser.add_argument("--train_ratio", type=float)
args = parser.parse_args()

# path for pic data
data_path = "./data"
train_path = data_path + "/train"
val_path = data_path + "/val"
output_path = data_path + "/output" # path for pix2pix output
gen_path = data_path + "/gen" # path for all generated pics
os.mkdir(train_path)
os.mkdir(val_path)
os.mkdir(output_path)
os.mkdir(gen_path)

# Read the video from specified path 
cam = cv2.VideoCapture(args.video) 
  
try: 
    # creating a folder named data 
    if not os.path.exists('data'): 
        os.makedirs('data') 
# if not created then raise error 
except OSError: 
    print ('Error: Creating directory of data') 
  
# frame 
framecount = 0
ret,lastframe = cam.read() 
if not ret:
    print ('Error: No frames to read')
while(True): 
    
    # reading from frame 
    ret,currentframe = cam.read() 
  
    if ret: 
        # if video is still left continue creating images 
        name = '{}/frame{}.jpg'.format(data_path, framecount)
        print ('Creating...' + name) 
        # combine two consecutive frames along the y-axis
        combined_frame = np.concatenate((lastframe, currentframe), axis=1)
        # writing the extracted images 
        cv2.imwrite(name, combined_frame) 
  
        # increasing counter so that it will 
        # show how many frames are created 
        framecount += 1
        lastframe = currentframe
    else: 
        break
  
# Release all space and windows once done 
cam.release() 
cv2.destroyAllWindows() 

# split dataset
train_size = int(framecount * args.train_ratio)
val_size = framecount - train_size
for frameid in range(framecount):
    filepath = '{}/frame{}.jpg'.format(data_path, framecount)
    if frameid < train_size:
        os.rename(filepath, "{}/{}.jpg".format(train_path, frameid))
    else:
        os.rename(filepath, "{}/{}.jpg".format(val_path, frameid - train_size))

# randomly select an image from val set for generation
pic_id = random.randint(0, val_size - 1)
pic = cv2.imread("{}/{}.jpg".format(val_path, pic_id))
pic = pic[:, :len(pic[0])//2, :]
cv2.imwrite("{}/outputs.jpg".format(output_path), pic)