# coding=utf-8
import os
from PIL import Image
import sys


 
def extractFrames(inGif, outFolder):
    frame = Image.open(inGif)
    nframes = 0
    while frame:
        frame.save( '%s/%s-%s.png' % (outFolder, os.path.basename(inGif), nframes ) , 'PNG')
        nframes += 1
        try:
            frame.seek( nframes )
        except EOFError:
            break;
    return True

if not os.path.isdir("output"): os.makedirs("output") 

if len(sys.argv) >= 2:
        extractFrames(sys.argv[1], 'output')
        print "Imagen procesada";
else:
        print "Este programa necesita el nombre del gif como parametro";
        

