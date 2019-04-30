import numpy as np
import pandas as pd
import ink



#Create a canvas: Should create a new canvas of width w and height h.
def drawCanvas(w, h):

    #Declare canvas variables
    full_w = w+2
    full_h = h+2
    semi_w = w+1
    semi_h = h+1
            
    #Create empty numpy array according to width and height
    blank_canvas=np.empty((full_h, full_w), dtype='str')
    
    #Draw edges of the canvas by populating the outter edges of the array 
    #with "-" and "|" characters
    for i in (0,semi_h):
        blank_canvas[i,0:full_w] = ink.h_bar
    for i in range(1,semi_h):
        blank_canvas[i,0] = ink.v_bar
        blank_canvas[i,semi_w] = ink.v_bar
        
    return blank_canvas

    
def prettyprint(array):
    
    #Use for testing
    #print(pd.DataFrame(data=array[:,:]).to_string(index=False, header=False))
    #out = open("output/tests/output.txt", "a")

    out = open("output/output.txt", "a")
    print(pd.DataFrame(data=array[:,:]).to_string(index=False, header=False),file=out)
    out.close()