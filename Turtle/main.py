from turtle import Turtle , Screen

tim_the_turtle=Turtle()

tim_the_turtle.shape("turtle")
tim_the_turtle.color("red")
# tim_the_turtle.forward(80)
# tim_the_turtle.right(90)
# tim_the_turtle.forward(80)
# tim_the_turtle.right(90)
# tim_the_turtle.forward(80)
# tim_the_turtle.right(90)
# tim_the_turtle.forward(80)

# #square used grpahics 
for _ in range (4):
    
    tim_the_turtle.forward(100)
    tim_the_turtle.right(90)

# dash dash line   - - - - - - - - - -  >
for _ in range(15):
    tim_the_turtle.pendown()      # 1. Put pen down
    tim_the_turtle.forward(10)    # 2. Draw a 10-pixel dash
    tim_the_turtle.penup()        # 3. Lift pen up
    tim_the_turtle.forward(10)    # 4. Skip a 10-pixel space
















screen=Screen()
screen.exitonclick()