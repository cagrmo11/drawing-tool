import ink
import err_messages as em


#Create a line: Should create a new line from (x1,y1) to (x2,y2). Currently
#only horizontal or vertical lines are supported. Horizontal and vertical lines
#will be drawn using the 'x' character.
def drawLine(canvas, x1, y1, x2, y2):
    
    #Check if it's a horiztonal or vertical line
    #Loop through values in the array along the line 
    #Update value with point character
    try:
        #Handle diagonals   
        if x1 != x2 and y1 !=y2:
            print(em.diag_support)
                
        #Handle horizontal lines
        if x1 != x2:
            for i in range(x1,x2+1):
                canvas[y1][i]=ink.point

        #Handle vertical lines
        elif x1 == x2:
            for i in range(y1-1,y2+1):
                canvas[i][x1]=ink.point
    except:
        print(em.err_line_message)
        
    return canvas


#Create a rectangle: Should create a new rectangle, whose upper left
#corner is (x1,y1) and lower right corner is (x2,y2). Horizontal and vertical
#lines will be drawn using the 'x' character.
def drawRectangle(canvas, x1, y1, x2, y2):
    
    try:
        
        #Draw top and bottom lines
        drawLine(canvas,x1,y1,x2,y1)
        drawLine(canvas,x1,y2,x2,y2)
            
        #Draw right and left sides
        drawLine(canvas,x1,y2-1,x1,y2)
        drawLine(canvas,x2,y2-1,x2,y2)
    
    except:
        print(em.err_rect_message)
        
    return canvas


#Bucket Fill: Should fill the entire area connected to (x,y) with "colour" c.
#The behaviour of this is the same as that of the "bucket fill" tool in paint
#programs.
def drawBackground(canvas, x, y, c):
    
    try:

        if canvas[y][x] != "":  
            return canvas
        
        canvas[y][x] = c 
    
        drawBackground(canvas,x+1,y,c)
        drawBackground(canvas,x-1,y,c)
        drawBackground(canvas,x,y+1,c)
        drawBackground(canvas,x,y-1,c)
    
    except:
        print(em.err_back_message)
    
    return canvas