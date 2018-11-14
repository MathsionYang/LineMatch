
import cv2
import numpy as np
from os import  walk
from os.path import join
import sys

def create_descriptors(folder):
    files=[]
    for(dirpath,dirnames,filenames)  in walk(folder):
        files.extend(filenames)
    for f in files:
       save_descriptor(folder,f,cv2.xfeatures2d.SIFT_create())

def save_descriptor(floder,image_path,feature_detector):
    img=cv2.imread(join(floder,image_path),0)
    keypoints,descriptors=feature_detector.detectAndCompute(img,None)
    descriptor_file=image_path.replace('jpg','npy')
    np.save(join(floder,descriptor_file),descriptors)
dir=sys.argv[1]
dir=r'images'    #相对路径
create_descriptors(dir)
