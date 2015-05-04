import sys
import time
from random import randint
from datetime import datetime
#//////////////////////////////////////config//////////////////////////////////////////////////77

random_alpha= randint(1,25)			#storing a random letter from the alphabet
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]


#///////////////////////////////////////////////////////////////////////////randomize word and handle input///////////////////////////////////////////////////////////////////////////////////

def get_duration():
	len_val = raw_input("For how many words would you like to play?")
	if len_val != int:
		len_val = raw_input("You must pass an integer for how many words you want to play...")
		if len_val != int:
			sys.exit()
	else:
		return True 
	
def get_word():
	word_range = range(randint(1,11))		# A random given length to the word
	word = ""
	for n in word_range:				#For all the letters whom can be fittet in the created word_range
		x = alphabet[random_alpha]		#make x a random letter in the alphabet
		word += str(x)				#and append those random letters to the entire word_range 
	return word

def handle_input():
	_inputWord = ""				#Getting the word from raw input
	_i = raw_input()				#Checking if it is the random word and outputs 0 or 1
	_inputWord += str(_i)

	if _inputWord == get_word():
		return 1
	else:
		return 0

def wpm_counter():					
	count = 0
	if handle_input() == 1:
		start_time = datetime.now().second
		count += 1
		elapsed_time = date.now().second - start_time
		speed_now = handle_input() * (60/elapsed_time)
		return "wpm: " + speed_now
	else: 
		return "wpm: 0"


#//////////////////////////////////////////////////////	MAIN	///////////////////////////////////////////////////////////////////////

def main():
	wpm_counter()
main()









	




	
