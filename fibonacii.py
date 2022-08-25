def fibo(n):
    if n <=1:
        return n
    elif n == 2:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

number = int(input('Number: '))
count = 1
while(1):
    print(fibo(count))
    if count < number:
        count+=1
    else: 
        break