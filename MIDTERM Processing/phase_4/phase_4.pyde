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
    for x in range(400, 0, 20):
        drawObject(x, y, 20)
        for y in range(0, 400, 20):
            drawObject(x, y, 20)
