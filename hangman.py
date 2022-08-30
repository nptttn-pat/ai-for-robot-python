Name = "guitar"
list = []
for letter in Name:
    list.append(letter)

new_list = []

x = 0
while (1):
    n = str(input("Guess letter: "))
    if x != 6:
        if n in list:
            print("Correct, trial: ",6-x)
            new_list.append(n)
            if sorted(new_list) == sorted(list):
                print("Done")
                break
        else:
            x += 1
            print("Don’t have letter "+n+ ". trial:",6-x)
    else:
       print("Die")
       break
