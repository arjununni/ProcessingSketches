class Dog:
    
    def __init__(self,width,height):
        self.w = width
        self.h = height
        self.currentFrame = 0
        self.totFrame = 5
        self.walk = [0,0,0,0,0]
        self.ref = self.currentFrame
        
        self.walk[0] = loadImage("dog/1.png")
        self.walk[1] = loadImage("dog/2.png")
        self.walk[2] = loadImage("dog/3.png")
        self.walk[3] = loadImage("dog/4.png")
        self.walk[4] = loadImage("dog/5.png")
        
    def display(self,mode):
        dy = 0
        if mode == 1:
            dy = self.currentFrame
        image(self.walk[self.currentFrame], self.w/2-20,(3*self.h/4)-20-(dy*20))
        
    def update(self,speed):
        self.jumped = 0
        #print(speed)
        xspeed = map(speed, 1, 10, 0,1)
        self.ref = self.ref+xspeed
    
        if self.ref>self.currentFrame+0.5:
            self.currentFrame = self.currentFrame +1
            self.ref = self.currentFrame
            
        if self.currentFrame>self.totFrame-1:
            self.currentFrame = 0
            xspeed = 0
            self.ref = 0
