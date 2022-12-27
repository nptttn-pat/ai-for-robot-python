word = "krit"
length = len(word)
count = 0
limit = 5
guessed = []

while(1):
    
    guess = input("Guess letter: ")
    
    if guess in word:
        guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "" + word[index + 1:]
        print("Correct, Trial: " + str(limit - count))
    else :
        count += 1
        if count == limit:
            print("Die")
            break
        print(f"Don't have letter {guess}. trial: {limit - count}")
        
    if word == ""*length:
        print("Done")
        break