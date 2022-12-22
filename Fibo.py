n = int(input("Number: "))
i,x = 0,0
a = 1 
for i in range(0,n):
	b = x + a
	x = a
	a = b
	print(x)
