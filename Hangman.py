name = "pat"
t = 5
i = 0
guesses = []
ans = False

while not ans:
        x = input("Guess letter: ")
        guesses.append(x)
        if x not in name:
            t -= 1
            if t == 0:
                break
            else:
                print(f"Don't have letter {x}. trial: {t}")
        else:
            i +=1
            if i == 3:
                ans = True
                break
            else:
                print(f"Correct, trial: {t}")
if ans:
    print("Done")
else:
    print("Die")
