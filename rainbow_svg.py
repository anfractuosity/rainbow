#!/usr/bin/python3

import svgwrite

def monitor(width,height,wres,hres):

    pixw = (width / wres)*4
    pixh = (height / hres)*4

    dwg = svgwrite.Drawing('test.svg', profile='full',size=(str(width)+'mm',str(height)+'mm'))

    #dwg.add(dwg.line((0, 0), (10, 0), stroke=svgwrite.rgb(10, 10, 16, '%')))
    #dwg.add(dwg.text('Test', insert=(0, 0.2), fill='red'))


    for y in range(int(height / pixh)):
        print(y/int(height / pixh))

        for x in range(int(width / pixh)):

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

            square = dwg.rect(insert=(str(x*pixw)+"mm", str(y*pixh)+"mm"), size=(str(pixw)+"mm", str(pixh)+"mm"),fill=colour)
            dwg.add(square)

    dwg.save()

monitor(433.1,324.8,2048,1536)
#monitor(100,100,200,200)

