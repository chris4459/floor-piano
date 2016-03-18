import pygame
from pygame.locals import *

import pygame.mixer

# import RPi.GPIO as GPIO

# Modes
piano = True
guitar = False
drum = False
violin = False

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
	# GPIO.output(11,GPIO.HIGH)
	if piano:
		piano_c1.play(maxtime=800)
	elif guitar:
		guitar_1.play(maxtime=800)
	elif drum:
		drum_1.play(maxtime=800)
	elif violin:
		violin_c1.play(maxtime=800)

def play_2():
	# GPIO.output(12,GPIO.HIGH)
	if piano:
		piano_d.play(maxtime=800)
	elif guitar:
		guitar_2.play(maxtime=800)
	elif drum:
		drum_2.play(maxtime=800)
	elif violin:
		violin_d.play(maxtime=800)

def play_3():
	# GPIO.output(13,GPIO.HIGH)
	if piano:
		piano_e.play(maxtime=800)
	elif guitar:
		guitar_3.play(maxtime=800)
	elif drum:
		drum_3.play(maxtime=800)
	elif violin:
		violin_e.play(maxtime=800)

def play_4():
	# GPIO.output(14,GPIO.HIGH)
	if piano:
		piano_f.play(maxtime=800)
	elif guitar:
		guitar_4.play(maxtime=800)
	elif drum:
		drum_4.play(maxtime=800)
	elif violin:
		violin_f.play(maxtime=800)

def play_5():
	# GPIO.output(15,GPIO.HIGH)
	if piano:
		piano_g.play(maxtime=800)
	elif guitar:
		guitar_5.play(maxtime=800)
	elif drum:
		drum_5.play(maxtime=800)
	elif violin:
		violin_g.play(maxtime=800)

def play_6():
	# GPIO.output(16,GPIO.HIGH)
	if piano:
		piano_a.play(maxtime=800)
	elif guitar:
		guitar_6.play(maxtime=800)
	elif drum:
		drum_6.play(maxtime=800)
	elif violin:
		violin_a.play(maxtime=800)

def play_7():
	# GPIO.output(17,GPIO.HIGH)
	if piano:
		piano_b.play(maxtime=800)
	elif guitar:
		guitar_7.play(maxtime=800)
	elif drum:
		drum_7.play(maxtime=800)
	elif violin:
		violin_b.play(maxtime=800)

def play_8():
	# GPIO.output(18,GPIO.HIGH)
	if piano:
		piano_c2.play(maxtime=800)
	elif guitar:
		guitar_8.play(maxtime=800)
	elif drum:
		drum_8.play(maxtime=800)
	elif violin:
		violin_c2.play(maxtime=800)

def pattern1():
	print ("Starting pattern 1. Changing instrument to piano")
	sequence = ['a', 's', 'd', 'a', 'd', 'a', 'd', 's', 'd', 'f', 'f', 'd', 's', 'f']
	index = 0
	# Turn light on for first note
	turnOnLEDLight(sequence[index])
	while True:
		for event in pygame.event.get():
			if event.type == KEYDOWN:
				letter = pygame.key.name(event.key)
				if letter == sequence[index]:
					converter(letter)
					# When current note is stepped on, turn off the LED light for current light
					# and turn on the next light in the pattern
					turnOffLEDLight(sequence[index])
					index += 1
					if index == len(sequence):
						index = 0
					turnOnLEDLight(sequence[index])
					print (":yay match")
				elif letter == 'x':
					pattern2()
					return
				elif letter == 'c':
					pattern3()
					return
				elif letter == 'p':
					print ("Exiting pattern1")
					return
				elif event.key == K_ESCAPE:
					print ("Exiting pattern1")
					return
def pattern2():
	print ("Starting star wars theme! Changing instrument to piano")
	sequence = ['a', 'g', 'f', 'd', 's', 'k', 'g', 'f', 'd', 's', 'k', 'g', 'f', 'd', 'f', 's']
	index = 0
	turnOnLEDLight(sequence[index])
	while index < len(sequence):
		for event in pygame.event.get():
			if event.type == KEYDOWN:
				letter = pygame.key.name(event.key)
				if letter == sequence[index]:
					converter(letter)
					turnOffLEDLight(sequence[index])
					index += 1
					if index == len(sequence):
						index = 0
					turnOnLEDLight(sequence[index])
					print (":yay match")
				elif letter == 'z':
					pattern1()
					return
				elif letter == 'c':
					pattern3()
					return
				elif letter == 'p':
					print ("Exiting starwars pattern")
					return
				elif event.key == K_ESCAPE:
					print ("Exiting Exiting starwars pattern")
					return

