import pygame
pygame.init()
screen = pygame.display.set_mode([800,600])
keep_going = True
pic = pygame.image.load("dvd.bmp")
colorkey = pic.get_at((0,0))
pic.set_colorkey(colorkey)  # this and previous are optional, only fix black corners
picx = 0
speedx = 5
speedy = 5
picy = 0
BLACK = (0,0,0)
timer = pygame.time.Clock()
while keep_going:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			keep_going = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			pygame.display.set_caption("I see you.")
	picx += speedx
	picy += speedy
	screen.fill(BLACK)
	screen.blit(pic, (picx, picy))
	pygame.display.update()
	timer.tick(60)
	if picx + pic.get_width() > 800:
		speedx = -speedx
	if picx <= 0:
		speedx = -speedx
	if picy + pic.get_height() > 600:
		speedy = -speedy
	if picy <= 0:
		speedy = -speedy
pygame.quit()
