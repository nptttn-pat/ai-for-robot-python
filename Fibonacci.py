while(1):
    n = int(input("Number: "))
    n1, n2 = 0, 1
    count = 0
    
    if n <= 0:
       print("Error")
    elif n == 1:
       print(n)
    else:
       while count < n:
           nth = n1 + n2
           n1 = n2
           n2 = nth
           print(n1)
           count += 1
