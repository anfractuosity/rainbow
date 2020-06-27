#!/usr/bin/python3

import os
import math
import time
import sdl2
import sdl2.ext
from PIL import Image, ImageFont, ImageDraw, ImageEnhance

sdl2.ext.init()

WIDTH = 2048
HEIGHT = 1536

window = sdl2.ext.Window("Display", size=(WIDTH, HEIGHT),position=(1920,0),flags=sdl2.SDL_WINDOW_FULLSCREEN)
renderer = sdl2.ext.Renderer(window,flags=sdl2.render.SDL_RENDERER_ACCELERATED) #| sdl2.render.SDL_RENDERER_PRESENTVSYNC)
windowsurface = window.get_surface()
window.show()

im = Image.open(os.path.join("test","test5.jpg"))
pix = im.load()

def draw_mosaic():

    img = Image.new('RGB', (WIDTH, HEIGHT), color = 'black')
    draw = ImageDraw.Draw(img)

    scale = 2
    for y in range(0,int(HEIGHT/scale),2):
        for x in range(0,int(WIDTH/scale),2):

            tmp = pix[x+200,y+200]
            color = sdl2.ext.Color(tmp[2],tmp[2],tmp[2]) # b
            sdl2.ext.fill(windowsurface, color, ((x+0)*scale , (y+0)*scale, scale, scale))
            draw.rectangle(((x+0)*scale ,(y+0)*scale,((x+0)*scale)+scale,((y+0)*scale)+scale), fill=(tmp[2],tmp[2],tmp[2]),outline=None,width=0)

            color = sdl2.ext.Color(tmp[1],tmp[1],tmp[1]) # g
            sdl2.ext.fill(windowsurface, color, ((x+1)*scale , (y+0)*scale, scale, scale))
            draw.rectangle(((x+1)*scale ,(y+0)*scale,((x+1)*scale)+scale,((y+0)*scale)+scale), fill=(tmp[1],tmp[1],tmp[1]),outline=None,width=0)

            color = sdl2.ext.Color(tmp[1],tmp[1],tmp[1]) # g
            sdl2.ext.fill(windowsurface, color, ((x+0)*scale , (y+1)*scale, scale, scale))
            draw.rectangle(((x+0)*scale ,(y+1)*scale,((x+0)*scale)+scale,((y+1)*scale)+scale), fill=(tmp[1],tmp[1],tmp[1]),outline=None,width=0)

            color = sdl2.ext.Color(tmp[0],tmp[0],tmp[0]) # r
            sdl2.ext.fill(windowsurface, color, ((x+1)*scale , (y+1)*scale, scale, scale))
            draw.rectangle(((x+1)*scale ,(y+1)*scale,((x+1)*scale)+scale,((y+1)*scale)+scale), fill=(tmp[0],tmp[0],tmp[0]),outline=None,width=0)
    
    img.save('out.png')
    window.refresh()

draw_mosaic()

while True:
    events = sdl2.ext.get_events()
    for event in events:
        if event.type == sdl2.SDL_KEYDOWN:
            quit()
    time.sleep(1)

