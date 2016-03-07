import pygame
from pygame.locals import *

import pygame.mixer

# Modes
piano = True
guitar = False

def play_1():
	if piano:
		piano_c1.play()
	elif guitar:
		guitar_1.play()

def play_2():
	if piano:
		piano_d.play()
	elif guitar:
		guitar_2.play()

def play_3():
	if piano:
		piano_e.play()
	elif guitar:
		guitar_3.play()

def play_4():
	if piano:
		piano_f.play()
	elif guitar:
		guitar_4.play()

def play_5():
	if piano:
		piano_g.play()
	elif guitar:
		guitar_5.play()

def play_6():
	if piano:
		piano_a.play()
	elif guitar:
		guitar_6.play()

def play_7():
	if piano:
		piano_b.play()
	elif guitar:
		guitar_7.play()

def play_8():
	if piano:
		piano_c2.play()
	elif guitar:
		guitar_8.play()

if __name__=="__main__":
	pygame.display.set_mode((120, 120), DOUBLEBUF | HWSURFACE)
	pygame.init()
	pygame.mixer.init(channels=16, buffer=4096)

	piano_c1 = pygame.mixer.Sound("piano/c1.wav")
	piano_d = pygame.mixer.Sound("piano/d.wav")
	piano_e = pygame.mixer.Sound("piano/e.wav")
	piano_f = pygame.mixer.Sound("piano/f.wav")
	piano_g = pygame.mixer.Sound("piano/g.wav")
	piano_a = pygame.mixer.Sound("piano/a.wav")
	piano_b = pygame.mixer.Sound("piano/b.wav")
	piano_c2 = pygame.mixer.Sound("piano/c2.wav")

	guitar_1 = pygame.mixer.Sound("guitar/c.wav")
	guitar_2 = pygame.mixer.Sound("guitar/d.wav")
	guitar_3 = pygame.mixer.Sound("guitar/e.wav")
	guitar_4 = pygame.mixer.Sound("guitar/g.wav")
	guitar_5 = pygame.mixer.Sound("guitar/a.wav")
	guitar_6 = pygame.mixer.Sound("guitar/dmin.wav")
	guitar_7 = pygame.mixer.Sound("guitar/emin.wav")
	guitar_8 = pygame.mixer.Sound("guitar/gmin.wav")

    
	running = True
	while running:
		for event in pygame.event.get():
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					running = False
				# Instrument switching
				elif event.key == pygame.K_q:
					piano = True
					guitar = False
				elif event.key == pygame.K_w:
					piano = False
					guitar = True
				elif event.key == pygame.K_a:
					play_1()
				elif event.key == pygame.K_s:
					play_2()
				elif event.key == pygame.K_d:
					play_3()
				elif event.key == pygame.K_f:
					play_4()
				elif event.key == pygame.K_g:
					play_5()
				elif event.key == pygame.K_h:
					play_6()
				elif event.key == pygame.K_j:
					play_7()
				elif event.key == pygame.K_k:
					play_8()
