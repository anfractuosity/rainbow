#!/usr/bin/python3

import cv2
from PIL import Image, ImageFont, ImageDraw, ImageEnhance

cap = cv2.VideoCapture("trailer.mkv")
WIDTH=2048
HEIGHT=1536
scale=2

frames = open('out.txt', 'a')
img = Image.new('RGB', (WIDTH, HEIGHT), color = 'black')
draw = ImageDraw.Draw(img)

counter = 0
skip = 0

while(True):

    ret, frame = cap.read()
    orig = frame.copy()
    skip += 1

    if skip < 24*48:
        continue
    
    for y in range(0,int(HEIGHT/scale),2):
        for x in range(0,int(WIDTH/scale),2):
            b,g,r = orig[y,x]
            tmp = [r,g,b]
            draw.rectangle(((x+0)*scale ,(y+0)*scale,((x+0)*scale)+scale,((y+0)*scale)+scale), fill=(tmp[2],tmp[2],tmp[2]),outline=None,width=0)
            draw.rectangle(((x+1)*scale ,(y+0)*scale,((x+1)*scale)+scale,((y+0)*scale)+scale), fill=(tmp[1],tmp[1],tmp[1]),outline=None,width=0)
            draw.rectangle(((x+0)*scale ,(y+1)*scale,((x+0)*scale)+scale,((y+1)*scale)+scale), fill=(tmp[1],tmp[1],tmp[1]),outline=None,width=0)
            draw.rectangle(((x+1)*scale ,(y+1)*scale,((x+1)*scale)+scale,((y+1)*scale)+scale), fill=(tmp[0],tmp[0],tmp[0]),outline=None,width=0)

    frames.write("""file frames/%d.png\nduration %f\n""" % (counter,1/24))
    img.save("""frames/%d.png""" % counter)

    counter += 1

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    if counter > 24*60:
        break
