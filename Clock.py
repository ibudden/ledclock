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
        #options.show_refresh_rate = 1
        
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
            brightness = 1
            
            while True:
                # only update at 0 seconds
                time_now = datetime.datetime.now()
                time_pause = int(time_now.strftime("%-S"))
                
                if time_pause == 0:
                    # different brightness at different times
                    hour_of_day = int(time_now.strftime("%-H"))
                    if hour_of_day < 7:
                        brightness = 1
                    elif hour_of_day > 9:
                        brightness = 1
                    else:
                        brightness = 3
                    # draw a background
                    for y in range(0, self.matrix.height):        
                        graphics.DrawLine(self.matrix, 0, y, 31, y, graphics.Color(y*brightness, 0, 0))
                    # type time
                    time_string = time_now.strftime("%H:%M")
                    graphics.DrawText(self.matrix, font, xpos, ypos, textColor, time_string)
                    
                time.sleep(1)


        except KeyboardInterrupt:
            print("Exiting\n")
            sys.exit(0)
        

clock = Clock()
clock.start()
