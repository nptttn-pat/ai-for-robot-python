name  = [x for x in 'pacawat']
count = 10
point = len(name)

while(1):
    print('Guess letter: ',end='')
    x = input()
    flag = 0
    for i in range(0,len(name)):
        if x == name[i]:
            name[i] = 0
            point = point-1
            flag = 1

    if flag == 1 :
        print('Correct,trial: ',count)
    if flag == 0 :
        print('Don\'t have letter '+x+'.,trial: ',count)

    if point == 0 :
        print('Done')
        break
    if count == 0 :
        print('Die')
        break

    count = count - 1
