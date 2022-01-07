import pygame
import os

pygame.init()

flagImage = pygame.image.load('Flag.png')
unrevealedImage = pygame.image.load("UnrevealedSquare.png")
mineImage = pygame.image.load("Mine.png")
colorDict = {
    1 : (0,0,255),
    2 : (0,255,0),
    3 : (255,0,0),
    4 : (255,255,0),
    5 : (255,0,255),
    6 : (0,255,255),
    7 : (100,100,100),
    8 : (0,0,0)
}

class SquareClass:
    

    def __init__(self,xPos_in,yPos_in,isMine_in):
        self.xPos = xPos_in
        self.yPos = yPos_in
        self.isMine = isMine_in
        self.isRevealed = False
        self.isFlagged = False
        self.number = 1
        self.font = pygame.font.Font('freesansbold.ttf', 50)
        self.baseRevealedImage = pygame.image.load("RevealedSquare.png")


    def __str__(self):
        return (f"{self.xPos}, {self.yPos}, {self.isMine}")
    
    def getImage(self):
        if self.isFlagged:
            return flagImage
        elif self.isRevealed:
            if self.isMine:
                return mineImage
            else:
                self.base = self.baseRevealedImage
                if self.number > 0:
                    self.text = self.font.render(f"{self.number}",(255,255,255), colorDict[self.number])
                    self.text_rect = self.text.get_rect()
                    self.text_rect.center = (50, 50)
                    self.base.blit(self.text,self.text_rect)
                return self.base
        else:
            return unrevealedImage
