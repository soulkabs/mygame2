import pygame
import time
import math
import random
import bullet
import enemy

sx=500
sy=500
window=pygame.display.set_mode((sx,sy))
screen = pygame.Surface((sx,sy))
screenfon=pygame.image.load(('game_res/images/fon.png'))
screen.blit(screenfon,(0,0))

bullets=[]
enemys=[]


while True:
	#screen.blit(screenfon,(0,0))
	pygame.draw.rect(screen,(0,0,0),(0,0,sx,sy))
	pygame.draw.line(screen,(0,255,0),(sx/2-50,sy),(sx/2-50,sy-50))
	pygame.draw.line(screen,(0,255,0),(sx/2-50,sy-50),(sx/2+50,sy-50))
	pygame.draw.line(screen,(0,255,0),(sx/2+50,sy-50),(sx/2+50,sy))

	if len(enemys)<10:
		size=random.randint(10,15)
		enemys.append(enemy.Enemy(random.randint(0,sx-size),0,size,random.randint(1,5)/10))

	mx,my=pygame.mouse.get_pos()
	mx=mx-sx/2
	my=my-sy
	norm=math.sqrt(mx*mx+my*my)
	mx=mx/norm
	my=my/norm
	#print(math.sqrt(mx*mx+my*my))

	length=50

	pygame.draw.line(screen,(0,255,0),(sx/2,sy-25),(sx/2+length*mx,sy-25+length*my))
 	
	'''Обработчик событий'''
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
			bullets.append(bullet.Bullet(sx/2+length*mx,sy-25+length*my,mx,my,random.randint(5,15)/10))


	for i in enemys:
		pygame.draw.rect(screen,(255,255,0),(i.x, i.y, i.size, i.size))
		i.step()

	for i in bullets:
		pygame.draw.line(screen,(255,0,0),(i.x, i.y),(i.x+i.nx*25, i.y+i.ny*25))
		i.step()

	def intersects(bullet,enemys):
		x,y=bullet.x+bullet.nx*25, bullet.y+bullet.ny*25
		for i in enemys:
			if x > i.x and x < i.x + i.size and y >i.y and y < i.y +i.size:
				i.destroyed = True
				return True
		return False


	bullets = [b for b in bullets if b.x >0 and b.y >0 and b.x < sx and b.y < sy and not intersects(b, enemys)]

	enemys = [e for e in enemys if e.y < sy and not e.destroyed]



	window.blit(screen,(0,0))
	pygame.display.flip()
	time.sleep(0.001)

