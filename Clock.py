#!/usr/bin/env python

import time
import datetime
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
            font.LoadFont("./6x13B.bdf")
            textColor = graphics.Color(0, 0, 0)
            
            xpos = 1
            ypos = 14
            brightness = 2

            while True:
                #offscreen_canvas.Clear()
                
                time_string = datetime.datetime.now().strftime("%H:%M")
                graphics.DrawText(self.matrix, font, xpos, ypos, textColor, time_string)
                
                for y in range(0, self.matrix.height):        
                    graphics.DrawLine(self.matrix, 0, y, 31, y, graphics.Color(y*brightness, 0, 0))
                
                #pos -= 1
                #if (pos + len < 0):
                #    pos = offscreen_canvas.width

                time.sleep(1)
                #offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)


        except KeyboardInterrupt:
            print("Exiting\n")
            sys.exit(0)
        

clock = Clock()
clock.start()
