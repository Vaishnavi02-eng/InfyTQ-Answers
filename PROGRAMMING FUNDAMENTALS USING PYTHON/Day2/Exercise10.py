import turtle 
wn = turtle.Screen()        # creates a graphics window
wn.setup(540,508)           # set window dimension

alex = turtle.Turtle()      # create a turtle named alex
alex.shape("turtle")        # alex looks like a turtle
alex.color("blue")          # alex has a color

dest = input()
if(dest == "south") :
    alex.right(90)
    alex.forward(50)
    
elif(dest =="north"):
    alex.left(90)
    alex.forward(50)
elif(dest =="west"):
    alex.right(180)
    alex.forward(50)
elif(dest =="east"):
    alex.forward(50)
else:
    alex.write("Looks like you have typed wrong destination")
#Write the logic to take the turtle to its destination
#Refer the statements given above to draw the pattern

#Provide different values and test your program
destination="south"
