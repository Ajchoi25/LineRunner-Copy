import pygame
from pygame.locals import *

class SmileB:
    # initialize all variables
    def __init__(self, newX, newY):
        self.x = newX
        self.y = newY
        self.up = False
        self.upCounter = 0
        self.img = pygame.image.load("SmileBlock.jpeg")
    
    # draw runningMan
    def draw(self, window):
        window.blit(self.img, (self.x,self.y))
        
        
    # move left unless you hit the edge
    def moveLeft(self):
        self.x -= 25
        if self.x < 0:
            self.x += 25
        
    # move left unless you hit the edge 
    def moveRight(self):
        self.x += 25
        myRect = self.getRec()
        if self.x +myRect[2] > 800:
            self.x -= 25
    
    # set the up variable to True
    def moveUp(self):
        if not self.up and self.upCounter == 0:
            self.up = True
        
    
    
    def update(self):
        """
        updates to upCounter and sets the up variable to
        false if upCounter has reached it's limit
        moves hopper up or down
        """
        if self.up:
            self.y -= 25
            self.upCounter += 1
            if self.upCounter > 4:
                self.up = False
        elif self.upCounter > 0:
            self.y += 25
            self.upCounter -= 1
    
    
    # determine if hopper has collided with an object 
    def collide(self, other):
        myRec = self.getRec()
        otherRec = other.getRec()
        oRight  = otherRec[0] + otherRec[2]
        oBottom  = otherRec[1] + otherRec[3]
    
        right = myRec[0] + myRec[2]
        bottom = myRec[1] + myRec[3]
        
        # if person is right of the object - person.x greater than (other.x + other.width)
        #    person and object do not intersect
        
        # elif person is left of the object
        #    person and object do not intersect
        
        # elif person is above the object
        #    person and object do not intersect
        
        # elif person is below the object
        #    person and object do not intersect
        
        # else
        #    person and object do intersect

        if (otherRec[0] <= right) and (oRight >= self.x) and (otherRec[1] <= bottom) and (oBottom >= self.y):
            return True
        return False

    
    def getRec(self):
        """
        This method returns a rectangle - (x, y, width, height) - that represents
        the object
        """
        myRec = self.img.get_rect()
        return (self.x, self.y, myRec[2], myRec[3])
