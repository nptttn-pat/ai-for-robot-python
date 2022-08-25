live = 5
x = 0
answer = "nattanon"
while(live!=0):
    inp = input('Guess letter: ')
    print("Entered: ",inp)
##check##
    if(inp == "n" or inp == "a" or inp == "t" or inp == "o"):
        print("Correct, trial: ",live)
        x = x + 1
    else:
        print("Don't have letter ",inp)
        live = live - 1
        print("trial: ",live)
    if(x == 4):
        print("My name is Nattanon, You're welcome :3")
        break