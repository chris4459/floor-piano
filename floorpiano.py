import pygame
from pygame.locals import *

import pygame.mixer

import RPi.GPIO as GPIO
import time

# Modes
piano = True
guitar = False

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
	print ("LED 1 on")
	GPIO.output(18,GPIO.HIGH)
	if piano:
		piano_c1.play(maxtime=800)
	elif guitar:
		guitar_1.play(maxtime=800)

def play_2():
	print ("LED 2 on")
	GPIO.output(17,GPIO.HIGH)
	if piano:
		piano_d.play(maxtime=800)
	elif guitar:
		guitar_2.play(maxtime=800)

def play_3():
	if piano:
		piano_e.play(maxtime=800)
	elif guitar:
		guitar_3.play(maxtime=800)

def play_4():
	if piano:
		piano_f.play(maxtime=800)
	elif guitar:
		guitar_4.play(maxtime=800)

def play_5():
	if piano:
		piano_g.play(maxtime=800)
	elif guitar:
		guitar_5.play(maxtime=800)

def play_6():
	if piano:
		piano_a.play(maxtime=800)
	elif guitar:
		guitar_6.play(maxtime=800)

def play_7():
	if piano:
		piano_b.play(maxtime=800)
	elif guitar:
		guitar_7.play(maxtime=800)

def play_8():
	if piano:
		piano_c2.play(maxtime=800)
	elif guitar:
		guitar_8.play(maxtime=800)

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


def turnOffLEDLight(char):
	if char == 'a':
		print ("LED 1 off")
		GPIO.output(18,GPIO.LOW)
	elif char == 's':
		print ("LED 2 off")
		GPIO.output(17,GPIO.LOW)
		

if __name__=="__main__":
	pygame.display.set_mode((120, 120), DOUBLEBUF | HWSURFACE)
	pygame.mixer.pre_init(44100, -16, 2, 2048)
	pygame.mixer.init(channels=32, buffer=512)
	pygame.init()

	piano_c1 = pygame.mixer.Sound("/home/pi/Desktop/project/piano/c1.wav")
	piano_d = pygame.mixer.Sound("/home/pi/Desktop/project/piano/d.wav")
	piano_e = pygame.mixer.Sound("/home/pi/Desktop/project/piano/e.wav")
	piano_f = pygame.mixer.Sound("/home/pi/Desktop/project/piano/f.wav")
	piano_g = pygame.mixer.Sound("/home/pi/Desktop/project/piano/g.wav")
	piano_a = pygame.mixer.Sound("/home/pi/Desktop/project/piano/a.wav")
	piano_b = pygame.mixer.Sound("/home/pi/Desktop/project/piano/b.wav")
	piano_c2 = pygame.mixer.Sound("/home/pi/Desktop/project/piano/c2.wav")

	guitar_1 = pygame.mixer.Sound("/home/pi/Desktop/project/guitar/c.wav")
	guitar_2 = pygame.mixer.Sound("/home/pi/Desktop/project/guitar/d.wav")
	guitar_3 = pygame.mixer.Sound("/home/pi/Desktop/project/guitar/e.wav")
	guitar_4 = pygame.mixer.Sound("/home/pi/Desktop/project/guitar/g.wav")
	guitar_5 = pygame.mixer.Sound("/home/pi/Desktop/project/guitar/a.wav")
	guitar_6 = pygame.mixer.Sound("/home/pi/Desktop/project/guitar/dmin.wav")
	guitar_7 = pygame.mixer.Sound("/home/pi/Desktop/project/guitar/emin.wav")
	guitar_8 = pygame.mixer.Sound("/home/pi/Desktop/project/guitar/gmin.wav")

	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup(17,GPIO.OUT)
	GPIO.setup(18,GPIO.OUT)

    
	running = True
	while running:
		for event in pygame.event.get():
			if event.type == KEYDOWN:
				# _ = pygame.key.name(event.key)
				# print (_)

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
				# Patterns
				elif event.key == pygame.K_z:
					pattern1()
				elif event.key == pygame.K_x:
					pattern2()
			elif event.type == KEYUP:
				letter = pygame.key.name(event.key)
				turnOffLEDLight(letter)
				
