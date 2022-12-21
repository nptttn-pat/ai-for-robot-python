num = int(input("Number: "))

a = 1 
b = 1

cnt = 3 

if num > 1:
    print(a)
    print(b)
else :
    print(a)

if num > 0:
    while cnt <= num :
        tmp = b
        b = a + tmp
        a = tmp
        cnt += 1
        print(b)
