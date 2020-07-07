#EPILEPSY WARNING
#THIS SKETCH CONTAINS FLASHING COLORS

def setup():
    size(800, 800)
    background(255)
    #noLoop()

def draw():
    background(random(255),random(255),random(255))
    translate(width/2,height/2)
    for n in range(5):
        stroke(random(255),random(255),random(255))
        for i in range(n*360, (n+1)*360):
            #x = random(50,150)
            #xx = random(150,350)
            pushMatrix()
            rotate(radians(i))
            strokeCap(ROUND)
            strokeWeight(4)
            line(mouseX,random(0,100),mouseY,0)
            popMatrix()
        
def mousePressed():
    redraw()
