class Ground:
    dots = []
    
    def __init__(self,width,height):
        for i in range(50):
            self.xy = [0,0]
            self.xy[0] = random(1,width)
            self.xy[1] = random(3*height/4,height)
            self.dots.append(self.xy)
    
    def display(self):
        noStroke()
        fill(94,60,158)
        rect(0,3*height/4,width,height/4)
        
        fill(50,12,117)
        for i in self.dots:
            rect(i[0],i[1],5,5)
            rect(i[0]+5,i[1],5,5)
            
        fill(135,74,240)
        rect(0,3*height/4,width,10)
    
    def update(self,speed):
        for i in self.dots:
            i[0] -= speed
            
            if i[0] < 0:
                i[0] = width
                i[1] = random(3*height/4,height)