def pattern3():
	print ("Starting pattern for only three keys")
	sequence = ['a', 's', 'd', 'a', 'd', 'a', 'd']
	index = 0
	turnOnLEDLight(sequence[index])
	while index < len(sequence):
		for event in pygame.event.get():
			if event.type == KEYDOWN:
				letter = pygame.key.name(event.key)
				if letter == sequence[index]:
					converter(letter)
					turnOffLEDLight(sequence[index])
					index += 1
					if index == len(sequence):
						index = 0
					turnOnLEDLight(sequence[index])
					print (":yay match")
				elif letter == 'z':
					pattern1()
					return
				elif letter == 'x':
					pattern2()
					return
				elif letter == 'p':
					print ("Exiting three key pattern")
					return
				elif event.key == K_ESCAPE:
					print ("Exiting three key pattern")
					return


def turnOffLEDLight(char):
	return
# 	if char == 'a':
# 		GPIO.output(11,GPIO.LOW)
# 	elif char == 's':
# 		GPIO.output(12,GPIO.LOW)
# 	elif char == 'd':
# 		GPIO.output(13,GPIO.LOW)
# 	elif char == 'f':
# 		GPIO.output(14,GPIO.LOW)
# 	elif char == 'g':
# 		GPIO.output(15,GPIO.LOW)
# 	elif char == 'h':
# 		GPIO.output(16,GPIO.LOW)
# 	elif char == 'j':
# 		GPIO.output(17,GPIO.LOW)
# 	elif char == 'k':
# 		GPIO.output(18,GPIO.LOW)

def turnOnLEDLight(char):
	return
# 	if char == 'a':
# 		GPIO.output(11,GPIO.HIGH)
# 	elif char == 's':
# 		GPIO.output(12,GPIO.HIGH)
# 	elif char == 'd':
# 		GPIO.output(13,GPIO.HIGH)
# 	elif char == 'f':
# 		GPIO.output(14,GPIO.HIGH)
# 	elif char == 'g':
# 		GPIO.output(15,GPIO.HIGH)
# 	elif char == 'h':
# 		GPIO.output(16,GPIO.HIGH)
# 	elif char == 'j':
# 		GPIO.output(17,GPIO.HIGH)
# 	elif char == 'k':
# 		GPIO.output(18,GPIO.HIGH)
		

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

	violin_c1 = pygame.mixer.Sound("violin/violin_c1.wav")
	violin_d = pygame.mixer.Sound("violin/violin_d.wav")
	violin_e = pygame.mixer.Sound("violin/violin_e.wav")
	violin_f = pygame.mixer.Sound("violin/violin_f.wav")
	violin_g = pygame.mixer.Sound("violin/violin_g.wav")
	violin_a = pygame.mixer.Sound("violin/violin_a.wav")
	violin_b = pygame.mixer.Sound("violin/violin_b.wav")
	violin_c2 = pygame.mixer.Sound("violin/violin_c2.wav")

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
	drum_7 = pygame.mixer.Sound("drum/SPARK_metal.wav")
	drum_8 = pygame.mixer.Sound("drum/Timpani2.wav")

	# GPIO.setmode(GPIO.BCM)
	# GPIO.setwarnings(False)
	# GPIO.setup(18,GPIO.OUT)
	# GPIO.setup(17,GPIO.OUT)
	# GPIO.setup(16,GPIO.OUT)
	# GPIO.setup(15,GPIO.OUT)
	# GPIO.setup(14,GPIO.OUT)
	# GPIO.setup(13,GPIO.OUT)
	# GPIO.setup(12,GPIO.OUT)
	# GPIO.setup(11,GPIO.OUT)

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
					violin = False
				elif event.key == pygame.K_w:
					piano = False
					guitar = True
					drum = False
					violin = False
				elif event.key == pygame.K_e:
					piano = False
					guitar = False
					drum = True
					violin = False
				elif event.key == pygame.K_r:
					piano = False
					guitar = False
					drum = False
					violin = True
				# Patterns
				elif event.key == pygame.K_z:
					piano = True
					guitar = False
					drum = False
					violin = False
					pattern1()
				elif event.key == pygame.K_x:
					piano = True
					guitar = False
					drum = False
					violin = False
					pattern2()
				elif event.key == pygame.K_c:
					piano = True
					guitar = False
					drum = False
					violin = False
					pattern3()
			elif event.type == KEYUP:
				letter = pygame.key.name(event.key)
				# turnOffLEDLight(letter)
				
