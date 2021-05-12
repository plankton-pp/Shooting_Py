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
		#set alive to char
		self.alive = True
		#set char type
		self.char_type = char_type
		#set speed
		self.speed = speed
		#set direction and flip
		self.direction = 1
		self.flip = False
		#img array of character to play when it updated movement
		self.animation_list = []
		self.frame_index = 0
		self.action = 0
		#start time when create the character
		self.update_time = pygame.time.get_ticks()
		#load charactor img into img_array
		#it's not the process to changed it the preparing item when start the game
		#animate functio is update_animation() below
		tmp_list = []
		for i in range(5):
			#load img
			img = pygame.image.load(f'img/{self.char_type}/Idle/{i}.png')
											#convert to int 
											#change scale img
			img =  pygame.transform.scale(img, (int(img.get_width()*scale), int(img.get_height() * scale)))
			#appending img into array
			tmp_list.append(img)
		self.animation_list.append(tmp_list)
		#set tmp list to empty
		tmp_list = []
		for i in range(6):
			#load img
			img = pygame.image.load(f'img/{self.char_type}/Run/{i}.png')
											#convert to int 
											#change scale img
			img =  pygame.transform.scale(img, (int(img.get_width()*scale), int(img.get_height() * scale)))
			#appending img into array
			tmp_list.append(img)
		self.animation_list.append(tmp_list)
		self.img = self.animation_list[self.action][self.frame_index]
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

	#update animation
	def update_animation(self):
		#every 100 millisec the char will be animated
		#frequentcy time to update
		#unit : millisec
		ANIMATION_COOLDOWN = 100
		#update image time depending on current frame
		self.img = self.animation_list[self.action][self.frame_index]
		#check if enough time has passed since the last update
		if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
			self.update_time = pygame.time.get_ticks()
			self.frame_index += 1
		#check if frame index is out of bound of animationlist (img array)
		if self.frame_index >= len(self.animation_list[self.action]):
			self.frame_index = 0
	#update action
	def update_action(self, new_action):
		#check if the new action is different to the previous on
		if new_action != self.action:
			self.action = new_action
			#update the animation setting
			self.frame_index = 0
			self.update_time = pygame.time.get_ticks()

	#function to draw itself on window
	def draw(self):
					#Flip the image      #sourceIMG  #Flip_condition	#position to draw on screen
		screen.blit(pygame.transform.flip(self.img, self.flip, False), self.rect)

#create soldier as them role
#player
player = Soldier('player',200, 200, 3, 5)
#enemy
enemy = Soldier('enemy',700, 200, 3, 5)

#run the window
run = True
while run:
	#set framerate
	clock.tick(FPS)

	#draw bg
	draw_bg()

	player.update_animation()
	#draw player
	player.draw()
	enemy.draw()

	#update player actions
	#change stage to run
	#stage 0 = idle
	#stage 1 = running
	if moving_right or moving_left:
		player.update_action(1)
	#change stage to idle
	else:
		player.update_action(0)
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