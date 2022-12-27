#This is fibonacci program
def fibo(num):
    x = 1
    prev =[0]    
    for i in range(1,num+1):
        prev.append(x)
        print(x)        
        x += prev[i-1]
        
while(1):
    number = int(input("Number: "))
    fibo(number)

