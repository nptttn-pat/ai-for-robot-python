import random
import time

# The parameters we require to execute the game:
def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    words_to_guess = ["kanyakorn"]
    word = random.choice(words_to_guess)
    length = len(word)
    count = 0
    display = '_' * length
    already_guessed = []
    play_game = ""

# Initializing all the conditions required for the game:
def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit = 5
    guess = input("Guess letter :")
    guess = guess.strip()

    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Invalid Input, Try a letter\n")
        hangman()
    
    elif	guess in already_guessed:
            print("Try another letter.\n")

    
    while guess in word:
        if  guess in word:
            num=0
            already_guessed.extend([guess])
            index = word.find(guess)
            word = word[:index] + "_" + word[index + 1:]
            display = display[:index] + guess + display[index + 1:]
            num=num+1
    if num>0:
        print("Correct,trial:"+str(limit - count))


    else:
        count += 1
        if guess in word:
            already_guessed.extend([guess])
            index = word.find(guess)
            word = word[:index] + "_" + word[index + 1:]
            display = display[:index] + guess + display[index + 1:]
        if count == 1:

            print("Don't have letter "+ str(guess) + "."+ "trial: "+str(limit - count))

        elif count == 2:
            print("Don't have letter "+ str(guess) + "."+ "trial: "+str(limit - count))

        elif count == 3:
            print("Don't have letter "+ str(guess) + "."+ "trial: "+str(limit - count))

        elif count == 4:
            print("Don't have letter "+ str(guess) + "."+ "trial: "+str(limit - count))

        elif count == 5:
            time.sleep(1)
            print("Die")
            print("The word was:",already_guessed,word)
           

    if word == '_' * length:
        print("Done")


    elif count != limit:
        hangman()


main()


hangman()