def isPalindrome(s):
	for i in range(len(s) // 2):
		if x[i] != s[-1 - i]:
			return 0
	return 1


x = input("String: ")
print("This word is a palindrome" if isPalindrome(x) else "This word is not a palindrome")
