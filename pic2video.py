import cv2
import numpy as np
import glob
import argparse
import os 

parser = argparse.ArgumentParser()
parser.add_argument("--frames", type=int)
args = parser.parse_args()

img_array = []
dirpath = "./data/gen"
framenum = args.frames
for frameid in range(framenum):
    filename = "{}.jpg".format(frameid)
    filepath = os.path.join(dirpath, filename)
    if not os.path.isfile(filepath):
        continue
    img = cv2.imread(filepath)
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)

out = cv2.VideoWriter('gen.mp4',cv2.VideoWriter_fourcc(*'DIVX'), 24, size)
 
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()