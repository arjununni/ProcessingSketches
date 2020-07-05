import Star
import Ground
import Dog

w = 480
h = 640
stars = []
gnd = Ground.Ground(w,h)

def setup():
    size(w,h)
    background(0)
    frameRate(30)
    
    global dog
    dog = Dog.Dog(w,h)
    
    for i in range(70):
        stars.append(Star.Star())
        

def draw():
    global dog
    background(0)
    speed = map(mouseX, 0, width, 3, 15)
    
    for i in stars:
        i.update(speed)
        i.display()
        
    gnd.display()
    gnd.update(speed)
    
    mode = (mouseButton==LEFT)
    print(mode)
    dog.display(mode)
    dog.update(speed)
