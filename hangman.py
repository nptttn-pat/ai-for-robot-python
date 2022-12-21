name = "chaiyo"
letter_dict = {}

number_of_trial = 5

state = 0
die = False

for char in name:
	if char not in letter_dict:
		letter_dict[char] = 1
	else:
		letter_dict[char] += 1

while number_of_trial > 0:
	char = chr(ord(input("Guess letter: "))).lower()
	if char in name and letter_dict[char] > 0:
		letter_dict[char] -= 1
		state += 1
		if state == len(name):
			break
		print("Correct, trial:", number_of_trial)
	else:
		number_of_trial -= 1
		if number_of_trial == 0:
			die = True
			break

		print("Don't have letter {}.".format(char), "trial:", number_of_trial)

if die:
	print("Die")
else:
	print("Done")
