from curses.textpad import rectangle

import pygame

slide1 = pygame.image.load("1.png")
slide2 = pygame.image.load("2.png")
slide3 = pygame.image.load("3.png")
imagerect1 = slide1.get_rect()
imagerect2 = slide2.get_rect()
imagerect3 = slide3.get_rect()

screen = pygame.display.set_mode((0, 0),pygame.FULLSCREEN)
curImage = 0
curImRect = pygame.Rect(0, 0, 1920, 1080)
def main():
    pygame.init()
    imagecounter = 0
    while True:
        #screen.fill(black)
        # proceed events
        screen.fill((255, 255, 255), pygame.Rect(0, 0, 1920, 1080))
        for event in pygame.event.get():
            if imagecounter == 0:
                curImage = slide1
                curImRect = imagerect1
            elif imagecounter == 1:
                curImage = slide2
                curImRect = imagerect2
            elif imagecounter == 2:
                curImage = slide3
                curImRect = imagerect3
            screen.blit(curImage, curImRect)
            pygame.display.flip()
            ev = pygame.event.get()
            # handle MOUSEBUTTONUP
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                imagecounter+=1
                if imagecounter > 2:
                    imagecounter = 0


if __name__ == '__main__':
    main()

