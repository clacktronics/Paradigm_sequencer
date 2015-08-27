import pyb, ure, os
from time import sleep
from pwm import ledpwm

adc1 = pyb.ADC('X22')
led1 = pyb.LED(1)
GreenF = 150


pin = [

  	ledpwm('Y1',8,1,GreenF),
	ledpwm('Y6',1,1,GreenF), #inv
 	ledpwm('Y2',8,2,GreenF),
 	ledpwm('Y12',1,3,GreenF),
 	ledpwm('X3',9,1,GreenF),
 	ledpwm('X6',0,0,GreenF),
	ledpwm('X5',0,0,GreenF),
 	ledpwm('Y11',1,2,GreenF) #inv
]

def allPWM(value):
	for led in pin:
		led.pwm(value)

allPWM(0)

directory = 'sequences'
sequence_cache = []
loop_read = 0

sequences = [elem for elem in os.listdir(directory) if elem[0] != '.']
sequences.sort()



for sequence in sequences:
	with open("%s/%s" % (directory,sequence)) as datatxtLine:
		for lineNumber,line in enumerate(datatxtLine):
			if ure.match('#|\n|^ *$',line) == None: 
				# Counter, this is used to select the loop, 1 when it is the first line, 2 when it is end of loop.
				if loop_read <= 1: 

					# Compile and identify the line
					# Group 1 variable detect
					# Group 2 variable name
					# Group 3 variable value
					# Group 4 sequence step (0 0 0 0 0 0 0 0)
					# Group 5 Plain text (sequence title)

					lineRead = ure.match(' *((loop|delay) *= *(\d*))?([ 0-9]*)([ a-zA-Z0-9]*)',line)

					# If plain text this is treated as a title, the space inbetween 2 titles is treated as a sequence.
					if lineRead.group(5):
						
						print(line)
						loop_read += 1

						if loop_read >= 2:

							for repeats in range(loop):
								for step in sequence_cache:
									for led_number,led in enumerate(pin):
										LED_value = int(step[led_number]) * 11
										led.pwm(LED_value)
									sleep(0.05)
							sequence_cache = []
							loop_read = 1
							
						
						Sequence_name = line


					# Variable, for loop and speed, 
					# loop = this sets how many times this sequence repeats
					# speed = the delay in-between steps

					elif lineRead.group(2) == "loop":
						loop = int(lineRead.group(3))
						print(lineRead.group(3))
					
					elif lineRead.group(4):
					 	sequence_cache.append(lineRead.group(4).replace(' ',''))

