import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Shooting Pygame')

#set framerate
clock = pygame.time.Clock()
FPS = 60

#define player action variable
moving_left = False
moving_right = False

#Background colour as RGB
BG = (144,201,120)

#draw bg

def draw_bg():
	screen.fill(BG)

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

	#function to move character
	def move(self, moving_left, moving_right):
		#reset movement variables
		dx = 0
		dy = 0

		#assign movement variables if moving left or right
		if moving_left:
			dx = -self.speed
		if moving_right:
			dx = self.speed

		#update rectangle position
		self.rect.x += dx
		self.rect.y += dy



	#function to draw itself on window
	def draw(self):
		screen.blit(self.img, self.rect)

#create soldier as them role
player = Soldier(200, 200, 3, 5)

#run the window
run = True
while run:
	#set framerate
	clock.tick(FPS)

	#draw bg
	draw_bg()

	#draw player
	player.draw()
	player.move(moving_left, moving_right)

	#loop check event
	for event in pygame.event.get():
		#check event to exit loop
		if event.type == pygame.QUIT:
			run = False
		#keyboard pressed event
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_a:
				moving_left = True

			if event.key == pygame.K_d:
				moving_right = True

			if event.key == pygame.K_ESCAPE:
				run = False

		#keyboard unpressed event // buntton released
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_a:
				moving_left = False

			if event.key == pygame.K_d:
				moving_right = False

	#update screen all the times
	pygame.display.update()

#close the window
pygame.quit()