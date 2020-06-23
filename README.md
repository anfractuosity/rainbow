# rainbow

A silly idea to make my B&W monitor colour.

The idea is to overlay the bayer pattern, printed on acetate, over a B&W monitor, whilst displaying an appropriately created image, 
in the hopes the result appears like a colour image.

There are two scripts, one which generates a pdf file and the other an svg file.

With the pdf files, I find they seem to display best with foxitreader on Linux, when I use a large magnification > 1000%, there doesn't appear 
to be gaps between the squares, however strangely with evince there does even at 150% magnification.

The pdf script generation is faster for me than the svg version, especially at lower scales.

For the svg script you need to install svgwrite, via pip.

# To Do

* Add argument handling to the Python scripts, so that you can simply pass in your monitor resolution and size etc. to the script
