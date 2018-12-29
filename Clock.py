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
            textColor = graphics.Color(40, 40, 40)
            
            xpos = 2
            ypos = 14
            my_text = datetime.datetime.now().strftime("%H:%M")

        while True:
            
            while True:
                offscreen_canvas.Clear()
                
                for y in range(0, self.matrix.height):
                    self.matrix.drawLine(0, y, 15, y, self.matrix.Color333(7, 0, 0));
                
                graphics.DrawText(offscreen_canvas, font, xpos, ypos, textColor, my_text)
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
