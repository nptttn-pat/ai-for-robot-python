name = "noppanut"
listname = list(name)
i = 5
while True:
	if i > 0:
		x = input("Guess letter ")
		if x in listname:
			print("correct, trial",i)
			listname.remove(x)
			if len(listname) == 0:
				print("Done")
				break
		
		else:
			print("Don't have letter",x,"trial",i-1)
			i = i - 1
	else:
		print("Die")
		break
	
