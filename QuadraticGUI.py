#
# Sylvia Chin
#
# Calculates a polynomial using the quadratic formula
    # Asks user for a, b, and c from the equation ax^2 + bx + c = 0
#
from graphics import *
import cmath

def graphQuadForm():
    # Create a graphics window, 600x600
    win = GraphWin("Graphics Quadratic Formula", 600, 600)
    
    # Display the standard equation ax^2 + bx + c = 0 for user reference
    standard = Text(Point(300, 150), "The standard equation is: ax^2 + bx + c = 0")
    standard.draw(win)    

    # Create three Entry boxes for a, b, and c respectively
        # Label them a, b, c
    aval = Entry(Point(200, 200), 20)
    alabel = Text(Point(200, 180), "Enter the value for a:")
    aval.draw(win)
    alabel.draw(win)
    
    bval = Entry(Point(200, 300), 20)
    blabel = Text(Point(200, 280), "Enter the value for b:")
    bval.draw(win)
    blabel.draw(win)
    
    cval = Entry(Point(200, 400), 20)
    clabel = Text(Point(200, 380), "Enter the value for c:")
    cval.draw(win)
    clabel.draw(win)

    # Display a "Calculate" button to use the quadratic formula when clicked
    buttonshape = Rectangle(Point(260, 550), Point(340, 520))
    buttonshape.draw(win)
    buttontext = Text(Point(300, 535), "Calculate")
    buttontext.draw(win)

    # Makes the program pause to evaluate inputs in Entry
        # Also works for calculate button
    win.getMouse()
        
    # Get the user input for each value
    a = eval(aval.getText())
    b = eval(bval.getText())
    c = eval(cval.getText())
    
    # Set up conditionals to determine if user values are valid
        # Calculate the discriminant b^2 - 4ac
        # No sol' if the discriminant < 0, one sol' = 0, two sol' > 0
    discriminant = b**2 - 4*a*c
    
    # Point that answer is displayed
    p = Point(450, 300)
    
    if discriminant > 0:
        val1 = (-b + discriminant**(1/2))/(2*a)
        val2 = (-b - discriminant**(1/2))/(2*a)
        # Display the solutions, rounded to two decimal points
        val1 = round(val1, 2)
        val2 = round(val2, 2)
        ans = Text(p, "The solutions to your quadratic are x = " + str(val1)
                   + ", " + str(val2))
        ans.draw(win)           
    elif discriminant == 0:
        val1 = (-b + discriminant**(1/2))/(2*a)
        # Display the solution, rounded to two decimal points
        val1 = round(val1, 2)
        ans = Text(p, "The solution to your quadratic is x = " + str(val1))
        ans.draw(win)  
    else:
        ans = Text(p, "There are no solutions to your quadratic")
        ans.draw(win)  
    
    # Display "Quit" instead of "Calculate" on the button
        # When clicked, close the program
    buttontext.setText("Quit")
    win.getMouse()
    win.close()

graphQuadForm()
