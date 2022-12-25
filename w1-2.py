s=input("String: ")
c=s.strip().lower()
if c==c[::-1] :
	print("This word is a palindrome")
else:
	print("This word is not a palindrome")
