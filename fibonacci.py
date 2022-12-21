def fibo_seq(seq):
	num0 = 0
	num1 = 1
	a = 0
		
	if (seq == 0):
		print(0)
		return
	for i in range(seq):
		if i == 0:
			print(1)
		else:
			a = num0 + num1
			num0 = num1
			num1 = a
			print(a)

x = int(input("Number: "))
fibo_seq(x)
