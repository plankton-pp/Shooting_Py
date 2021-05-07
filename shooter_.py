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
	def __init__(self, char_type, x, y, scale, speed):
		pygame.sprite.Sprite.__init__(self)
		#set char type
		self.char_type = char_type
		#set speed
		self.speed = speed
		#set direction and flip
		self.direction = 1
		self.flip = False
		#load charactor img
		img = pygame.image.load(f'img/{self.char_type}/Idle/0.png')
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
			self.flip = True
			self.direction = -1
		if moving_right:
			dx = self.speed
			self.flip = False
			self.direction = 1

		#update rectangle position
		self.rect.x += dx
		self.rect.y += dy



	#function to draw itself on window
	def draw(self):
					#Flip the image      #sourceIMG  #Flip_condition	#position to draw on screen
		screen.blit(pygame.transform.flip(self.img, self.flip, False), self.rect)

#create soldier as them role
player = Soldier('player',200, 200, 3, 5)
enemy = Soldier('enemy',200, 200, 3, 5)

#run the window
run = True
while run:
	#set framerate
	clock.tick(FPS)

	#draw bg
	draw_bg()

	#draw player
	player.draw()
	enemy.draw()
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