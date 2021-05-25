#this program is to play how many fingers I am holding game.   

import random   # this is a funtion in python which help us decalre  random values in computer 
print ( "lets play how many fingers I am holding") 
def guess(x):                 #this a function declaration. we decvalred a function called guess.
	random_number = random.randint(1, x)         #This a specific to  RANDOM import in line 1.  random_numebr is decalare and random.randint(x,y) is predefined in random
	guess = 0
	while guess != random_number:
		guess = int(input(f'guess how many fingers I am holding: '))
		if guess < random_number:
				print(' yo  I  have 2 hands go high')
		elif guess > random_number:
				print('to high my dude keep go low')
	print('dyam son how you find this')

guess(10) 		#this is where we define the valuse of x from  top value. 
