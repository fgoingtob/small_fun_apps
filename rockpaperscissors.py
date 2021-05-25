# to play rock paper scissors using random import in python.
#this taks is achived by combing loops and  random function. 
import random
#we have delcered action to input users action. 
player = input("Choose - rock,paper,scissors: ")
#this is our action where it will show the what are the option we have
action = ["rock, paper, scissors"]
#here we use random function to achive our action result.
task = random.choice(action)
# decalaration statement.
print (f'you choose {player} computer choose {task}.')

#loops condition starts.
if player == task:
	print (f'cmon man {player}.lets go again')
elif player == "rock":
	if task == "scissors":
		print ("Rock destroys everything , YOU WIN")
	else:
		print ("paper is like a blanket, YOU LOSE")
elif player == "paper":
	if task == "rock":
		print (" paper takes the W ,YOU WIN")
	else:
		print (" you know what cuts paper, Scissors. YOU TOOK L")
elif player == "scissors":
	if task == "paper":
		print ( " IMMA CUT you, YOU WIN")
	else:
		print ("BRUH YOU GOT SCISSORS TO ROCK FIGHT, TAKE THE L")
