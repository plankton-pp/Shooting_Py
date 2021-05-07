import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Shooting Pygame')

#define player action variable
moving_left = False
moving_right = False

#create class as blueprint to call it many times
class Soldier(pygame.sprite.Sprite):
	#define type of soldier and its properties
					#define img position , #define scale
	def __init__(self, x, y, scale, speed):
		pygame.sprite.Sprite.__init__(self)
		#set speed
		self.speed = speed
		#load charactor img
		img = pygame.image.load('img/player/Idle/0.png')
											#convert to int 
											#change scale img
		self.img =  pygame.transform.scale(img, (int(img.get_width()*scale), int(img.get_height() * scale)))
		self.rect = self.img.get_rect()
		self.rect.center = (x, y)

#create soldier as them role
player = Soldier(200, 200, 3, 5)

#run the window
run = True
while run:
	#draw player
	player.draw()

	player.move(moving_left, moving_right)
	#loop check event
	for event in pygame.event.get():
		#check event to exit loop
		if event.type == pygame.QUIT:
			run = False

	#update screen all the times
	pygame.display.update()

#close the window
pygame.quit()