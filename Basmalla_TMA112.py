from turtle import* # import of turtle to can use all its functions
goto(0,0)  # the Starting position x=0,y=0
colors=['brown','red','magenta','blue','green','orange']#list of used colors
B=0  # B is the index of list
for i in range(1,37): # loop to draw the circles 36 times
                      #i is the variable to iterate on loop
    color(colors[B])  # start with the first color in list
    circle(100)    # draw a circle with raduis=100
    left(10)       # after each circle turn left with angle 10
    if i%6==0:  # check if i% 6 =0 
       B=B+1    # add 1 to B to change the color after each 6 circles
       color(colors[0]) 
    

 
