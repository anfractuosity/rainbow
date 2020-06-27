#!/usr/bin/python3

import os
import cv2
from PIL import Image, ImageFont, ImageDraw, ImageEnhance

cap = cv2.VideoCapture("trailer.mkv")
WIDTH=2048
HEIGHT=1536
scale=2

try:
    os.remove('out.txt')
except FileNotFoundError:
    ok = 1

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
            draw.rectangle(((x+0)*scale ,(y+0)*scale,((x+0)*scale)+scale,((y+0)*scale)+scale), fill=(b,b,b),outline=None,width=0)
            draw.rectangle(((x+1)*scale ,(y+0)*scale,((x+1)*scale)+scale,((y+0)*scale)+scale), fill=(g,g,g),outline=None,width=0)
            draw.rectangle(((x+0)*scale ,(y+1)*scale,((x+0)*scale)+scale,((y+1)*scale)+scale), fill=(g,g,g),outline=None,width=0)
            draw.rectangle(((x+1)*scale ,(y+1)*scale,((x+1)*scale)+scale,((y+1)*scale)+scale), fill=(r,r,r),outline=None,width=0)

    frames.write("""file frames/%d.png\nduration %f\n""" % (counter,1/24))
    img.save("""frames/%d.png""" % counter)

    if counter > 24*1:
        break

    counter += 1

frames.close()
# Should be Python library for this?
os.system("ffmpeg -f concat -i out.txt -framerate 24 -c:v libx264 out.mkv")

