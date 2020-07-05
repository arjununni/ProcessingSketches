class Star:
    def __init__(self):
        self.x = random(1,width)
        self.y = random(1,height)
        self.w = random(2,6)
        self.wid = self.w
        
        self.px = 0
    
    def display(self):
        noStroke()
        
        fill(32,32,32)
        rect(self.x,self.y,self.w*1.5,self.w*1.5)
        
        fill(255)
        rect(self.x,self.y,self.w,self.w)
        
        fill(128)
        rect(self.px,self.y,self.w,self.w)
        
    def update(self, speed): 
        self.w = random(self.wid-2,self.wid+2)
        self.px = self.x
        self.x = self.x - (speed/2)
        if self.x < 0:
            self.x = width
            self.y = random(1,height)
            self.w = random(2,6)
            self.wid = self.w
        
