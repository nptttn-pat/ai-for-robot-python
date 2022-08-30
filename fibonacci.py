num = int(input("Number:"))
x = 0
y = 1
while num != 0:
    z = x + y
    print(y)
    x = y
    y = z
    num = num - 1


