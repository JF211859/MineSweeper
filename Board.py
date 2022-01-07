from Square import SquareClass
import random
import pygame

class BoardClass:

    def __init__(self, width_in, height_in, num_mines_in):
        self.width = width_in
        self.height = height_in
        self.num_mines = num_mines_in
        self.squares = []
        self.squaresRemaining = (self.width*self.height)-self.num_mines
        self.mines = set({})

        while len(self.mines) < self.num_mines:
            x = random.randint(0,self.width-1)
            y = random.randint(0,self.height-1)
            self.mines.add((x,y))

        for x in range(self.width):
            row = []
            for y in range(self.height):
                if (x,y) in self.mines:
                    row.append(SquareClass(x,y,True))
                else:
                    row.append(SquareClass(x,y,False))
            self.squares.append(row)

        self.assignNumbers()

    def __str__(self):
        string = ""
        for x in range(self.width):
            for y in range(self.height):
                string = string + str(self.squares[x][y]) + "\n"
        return string
    
    def getImage(self):
        base = pygame.Surface((800,500))
        for x in range(self.width):
            for y in range(self.height):
                base.blit(self.squares[x][y].getImage(),(x*100,y*100))
        return base

    def revealSquare(self,mouseX,mouseY,isLeft):
        mouseX -= 100
        mouseY -= 100
        xPos = int(mouseX / 100)
        yPos = int(mouseY / 100)
        if isLeft and (not self.squares[xPos][yPos].isFlagged) and (not self.squares[xPos][yPos].isRevealed):
            self.squares[xPos][yPos].isRevealed = True
            if self.squares[xPos][yPos].isMine:
                return "LOST"
            else:
                self.squaresRemaining -= 1
                if self.squaresRemaining == 0:
                    return "WON"
        elif self.num_mines > 0 and (not self.squares[xPos][yPos].isFlagged) and (not self.squares[xPos][yPos].isRevealed):
            self.squares[xPos][yPos].isFlagged = True
            self.num_mines -= 1
        elif self.squares[xPos][yPos].isFlagged and not isLeft:
            self.squares[xPos][yPos].isFlagged = False
            self.num_mines += 1
        return False

    def assignNumbers(self):
        directions = [
            (-1,1),
            (0,1),
            (1,1),
            (1,0),
            (1,-1),
            (0,-1),
            (-1,-1),
            (-1,0)
        ]
        for x in range(self.width):
            for y in range(self.height):
                totalNeighbors = 0
                for direction in directions:
                    if 0 <= x+direction[0] and x+direction[0] < self.width \
                    and 0 <= y+direction[1] and y+direction[1] < self.height \
                    and self.squares[x+direction[0]][y+direction[1]].isMine:
                        totalNeighbors += 1
                self.squares[x][y].number = totalNeighbors
