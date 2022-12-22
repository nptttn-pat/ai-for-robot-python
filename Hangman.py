test = ('n','o','p','p','a','n','u','t')
i,limit=0,5
while(1):
	key = input("Guess letter: ")
	if(key == test[i]):
		print(f'correct,trail: {limit}')
		i += 1
		if(i==len(test)):
			print('Done')
			break
	else:
		limit -= 1
		print(f"Don't have letter {key}. trial: {limit}")
		if(limit == 0 ):
			print("Die")
			break
