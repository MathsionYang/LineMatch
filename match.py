from os.path import join
from os import walk
import numpy as np
from sys import  argv
import cv2

floder=argv[1]
query=cv2.imread(join(floder,'tattoo_seed.jpg'))

files=[]
images=[]
descriptors=[]
for (dirpath,dirname,filenames) in walk(floder):
    files.extend(filenames)
    for f in files:
        if f.endswith('npy') and f!='tattoo_seed.npy':
            descriptors.append(f)
    print(descriptors)

sift=cv2.xfeatures2d.SIFT_create()
query_ky,query_dx=sift.detectAndCompute(query,None)

FLANN_INDEX_KDTREE=0
index_params=dict(algorithm=FLANN_INDEX_KDTREE,trees=5)
search_params=dict(checks=50)
flann=cv2.FlannBasedMatcher(index_params,search_params)