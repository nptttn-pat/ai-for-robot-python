answer = {'e':1,'a':1,'r':1,'t':1,'h':1}
num_char = sum([i for i in answer.values()])
trail = 5
while(trail!=0):
    letter = input('Guess letter: ')
    if letter in answer.keys() and answer[letter.lower()]:
        answer[letter.lower()] -= 1
        num_char -= 1
        if not num_char:
            print('Done')
            break
        print(f'Correct, trial: {trail}')
    else:
        trail -= 1
        if not trail:
            print('Die')
            break
        print(f"Don’t have letter {letter}. trial: {trail}")
        
