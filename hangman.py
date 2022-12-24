number_of_trial = 5
used_letters = []
word = 'panawat'

while number_of_trial > 0 :
    guess = input('Guess letter:')
    if guess in word:
        used_letters.append(guess)
        if set(word) == set(used_letters):
            break
        else:
            print(f'Correct, trial:{number_of_trial}')
    else:
        number_of_trial  = number_of_trial-1
        if number_of_trial != 0:
            print(f"Don't have letter {guess}. trial:{number_of_trial}")
    
  
if set(word) == set(used_letters):
    print('Done')
else:
    print('Die')
     

