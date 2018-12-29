#!/usr/bin/env python

import time
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/..'))

from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics


class Clock():
    
    def __init__(self): # , *args, **kwargs
        print("Initialising...")
    
    def start(self):
        
        options = RGBMatrixOptions()
        options.rows = 16
        options.cols = 32
        
        self.matrix = RGBMatrix(options = options)

        try:
            # Start loop
            print("Press CTRL-C to stop sample")

            offscreen_canvas = self.matrix.CreateFrameCanvas()
            font = graphics.Font()
            font.LoadFont("/home/pi/rpi-rgb-led-matrix/fonts/6x13O.bdf")
            textColor = graphics.Color(50, 50, 50)
            
            xpos = 1
            ypos = 16
            my_text = "15:49"

            while True:
                offscreen_canvas.Clear()
                len = graphics.DrawText(offscreen_canvas, font, xpos, ypos, textColor, my_text)
                #pos -= 1
                #if (pos + len < 0):
                #    pos = offscreen_canvas.width

                time.sleep(1)
                offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)


        except KeyboardInterrupt:
            print("Exiting\n")
            sys.exit(0)
        

clock = Clock()
clock.start()
