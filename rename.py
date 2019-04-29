#-*-coding:utf-8-*-
#@author:lijinxi
import os.path

''' rename picture files '''
pictures_dir=os.path.join(os.path.curdir,"pictures")
pictures_list=os.listdir(pictures_dir)
i=0
j=0
for picture in pictures_list:
    if picture.endswith('.png'):
        i=i+1
        os.rename(os.path.join(pictures_dir,picture),os.path.join(pictures_dir,str(i)+'_processed.png'))
    else:
        j=j+1
        os.rename(os.path.join(pictures_dir,picture),os.path.join(pictures_dir,str(j)+"_truth.jpg"))
