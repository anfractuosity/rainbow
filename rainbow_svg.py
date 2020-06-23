#!/usr/bin/python3

import svgwrite

def monitor(width,height,wres,hres,out,pattern,scale):

    pixw = (width / wres)*scale
    pixh = (height / hres)*scale

    dwg = svgwrite.Drawing(out, profile='full',size=(str(width)+'mm',str(height)+'mm'))

    for y in range(int(height / pixh)):
        print(y/int(height / pixh))

        z = 0
        for x in range(int(width / pixw)):

            if y % 2 == 0:
                if x % 2 == 0:
                    colour = "#0000ff"
                else:
                    colour = "#00ff00"
            else:
                if x % 2 == 0:
                    colour = "#00ff00"
                else:
                    colour = "#ff0000"

            if pattern == "bayer":
                if y % 2 == 0:
                    if x % 2 == 0:
                        colour = "#0000ff"
                    else:
                        colour = "#00ff00"
                else:
                    if x % 2 == 0:
                        colour = "#00ff00"
                    else:
                        colour = "#ff0000"
            else:   
                if z == 0:
                    colour = "#ff0000"
                    z += 1
                elif z == 1:
                    colour = "#00ff00"
                    z += 1
                elif z == 2:
                    colour = "#0000ff"
                    z = 0

            square = dwg.rect(insert=(str(x*pixw)+"mm", str(y*pixh)+"mm"), size=(str(round(pixw,2))+"mm", str(round(pixh,2))+"mm"),fill=colour)
            dwg.add(square)

    dwg.save()

monitor(433.1,324.8,2048,1536,"bayer.svg","bayer",4)
monitor(433.1,324.8,2048,1536,"rgb.svg","rgb",4)
