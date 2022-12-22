while(1) :
	i = 0
	count = 0
	x = input("String:")
	l = len(x)
	if(x == ""):
		break
	elif(l==1):
		print("This word is a palindrome")
	else:
		for i in range(0,int(l/2)):
			if(x[i]==x[len(x)-1-i] ):
				count += 1
				if(count == int(l/2)):
					print("This word is a palindrome")
					break
			else:
				print("This word is not a palindrome")
				count = 1
				break
