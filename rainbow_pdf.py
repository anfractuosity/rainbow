#!/usr/bin/python3

import math,cairo

pt = 2.83465

def monitor(width,height,wres,hres,out,pattern,scale):

    pixw = (width / wres)*scale
    pixh = (height / hres)*scale

    surface = cairo.PDFSurface (out, width*pt, height*pt)
    ctx = cairo.Context (surface)
    ctx.set_source_rgb(1,1,1)
    ctx.rectangle(0,0,width*pt,height*pt)
    ctx.fill()

    for y in range(int(height / pixh)):
        print(y/int(height / pixh))
        z = 0
        for x in range(int(width / pixw)):
            if pattern == "bayer":
                if y % 2 == 0:
                    if x % 2 == 0:
                        colour = "#0000ff"
                        ctx.set_source_rgb(0,0,1)
                    else:
                        colour = "#00ff00"
                        ctx.set_source_rgb(0,1,0)
                else:
                    if x % 2 == 0:
                        colour = "#00ff00"
                        ctx.set_source_rgb(0,1,0)
                    else:
                        colour = "#ff0000"
                        ctx.set_source_rgb(1,0,0)
            else:   
                if z == 0:
                    ctx.set_source_rgb(1,0,0)
                    z += 1
                elif z == 1:
                    ctx.set_source_rgb(0,1,0)
                    z += 1
                elif z == 2:
                    ctx.set_source_rgb(0,0,1)
                    z = 0

            ctx.rectangle(x*pixw*pt,y*pixh*pt,pixw*round(pt,2),pixh*round(pt,2))
            #ctx.rectangle(x*pixw*pt,y*pixh*pt,pixw*pt,pixh*pt)
            ctx.fill()

    ctx.show_page()

monitor(433.1,324.8,2048,1536,"bayer_1.pdf","bayer",1)
monitor(433.1,324.8,2048,1536,"bayer_2.pdf","bayer",2)
monitor(433.1,324.8,2048,1536,"bayer_4.pdf","bayer",4)
#monitor(433.1,324.8,2048,1536,"rgb_4.pdf","rgb",4)

