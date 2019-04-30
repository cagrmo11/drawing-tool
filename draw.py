#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 12:13:35 2019

@author: moran
"""

# -*- coding: utf-8 -*-

import stylus as st
import tools as t
import err_messages as em

        
if __name__ == '__main__':
    

    try:
        f = open("input/input.txt", "r")
        #f = open("input/tests/test_line.txt", "r")
        #f = open("input/tests/test_rectangle.txt", "r")
        #f = open("input/tests/test_backfill.txt", "r")
        
        for line in f:
            values = line.split()
            
            try:
                if values[0] ==  "C":
                    
                    if len(values) > 3:
                        print(em.too_many_args)
                        break
                    elif len(values) < 3:
                        print(em.not_enough_args)
                        break
                    else:
                        w = int(values[1])
                        h = int(values[2])
                        
                        your_canvas=t.drawCanvas(w,h)
                        t.prettyprint(your_canvas)
                    
                    
                elif values[0] ==  "L":
                    
                    try:
                        
                        if len(values) > 5:
                            print(em.too_many_args)
                            continue
                        elif len(values) < 5:
                            print(em.not_enough_args)
                            continue
                        else:
                            x1 = int(values[1])
                            y1 = int(values[2]) 
                            x2 = int(values[3])
                            y2 = int(values[4])      
                        
                        if x1 < 1 or y1 < 1 or y2 < 1 or x1 > (your_canvas.shape[1]-2) or x2 > (your_canvas.shape[1]-2) or y1 > (your_canvas.shape[0]-2) or y2 > (your_canvas.shape[0]-2):
                           print(em.too_far)
                           continue
                        else:
                            t.prettyprint(st.drawLine(your_canvas,x1,y1,x2,y2))         
                    except NameError:
                        print(em.no_canvas_message)
                        break
                    except:
                        print(em.err_message)
        
                    
                elif values[0] ==  "R":
                    
                    try:
                        if len(values) > 5:
                            print(em.too_many_args)
                            continue
                        elif len(values) < 5:
                            print(em.not_enough_args)
                            continue
                        else:
                            x1 = int(values[1])
                            y1 = int(values[2]) 
                            x2 = int(values[3])
                            y2 = int(values[4])
                            
                        if x1 < 1 or y1 < 1 or y2 > (your_canvas.shape[0]-2) or x2 > (your_canvas.shape[1]-2):
                            print(em.too_far)
                            continue
                        else:             
                            t.prettyprint(st.drawRectangle(your_canvas,x1,y1,x2,y2))
                    except NameError:
                        print(em.no_canvas_message)
                        break
                    except:
                        print(em.err_message)
                    
                    
                elif values[0] ==  "B":

                    try:
                        if len(values) > 4:
                            print(em.too_many_args)
                            continue
                        elif len(values) < 4:
                            print(em.not_enough_args)
                            continue
                        else:
                            x = int(values[1])
                            y = int(values[2])
                            c = values[3]
                           
                        if x < 0 or x > (your_canvas.shape[1]-2) or y > (your_canvas.shape[0]-2) < 1 or y < 1:
                            print(em.too_far)
                            continue
                        else:   
                            t.prettyprint(st.drawBackground(your_canvas,x,y,c))
                    except NameError:
                        print(em.no_canvas_message)
                        break
                    except:
                        print(em.err_message)
                
            except:
                print(em.err_message)
                
        print(em.check_drawing_message)
        
    except:
        print(em.input_txt_not_found)