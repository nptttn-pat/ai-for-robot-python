Name = 'noppanut'
sort_name = "".join(dict.fromkeys(Name))
correct = len(sort_name)
guess = correct 
count = 0
check = []
while(1):
    letter = (input('Guess letter:')).lower()
    if sort_name.find(letter) != -1:
        if letter in check:
            count -=1
        count+=1
        print(f'Corrent, trail: {guess}')
    else:
        if letter in check:
            guess+=1
        guess-=1
        print(f"Don't have letter {letter}. trail: {guess}")
    if(count == correct):
        print('Done')
        break
    elif(guess <= 0):
        print('Die')
        break
    check.append(letter)