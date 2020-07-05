import time

#init width and height
w = 400
h = 400

#gridScale - turns canvas into a gridScale x gridScale grid
gridScale = 20


class Snake:
    score = 1
    x = 0
    y = 0
    
    xspeed = 1
    yspeed = 0
    tail = []
    
    #deadcheck is a copy of the tail without the last two entries to check if the snake died
    deadcheck = []
    
    def update(self):
        #shift tail and add the newest position of the head
        if self.score>1:
            print(self.tail)
            for i in range(len(self.tail)-1):
                self.tail[i] = self.tail[i+1]
            self.tail[len(self.tail)-1] = [self.x,self.y]
            
        #copy tail to deadcheck and pop last two entries
        if self.score>2:
            self.deadcheck = self.tail[:]
            self.deadcheck.pop()
            self.deadcheck.pop()
        
        #movement
        if(self.x > width or self.x < 0):
            #if it reaches width edges
            self.x = abs(self.xspeed * (width - self.x)) - gridScale
        else:
            self.x += self.xspeed*gridScale
            
        if(self.y > height or self.y < 0):
            #if it reaches height edges
            self.y = abs(self.yspeed * (height - self.y))-gridScale
        else:
            self.y += self.yspeed*gridScale
            
    def show(self):
        #displays the snake
        for i in range(len(self.tail)):
            fill(random(1,255),random(1,255),random(1,255))
            rect(self.tail[i][0],self.tail[i][1],gridScale,gridScale)
            
        fill(255)
        rect(self.x,self.y,gridScale,gridScale)
        
    def scored(self):
        #if it scored, append the position to the tail
        self.tail.append([self.x,self.y])
    
    def death(self):
        #restart if died
        time.sleep(1)
        self.score = 1
        self.tail = []
        

class Food:
    x = 0
    y = 0
    
    def reLocate(self):
        #relocate food
        self.x = round(random(1,(w/gridScale)-1)) * gridScale
        self.y = round(random(1,(h/gridScale)-1)) * gridScale
        print(self.x, self.y)
                
        
s = Snake()
food = Food()
food.reLocate()
        
def setup():
    size(w,h)
    frameRate(10)
    print(s.score -1)

def draw():
    background(0)
    s.show()
    
    fill(255,0,0)
    rect(food.x,food.y,gridScale,gridScale)
    
    #print s.tail
    
    s.update()
    
    #check if food has been eaten
    if (abs(food.x - s.x) < 1 and abs(food.y - s.y) < 1):
        food.reLocate()
        s.score += 1
        s.scored()
        print(s.score -1)
    
    #check if hit itself
    for i in s.deadcheck:
        if (abs(i[0] - s.x) < 1 and abs(i[1] - s.y) < 1):
            s.death()
   

def keyPressed():
    if(keyCode == UP and s.yspeed != 1):
        s.xspeed = 0
        s.yspeed = -1
    if(keyCode == DOWN and s.yspeed != -1):
        s.xspeed = 0
        s.yspeed = 1
    if(keyCode == LEFT and s.xspeed != 1):
        s.xspeed = -1
        s.yspeed = 0
    if(keyCode == RIGHT and s.xspeed != -1):
        s.xspeed = 1
        s.yspeed = 0
    
    
