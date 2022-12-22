while(1) :
	x = input("Input number: ")
	if(x == ''):
		break
	x = float(x)
	if (x%2 == 0):
		print('even')
	else:
		print('odd')
