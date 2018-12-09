from createImage import *
import os
#print(os.listdir("../pictures"))
dir=os.listdir('../pictures')

filelist=[]
for file in dir:
    if file.endswith('.png'):
        filelist.append(file)
print(filelist)

for file in filelist:
    print('done')
    im = readImage('../pictures/'+file)
    black = oneColor(im, (0, 0, 0))
    imsave('./pictures/'+file.split('.')[0]+'_black'+'.png',black)
    processed = process(black, size=(5, 5), r=0.6)
    imsave('./pictures/'+file.split('.')[0]+'_black_less'+'.jpg',processed)
