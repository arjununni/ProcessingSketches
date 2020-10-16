#EPILEPSY WARNING
#THIS SKETCH CONTAINS FLASHING COLORS
#V2 LESS RANDOM MORE COLOR

colors = ["#ff0000", "#feb30f", "#0aa4f7", "#000000", "#ffffff"]
weights = [1,2,2,1,1,0]
x=0

def setup():
    size(800, 800)
    colorMode(HSB, 360, 100, 100, 100);
    background(0,0,0)
    #noLoop()

def draw():
    translate(width/2,height/2)
    for n in range(1):
        stroke(generateColor())
        for i in range(n*360, (n+1)*360):
            #x = random(50,150)
            #xx = random(150,350)
            pushMatrix()
            rotate(radians(x+(i/2)))
            strokeCap(SQUARE)
            strokeWeight(3)
            line(mouseX,random(0,n)/2,mouseY,0)
            popMatrix()
    
    if mouseX==width and mouseY==width:
        background(0,0,0)
        
def mousePressed():
    global x
    if x==180:
        background(0);
        x=0
    else:
        background(0);
        x=180
    redraw()

#COLOR GENERATOR CODE

def generateColor():
  temp = myRandom(colors, weights)
  myColor = color(hue(temp) + randomGaussian()*10,
                  saturation(temp) + randomGaussian()*10,
                  brightness(temp)*0.75, 
                  random(0,50))

  return myColor

def myRandom(colors, weights):
    sum = 0

    for i in range(len(colors)):
        sum += weights[i]

    rr = random(0, sum)

    for j in range(len(weights)):
        if (weights[j] >= rr):
            return colors[j]
        rr -= weights[j]
