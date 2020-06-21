#!/usr/bin/python3

import math,cairo

pt = 2.83465


#ctx.show_page()


def monitor(width,height,wres,hres,out,pattern):

    pixw = (width / wres)*1
    pixh = (height / hres)*1

    #dwg = svgwrite.Drawing('test.svg', profile='full',size=(str(width)+'mm',str(height)+'mm'))
    surface = cairo.PDFSurface (out, width*pt, height*pt)
    ctx = cairo.Context (surface)
    ctx.set_source_rgb(1,1,1)
    ctx.rectangle(0,0,width*pt,height*pt)
    ctx.fill()

    #dwg.add(dwg.line((0, 0), (10, 0), stroke=svgwrite.rgb(10, 10, 16, '%')))
    #dwg.add(dwg.text('Test', insert=(0, 0.2), fill='red'))

    for y in range(int(height / pixh)):
        print(y/int(height / pixh))

        z = 0
        for x in range(int(width / pixh)):
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

            ctx.rectangle(x*pixw*pt, y*pixh*pt, pixw* 2.84,pixh* 2.84)
            #ctx.rectangle(x*pixw*pt, y*pixh*pt, pixw*pt,pixh*pt)
            ctx.fill()

    ctx.show_page()

monitor(433.1,324.8,2048,1536,"bayer.pdf","bayer")
monitor(433.1,324.8,2048,1536,"rgb.pdf","rgb")

