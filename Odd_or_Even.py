while(1):
	print('Input number:',end=' ')
	x = input()
	y = int(x)%2

	if y == 0 :
		print('even')
	if y == 1 :
		print('odd')
	if x == '0' :
		break
