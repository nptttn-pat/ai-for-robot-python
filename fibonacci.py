n = int(input("Number: "))
count = 0
n0 = 0
n1 = 1
n2 = n
while count < n:
    print(n1)
    n_new = n0 + n1
    n0 = n1
    n1 = n_new
    count += 1