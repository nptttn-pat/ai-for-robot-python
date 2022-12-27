#Let's guess my name
def guess(word,maxguess):
    word = word.lower()
    cWord =["_" for letter in word]
    while(1):
        guess = input("Guess letter:").lower()
        if guess in word:
            print("Correct!, trial left: ",maxguess)
            for i in range(len(word)):
                if word[i] == guess:
                    cWord[i] = guess
        else:
            maxguess -= 1
            print("Don't have letter ",guess," trial left: ",maxguess)
            if(maxguess == 0):
                print("Die")
                return
        for i in cWord:
            print(i.upper(),end ="")
        print(" ")
        if cWord == list(word):
            print("DONE!")
            return
        
guess("Settapong",5) 
            
