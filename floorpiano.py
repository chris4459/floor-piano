import pygame
from pygame.locals import *

import pygame.mixer

# import RPi.GPIO as GPIO

# Modes
piano = True
guitar = False
drum = False

def converter(char):
	if char == 'a':
		play_1()
	elif char == 's':
		play_2()
	elif char == 'd':
		play_3()
	elif char == 'f':
		play_4()
	elif char == 'g':
		play_5()
	elif char == 'h':
		play_6()
	elif char == 'j':
		play_7()
	elif char == 'k':
		play_8()

def play_1():
	# GPIO.output(18,GPIO.HIGH)
	if piano:
		piano_c1.play(maxtime=800)
	elif guitar:
		guitar_1.play(maxtime=800)
	elif drum:
		drum_1.play(maxtime=800)

def play_2():
	# GPIO.output(17,GPIO.HIGH)
	if piano:
		piano_d.play(maxtime=800)
	elif guitar:
		guitar_2.play(maxtime=800)
	elif drum:
		drum_2.play(maxtime=800)

def play_3():
	if piano:
		piano_e.play(maxtime=800)
	elif guitar:
		guitar_3.play(maxtime=800)
	elif drum:
		drum_3.play(maxtime=800)

def play_4():
	if piano:
		piano_f.play(maxtime=800)
	elif guitar:
		guitar_4.play(maxtime=800)
	elif drum:
		drum_4.play(maxtime=800)

def play_5():
	if piano:
		piano_g.play(maxtime=800)
	elif guitar:
		guitar_5.play(maxtime=800)
	elif drum:
		drum_5.play(maxtime=800)

def play_6():
	if piano:
		piano_a.play(maxtime=800)
	elif guitar:
		guitar_6.play(maxtime=800)
	elif drum:
		drum_6.play(maxtime=800)

def play_7():
	if piano:
		piano_b.play(maxtime=800)
	elif guitar:
		guitar_7.play(maxtime=800)
	elif drum:
		drum_7.play(maxtime=800)

def play_8():
	if piano:
		piano_c2.play(maxtime=800)
	elif guitar:
		guitar_8.play(maxtime=800)
	elif drum:
		drum_8.play(maxtime=800)

def pattern1():
	print ("Starting pattern 1")
	sequence = ['a', 's', 'd', 'a', 'd', 'a', 'd', 's', 'd', 'f', 'f', 'd', 's', 'f']
	index = 0
	while index < len(sequence):
		for event in pygame.event.get():
			if event.type == KEYDOWN:
				letter = pygame.key.name(event.key)
				if letter == sequence[index]:
					index += 1
					print (":yay match")
					converter(letter)
				elif letter == 'p':
					print ("Exiting pattern1")
					return
				elif event.key == K_ESCAPE:
					print ("Exiting pattern1")
					return
def pattern2():
	print ("Starting star wars theme!")
	sequence = ['a', 'g', 'f', 'd', 's', 'k', 'g', 'f', 'd', 's', 'k', 'g', 'f', 'd', 'f', 's']
	index = 0
	while index < len(sequence):
		for event in pygame.event.get():
			if event.type == KEYDOWN:
				letter = pygame.key.name(event.key)
				if letter == sequence[index]:
					index += 1
					print (":yay match")
					converter(letter)
				elif letter == 'p':
					print ("Exiting pattern1")
					return
				elif event.key == K_ESCAPE:
					print ("Exiting pattern1")
					return


# def turnOffLEDLight(char):
# 	if char == 'a':
# 		GPIO.output(18,GPIO.LOW)
# 	elif char == 's':
# 		GPIO.output(17,GPIO.LOW)
		

if __name__=="__main__":
	pygame.display.set_mode((120, 120), DOUBLEBUF | HWSURFACE)
	pygame.mixer.pre_init(44100, -16, 2, 2048)
	pygame.mixer.init(channels=32, buffer=512)
	pygame.init()

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

	drum_1 = pygame.mixer.Sound("drum/BRUSH_SLAP_1.wav")
	drum_2 = pygame.mixer.Sound("drum/BRUSH_SWISH_1.wav")
	drum_3 = pygame.mixer.Sound("drum/CHINESE_TD_1.wav")
	drum_4 = pygame.mixer.Sound("drum/CRASH.wav")
	drum_5 = pygame.mixer.Sound("drum/LIGHT_SHOT.wav")
	drum_6 = pygame.mixer.Sound("drum/Piatti.wav")
	drum_7 = pygame.mixer.Sound("drum/Spark_metal.wav")
	drum_8 = pygame.mixer.Sound("drum/Timpani2.wav")

	# GPIO.setmode(GPIO.BCM)
	# GPIO.setwarnings(False)
	# GPIO.setup(17,GPIO.OUT)
	# GPIO.setup(18,GPIO.OUT)

	running = True
	while running:
		for event in pygame.event.get():
			if event.type == KEYDOWN:
				letter = pygame.key.name(event.key)
				converter(letter)
				if event.key == K_ESCAPE:
					running = False
				# Instrument switching
				elif event.key == pygame.K_q:
					piano = True
					guitar = False
					drum = False
				elif event.key == pygame.K_w:
					piano = False
					guitar = True
					drum = False
				elif event.key == pygame.K_e:
					piano = False
					guitar = False
					drum = True
				# Patterns
				elif event.key == pygame.K_z:
					pattern1()
				elif event.key == pygame.K_x:
					pattern2()
			elif event.type == KEYUP:
				letter = pygame.key.name(event.key)
				# turnOffLEDLight(letter)
				
