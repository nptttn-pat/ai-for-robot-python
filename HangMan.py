Name = "noppanutp"
Trial = len(set(Name))
found_index = 0
while Trial >= 0:
  start = 0
  alphabet = input('Guess letter: ')
  Trial = Trial - 1
  count = 0
  while start<len(Name) :
      found_index = Name.find(alphabet,0,len(Name))
      if found_index >= 0 :
        count = count+1
        Name = Name[:found_index] + Name[found_index + 1:]
      elif found_index == -1:
        if count>0:
          print('Correct, trial: ',Trial)
          break
        elif count==0 and Trial ==0:
          print('Die')
          exit()
        else:
          print('Don’t have letter %s. trial: %d '%(alphabet,Trial))
          break
  if Trial == 0 and count>0:
    print('Done')
    break
    