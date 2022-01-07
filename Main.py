#imports
import pygame
from pygame import constants
from pygame import mouse
from Board import BoardClass
import Square

#defines screen dimensions
HEIGHT = 600
WIDTH = 1000


font = pygame.font.Font('freesansbold.ttf', 50)

#main function
def main():
    pygame.init()

    #sets the screen dimensions
    screen = pygame.display.set_mode((WIDTH,HEIGHT))

    #sets the screen caption
    pygame.display.set_caption("Minesweeper")

    background = generate_background()
    screen.blit(background,(0,0))

    board = BoardClass(8,5,1)

    boardImage = board.getImage()
    screen.blit(boardImage,(100,100))

    mine_count = font.render(f"{board.num_mines}", (255,255,255),(0,0,0))
    mine_count_rect = mine_count.get_rect()
    mine_count_rect.top = 25
    mine_count_rect.left = 730
    screen.blit(mine_count, mine_count_rect)

    lostImage = pygame.image.load('Lost.png')
    wonImage = pygame.image.load('Won.png')

    hasLost = False
    hasWon = False

    while True:
        
        #Gets all events in queue
        for event in pygame.event.get():

            #Quits game
            if  event.type == constants.QUIT:
                pygame.quit()
                quit()

            if event.type == constants.MOUSEBUTTONDOWN:
                if not hasLost:
                    screen.blit(background,(0,0))
                    isLeft = pygame.mouse.get_pressed(num_buttons = 3)[0]
                    mousePos = event.pos
                    gameStatus = board.revealSquare(mousePos[0], mousePos[1], isLeft)
                    if gameStatus == "LOST":
                        hasLost = True
                    if gameStatus == "WON":
                        hasWon = True
                    boardImage = board.getImage()
                    screen.blit(boardImage,(100,100))
                    mine_count = font.render(f"{board.num_mines}", (255,255,255),(0,0,0))
                    mine_count_rect = mine_count.get_rect()
                    mine_count_rect.top = 25
                    mine_count_rect.left = 730
                    screen.blit(mine_count, mine_count_rect)
                    if hasLost:
                        screen.blit(lostImage, (0,0))
                    if hasWon:
                        screen.blit(wonImage, (0,0))

        

                
        #updates screen
        pygame.display.update()


#creates static background
def generate_background():
    #creates background color
    background_color = (217,217,217)
    background = pygame.Surface((WIDTH, HEIGHT))
    background.fill(background_color)
    #creates field
    play_area_color = (128,128,128)
    play_area = pygame.Surface((WIDTH-200, HEIGHT-100))
    play_area.fill(play_area_color)
    #places field on background
    background.blit(play_area,(100,100))
    #creates text for mines remaing
    black = (0,0,0)
    text = font.render('Mines Remaining',background_color,black)
    text_rect = text.get_rect()
    text_rect.center = (WIDTH/2, 50)
    background.blit(text,text_rect)
    #creates square for mines remaing
    white = (255,255,255)
    square = pygame.Surface((80,80))
    square.fill(white)
    square_rect = square.get_rect()
    square_rect.left = text_rect.right + 10
    square_rect.top = 10
    background.blit(square,square_rect)
    return background









#check is main
if __name__ == "__main__":
    main()