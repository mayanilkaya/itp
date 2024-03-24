def setup():
    size(400, 400)

def drawObject(x,y,s):
    push()
    translate(x, y)
    scale(s)
    fill(0)
    line(50, 0, 50, 100)
    rect(25, 51, 50, 55)
    triangle(25, 50, 50, 10, 74, 50)
    pop()
    
def draw():
    drawObject(0,0,1)
    drawObject(0,150,1)
