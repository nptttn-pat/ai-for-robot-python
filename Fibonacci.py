while(1):
    i = int(input("Number: "))
    m, n = 1, 1
    count = 0

    if i <= 0:
        print("Input a positive number ")
    else :
        while count < i:
            print(m)
            o = m + n
            m = n
            n = o

            count += 1