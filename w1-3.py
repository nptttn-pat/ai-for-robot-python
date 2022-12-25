f=int(input("Number: "))
x=1
y=1
z=0
if f==1:
	print(x)
elif f==2:
	print(x)
	print(x)
else:
	print(x)
	print(x)
	for i in range(2,f):
		z=x+y
		print(z)
		x=y
		y=z
