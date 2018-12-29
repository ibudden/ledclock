#!/usr/bin/env python

import time
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/..'))

from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics


class Clock():
    
    def __init__(self): # , *args, **kwargs
        start(self)
    
        
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
            font.LoadFont("/home/pi/rpi-rgb-led-matrix/fonts/7x13.bdf")
            textColor = graphics.Color(255, 255, 0)
            pos = offscreen_canvas.width
            my_text = self.args.text

            while True:
                offscreen_canvas.Clear()
                len = graphics.DrawText(offscreen_canvas, font, pos, 10, textColor, my_text)
                pos -= 1
                if (pos + len < 0):
                    pos = offscreen_canvas.width

                time.sleep(0.05)
                offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)


        except KeyboardInterrupt:
            print("Exiting\n")
            sys.exit(0)
        

Clock()
