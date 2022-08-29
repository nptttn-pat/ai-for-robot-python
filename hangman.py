
name = "chin"
i = 5
j = 5
k = 0
count = 0
round = 5
while count < round:
  a = input("Guess letter: ")
  if a in name:
          if k < 3:
            print("Correct, trial:",i)
          k += 1
          if k == 4:
            print("Done")
            round = 0
  else:
    j -= 1
    print("Don't have letter "+a+" trial:",j)
    i = j
    round = j
    if round == 0:
        print("Die")
    