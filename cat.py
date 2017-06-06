#coding=uft-8
import pygame

...
  1.
...

if __name__ == "__main__":

	screen = pygame.display.set_mode((480,890),0,32)

	background = pygame.image.load("C:\Users\Administrator\Desktop\abc.jpg").convert()


	while True:
		screen.blit(background,(0,0))
		pygame.display.update()