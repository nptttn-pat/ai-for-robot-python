w="hangman"
lett=set(w)
lp=5
use= set()
while lp>0:
	if set(lett) == use:
		print("Done")
		break
	guess = input("Guess: ")
	
	if guess in lett:
		use.add(guess)
		print("Correct, trial: {}".format(lp))
	else:
		lp -= 1
		print("Don't have letter {}. trial: {}".format(guess,lp))
if lp==0:
	print("Die")
