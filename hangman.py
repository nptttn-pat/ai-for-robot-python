name = "belle"
chk = {'b':1,'e':2,'l':2}
trial = 5

while trial > 0:
    tmp = input("Guess letter: ")
    if tmp in chk.keys() :
        print(f"Correct, trial {trial}")
        chk[tmp] -= 1
    else:
        trial -= 1
        print(f"Don,t have letter {tmp}. trial {trial}")

    if (chk['b'] <= 0) and (chk['e'] <= 0) and (chk['l'] <= 0) : 
        print("Done")
        break
if trial == 0:
    print("Die")