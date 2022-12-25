x = int(input("Number: "))
y = [1,1]
for i in range(2,x-1):
	y.append(y[i-1]+y[i-2])
	i = i+1
for j in y:
	print(j)
